class
Customer:
"""This class stores customer details"""


def __init__(self, name, contact, address):
    self._name = name  # customer name
    self._contact = contact  # customer phone or email
    self._address = address  # customer address


def get_details(self):
    return f"Name: {self._name}, Contact: {self._contact}, Address: {self._address}"


def update_address(self, new_address):
    self._address = new_address  # change address


class Order:
    """This class handles order details"""

    def __init__(self, order_id, reference_number, delivery_date, items):
        self._order_id = order_id  # unique order id
        self._reference_number = reference_number  # reference number
        self._delivery_date = delivery_date  # delivery date
        self._items = items  # list of items in the order
        self._total_price = 0  # total order price (calculated later)
