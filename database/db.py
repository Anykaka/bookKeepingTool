import sqlite3
import os
from goods.inventory import Inventory
from goods.expense import Expense
from goods.traded import Traded


class DataBaseManager:
    inventory_path = os.getcwd() + os.sep + "database" + os.sep + 'inventory.db'
    expense_path = os.getcwd() + os.sep + "database" + os.sep + 'expense.db'
    traded_path = os.getcwd() + os.sep + "database" + os.sep + 'traded.db'

    inventory_select = "inventory"
    expense_select = "test"
    traded_select = "test"

    def __init__(self):
        """
        数据库管理, 总共分为进货清单、销货清单两种，提供每个清单的增删改查
        进货清单要求记录：货品名、货品品牌、货品型号、货品数量、货品单位、货品进价、进货日期
        出货清单按照项目划分，不同项目创建不同的表单，表单内容要求记录：货品名、货品品牌、货品型号、货品数量、货品单位、货品进价、货品售价、折扣信息、货品成交价、
        销货成交清单：记录项目、货品总进价、货品总售价、货品折前优惠价格、货品最终折扣、货品折后优惠价格、货品总计优惠价格、货品成交总价、
        """

        # 创建库存数据库，并检查inventory表单是否存在，不存在则添加，这个表单是默认表单
        self.inventory = sqlite3.connect(self.inventory_path)
        self.inventory_cursor = self.inventory.cursor()
        self.create_inventory_table(self.inventory_select)

        # 创建出货数据库
        self.expense = sqlite3.connect(self.expense_path)
        self.expense_cursor = self.expense.cursor()
        self.create_expense_table(self.expense_select)

        # 创建成交数据库
        self.traded = sqlite3.connect(self.traded_path)
        self.traded_cursor = self.traded.cursor()
        self.create_traded_table(self.traded_select)

    def check_table(self, cursor, table_name) -> bool:
        """
        检查指定数据库是否存在指定表单
        :param cursor: 数据库游标
        :param table_name: 表单名
        """
        exec_command = '''
            select name FROM sqlite_master WHERE type= "table" AND name = ?
        '''
        cursor.execute(exec_command, (table_name,))
        result = cursor.fetchall()
        return len(result) > 0

    def create_inventory_table(self, table_name) -> bool:
        """
        添加一个库存表单，存放进货的物品，表单包括货品名、货品品牌、货品型号、货品数量、货品单位、货品进价、进货日期
        """
        if self.check_table(self.inventory_cursor, table_name) is True:
            return True
        exec_command = f'''
            CREATE TABLE {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name text not null,
                            brand text not null,
                            model text not null,
                            count float mot null,
                            unit text not null,
                            price float not null,
                            date text not null);
        '''
        self.inventory_cursor.execute(exec_command, ())
        return True

    def create_expense_table(self, table_name) -> bool:
        """
        添加一个项目销货表单，货品名、货品品牌、货品型号、货品数量、货品单位、货品进价、货品售价、折扣信息、货品成交价、销售日期
        """
        if self.check_table(self.expense_cursor, table_name) is True:
            return True
        exec_command = f'''
            CREATE TABLE {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name text not null,
                            brand text not null,
                            model text not null,
                            count float mot null,
                            unit text not null,
                            price float not null,
                            value float not null,
                            rebate float not null,
                            last_value float not null,
                            date text not null);
        '''
        self.expense_cursor.execute(exec_command, ())
        return True

    def create_traded_table(self, table_name) -> bool:
        """
        添加一个销货统计表单，货品总进价、货品总售价、货品折前优惠价格、货品最终折扣、货品折后优惠价格、货品总计优惠价格、货品成交总价、成交日期
        """
        if self.check_table(self.traded_cursor, table_name) is True:
            return True
        exec_command = f'''
            CREATE TABLE {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            in_price float not null,
                            out_price float not null,
                            before_rebate_loss float not null,
                            rebate float not null,
                            after_rebate_loss float not null,
                            all_loss float not null,
                            value float not null,
                            date text not null);
        '''
        self.traded_cursor.execute(exec_command, ())
        return True


    def get_tables(self, cursor) -> list:
        """
        获取数据库所有表单, 返回表单列表
        """
        exec_command = f'''
            SELECT name FROM sqlite_master WHERE type='table' order by name
        '''
        cursor.execute(exec_command, ())
        result = cursor.fetchall()
        return result

    def drop_table(self, cursor, table_name) -> bool:
        """
        删除指定数据库的指定表单
        """
        if self.check_table(cursor, table_name) is True:
            exec_command = f'''
                DROP TABLE {table_name};
            '''
            cursor.execute(exec_command)
            result = cursor.fetchall()
            return True
        else:
            print(f"Not found table: {table_name}, drop failed.")
            return False

    def create(self, goods=None):
        """
        添加物品，会根据物品的类型添加到指定的数据库
        """
        if isinstance(goods, Inventory):
            return self.create_inventory(goods)
        elif isinstance(goods, Expense):
            return self.create_expense(goods)
        elif isinstance(goods, Traded):
            return self.create_traded(goods)
        else:
            return False

    def create_inventory(self, goods: Inventory):
        """
        添加进货物品，会检查仓库内是否有相同的货物，如果货物存在相同的则无法添加
        :param goods:
        :return:
        """
        if self.check_inventory_goods(goods):
            print(f"Goods {goods.name()} index is already created, if you want change it, please use update interface.")
            return False
        exec_command = f'''
            INSERT INTO {self.inventory_select} ('name', 'brand', 'model', 'count', 'unit', 'price', 'date') 
            VALUES ('{goods.name()}', '{goods.brand()}', '{goods.model()}', {goods.count()}, '{goods.unit()}', {goods.price()}, '{goods.date()}');
        '''
        self.inventory_cursor.execute(exec_command)
        goods.index(self.inventory_cursor.lastrowid)
        self.inventory.commit()
        return True

    def check_inventory_goods(self, goods: Inventory):
        """
        根据货物的名字、品牌、型号判断是否存在相同的货品
        :param goods:
        :return:
        """
        exec_command = f'''
            SELECT * FROM {self.inventory_select}
            WHERE name = '{goods.name()}' AND brand = '{goods.brand()}' AND model = '{goods.model()}' AND unit = '{goods.unit()}';
        '''
        self.inventory_cursor.execute(exec_command)
        result = self.inventory_cursor.fetchall()
        return len(result) > 0

    def change_object(self, name):
        """
        修改当前选中的数据库表单，并调用添加表单接口添加它
        """
        self.expense_select = name
        self.traded_select = name
        self.create_expense_table(self.expense_select)
        self.create_traded_table(self.traded_select)

    def create_expense_goods(self, goods: Expense):
        """
        新增一个销货清单商品
        """
        exec_command = f'''
            INSERT INTO {self.expense_select} ('name', 'brand', 'model', 'count', 'unit', 'price', 'value', 'rebate', 'last_value', 'date') 
            VALUES ('{goods.name()}', '{goods.brand()}', '{goods.model()}', {goods.count()}, '{goods.unit()}', {goods.price()}, 
                     {goods.value()}, {goods.rebate()}, {goods.last_value()}, '{goods.date()}');
        '''
        self.expense_cursor.execute(exec_command)
        goods.index(self.expense_cursor.lastrowid)
        self.inventory.commit()
        return True



def main():
    db = DataBaseManager()
    goods = Inventory("苹果", "富士", "AX1", 10.0, "斤", 3.0)
    db.create(goods)
