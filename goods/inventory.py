import datetime


class Inventory:
    _id: int
    _name: str
    _brand: str
    _model: str
    _count: float
    _unit: str
    _price: float
    _date = datetime.date

    def __init__(self, name: str, brand: str, model: str, count: float, unit: str, price: float):
        self._id = -1
        self._name = name
        self._brand = brand
        self._model = model
        self._count = count
        self._unit = unit
        self._price = price
        self._date = datetime.datetime.now()

    def __str__(self):
        return f"{self._id}: {self._name} {self._brand} {self._model} {self._count} {self._unit} {self._date}"

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
        self._price = self._price if price is None else price
        self._date = datetime.datetime.now()
        return self._price

    def index(self, index: int = None):
        self._id = self._id if index is None or index < 0 else index
        self._date = datetime.datetime.now()
        return self._id

    def date(self, update: bool = False):
        self._date = datetime.datetime.now() if update else self._date
        str_time = self._date.strftime("%Y-%m-%d %H:%M:%S")
        return str_time




