import datetime


class Traded:
    _id: int
    _in_price: float
    _out_price: float
    _before_rebate_loss: float
    _rebate: float
    _after_rebate_loss: float
    _all_loss: float
    _value: float
    _date: datetime.date

    def __init__(self, in_price: float, out_price: float, before: float, rebate: float, after: float, all_loss: float, value: float):
        self._id = -1
        self._in_price = in_price
        self._out_price = out_price
        self._before_rebate_loss = before
        self._rebate = rebate
        self._after_rebate_loss = after
        self._all_loss = all_loss
        self._value = value
        self._date = datetime.datetime.now()

    def in_price(self, in_price: float = None):
        self._in_price = self._in_price if in_price is None else in_price
        self._date = datetime.datetime.now()
        return self._in_price

    def out_price(self, out_price: float = None):
        self._out_price = self._out_price if out_price is None else out_price
        self._date = datetime.datetime.now()
        return self._out_price

    def before_rebate_loss(self, before: float = None):
        self._before_rebate_loss = self._before_rebate_loss if before is None else before
        self._date = datetime.datetime.now()
        return self._before_rebate_loss

    def after_rebate_loss(self, after: float = None):
        self._after_rebate_loss = self._after_rebate_loss if after is None else after
        self._date = datetime.datetime.now()
        return self._after_rebate_loss

    def all_loss(self, all_loss: float = None):
        self._all_loss = self._all_loss if all_loss is None else all_loss
        self._date = datetime.datetime.now()
        return self._all_loss

    def value(self, value: float = None):
        self._value = value if value is not None else self._value
        self._date = datetime.datetime.now()
        return self._value

    def index(self, index: int = None):
        self._id = self._id if index is None or index < 0 else index
        self._date = datetime.datetime.now()
        return self._id

    def date(self, update: bool = False):
        self._date = datetime.datetime.now() if update else self._date
        return self._date

