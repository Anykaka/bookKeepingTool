import datetime


class Expense:
    _id: int
    _name: str
    _brand: str
    _model: str
    _count: float
    _unit: str
    _price: float
    _value: float
    _rebate: float
    _last_value: float
    _date = datetime.date

    def __init__(self, name: str, brand: str, model: str, count: float, unit: str, price: float, value: float, rebate: float, last_value: float):
        self._id = -1
        self._name = name
        self._brand = brand
        self._model = model
        self._count = count
        self._unit = unit
        self._price = price
        self._value = value
        self._rebate = rebate
        self._last_value = last_value
        self._date = datetime.datetime.now()

    def name(self, name: str = None):
        self._name = self._name if name is None else name
        self._date = datetime.datetime.now()
        return self._name

    def brand(self, brand: str = None):
        self._brand = self._brand if brand is None else brand
        self._date = datetime.datetime.now()
        return self._brand

    def model(self, model: str = None):
        self._model = self._model if model is None else model
        self._date = datetime.datetime.now()
        return self._model

    def count(self, count: float = None):
        self._count = self._count if count is None else count
        self._date = datetime.datetime.now()
        return self._count

    def unit(self, unit: str = None):
        self._unit = self._unit if unit is None else unit
        self._date = datetime.datetime.now()
        return self._unit

    def price(self, price: float = None):
        self._price = self._value if price is None else price
        self._date = datetime.datetime.now()
        return self._price

    def value(self, value: float = None):
        self._value = self._value if value is None else value
        self._date = datetime.datetime.now()
        return self._value

    def rebate(self, rebate: float = None):
        self._rebate = self._rebate if rebate is None else rebate
        self._date = datetime.datetime.now()
        return self._rebate

    def last_value(self, last_value: float = None):
        self._last_value = self._last_value if last_value is None else last_value
        self._date = datetime.datetime.now()
        return self._last_value

    def index(self, index: int = None):
        self._id = self._id if index is None or index < 0 else index
        self._date = datetime.datetime.now()
        return self._id

    def date(self, update: bool = False):
        self._date = datetime.datetime.now() if update else self._date
        return self._date
