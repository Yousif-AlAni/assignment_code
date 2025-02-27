class DeliveryOrder:
    """This class represents a delivery order with order details."""

    def __init__(self, order_number, reference_number, delivery_date, delivery_method, total_weight):
        self.__order_number = order_number  # order number
        self.__reference_number = reference_number  # reference number
        self.__delivery_date = delivery_date  # delivery date
        self.__delivery_method = delivery_method  # delivery method
        self.__total_weight = total_weight  # total weight of the delivery

    def get_order_number(self):
        return self.__order_number  # return order number

    def set_order_number(self, order_number):
        self.__order_number = order_number  # update order number

    def calculate_delivery_cost(self):
        pass  # calculate cost based on weight and method


class Item:
    """This class represents an item in a delivery order."""

    def __init__(self, item_code, description, quantity, unit_price):
        self.__item_code = item_code  # item code
        self.__description = description  # item description
        self.__quantity = quantity  # item quantity
        self.__unit_price = unit_price  # price per unit

    def calculate_total_price(self):
        return self.__quantity * self.__unit_price  # total cost of item


class Recipient:
    """This class represents the recipient of a delivery."""

    def __init__(self, name, contact, address):
        self.__name = name  # recipient name
        self.__contact = contact  # recipient contact
        self.__address = address  # recipient address

    def validate_contact(self):
        pass  # validate contact details


class DeliveryNote:
    """This class generates a delivery note with order and recipient details."""

    def __init__(self, delivery_order, recipient, items):
        self.__delivery_order = delivery_order  # delivery order details
        self.__recipient = recipient  # recipient details
        self.__items = items  # list of items in the order

    def generate_note(self):
        pass  # generate delivery note


# Usage
recipient = Recipient("Sarah Johnson", "sarah.johnson@example.com", "45 Knowledge Avenue, Dubai, UAE")
item1 = Item("ITM001", "Wireless Keyboard", 1, 100)
item2 = Item("ITM002", "Wireless Mouse & Pad Set", 1, 75)
item3 = Item("ITM003", "Laptop Cooling Pad", 1, 120)
item4 = Item("ITM004", "Camera Lock", 3, 15)

order = DeliveryOrder("DEL123456789", "DN-2025-001", "January 25, 2025", "Courier", 7)

delivery_note = DeliveryNote(order, recipient, [item1, item2, item3, item4])

# Placeholder for actual note generation
print("Delivery Note for", recipient._Recipient__name, "at", recipient._Recipient__address)
