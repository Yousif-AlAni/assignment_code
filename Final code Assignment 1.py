class DeliveryOrder:
    """This class represents a delivery order with order details."""

    def __init__(self, order_number, reference_number, delivery_date, delivery_method, total_weight, status):
        # Order details
        self.__order_number = order_number  # Unique ID for the order
        self.__reference_number = reference_number  # Order tracking reference
        self.__delivery_date = delivery_date  # Scheduled delivery date
        self.__delivery_method = delivery_method  # How the order will be delivered (e.g., courier)
        self.__total_weight = total_weight  # Total weight of the delivery
        self.__status = status  # Status of the order (e.g., pending, shipped)

    # Getter and setter methods for attributes
    def get_order_number(self):
        return self.__order_number  # Returns the order number

    def set_order_number(self, order_number):
        self.__order_number = order_number  # Updates the order number

    def get_status(self):
        return self.__status  # Returns the order status

    def set_status(self, status):
        self.__status = status  # Updates the order status

    def calculate_delivery_cost(self):
        pass  # This function will calculate the delivery cost based on weight and method


class Item:
    """This class represents an item in a delivery order."""

    def __init__(self, item_code, description, quantity, unit_price, category):
        # Item details
        self.__item_code = item_code  # Unique item code
        self.__description = description  # Short description of the item
        self.__quantity = quantity  # Number of units ordered
        self.__unit_price = unit_price  # Price per unit
        self.__category = category  # Category of the item (e.g., electronics, furniture)

    # Getter and setter methods
    def get_item_code(self):
        return self.__item_code  # Returns the item code

    def set_item_code(self, item_code):
        self.__item_code = item_code  # Updates the item code

    def calculate_total_price(self):
        return self.__quantity * self.__unit_price  # Calculates total cost of the item


class Recipient:
    """This class represents the recipient of a delivery."""

    def __init__(self, name, contact, address, email, postal_code):
        # Recipient details
        self.__name = name  # Full name of the recipient
        self.__contact = contact  # Phone number or email
        self.__address = address  # Delivery address
        self.__email = email  # Email address of recipient
        self.__postal_code = postal_code  # Postal code for delivery

    # Getter and setter methods
    def get_name(self):
        return self.__name  # Returns the recipient's name

    def set_name(self, name):
        self.__name = name  # Updates the recipient's name

    def validate_contact(self):
        pass  # This function will check if the contact details are valid


class DeliveryNote:
    """This class generates a delivery note with order and recipient details."""

    def __init__(self, delivery_order, recipient, items, note_date, note_id):
        # Delivery note details
        self.__delivery_order = delivery_order  # The order this note is for
        self.__recipient = recipient  # Recipient details
        self.__items = items  # List of items in the order
        self.__note_date = note_date  # Date the note is created
        self.__note_id = note_id  # Unique ID for the delivery note

    # Getter and setter methods
    def get_note_id(self):
        return self.__note_id  # Returns the delivery note ID

    def set_note_id(self, note_id):
        self.__note_id = note_id  # Updates the delivery note ID

    def generate_note(self):
        pass  # This function will generate a formatted delivery note with order details


# Example Usage
# Creating a recipient
recipient = Recipient("Sarah Johnson", "sarah.johnson@example.com", "45 Knowledge Avenue, Dubai, UAE",
                      "sarah@example.com", "12345")

# Creating items for the order
item1 = Item("ITM001", "Wireless Keyboard", 1, 100, "Electronics")
item2 = Item("ITM002", "Wireless Mouse & Pad Set", 1, 75, "Accessories")
item3 = Item("ITM003", "Laptop Cooling Pad", 1, 120, "Electronics")
item4 = Item("ITM004", "Camera Lock", 3, 15, "Security")

# Creating a delivery order
order = DeliveryOrder("DEL123456789", "DN-2025-001", "January 25, 2025", "Courier", 7, "Shipped")

# Creating a delivery note
delivery_note = DeliveryNote(order, recipient, [item1, item2, item3, item4], "January 26, 2025", "DN123")

# Placeholder for actual note generation
print("Delivery Note for", recipient.get_name(), "at", recipient._Recipient__address)
