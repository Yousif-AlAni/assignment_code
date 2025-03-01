class DeliveryOrder:
    """This class represents a delivery order with order details."""

    def __init__(self, order_number, reference_number, delivery_date, delivery_method, total_weight, status):
        self.__order_number = order_number
        self.__reference_number = reference_number
        self.__delivery_date = delivery_date
        self.__delivery_method = delivery_method
        self.__total_weight = total_weight
        self.__status = status

    def get_order_number(self):
        return self.__order_number

    def get_reference_number(self):
        return self.__reference_number

    def get_delivery_date(self):
        return self.__delivery_date

    def get_delivery_method(self):
        return self.__delivery_method

    def get_total_weight(self):
        return self.__total_weight

    def get_status(self):
        return self.__status


class Item:
    """This class represents an item in a delivery order."""

    def __init__(self, item_code, description, quantity, unit_price, category):
        self.__item_code = item_code
        self.__description = description
        self.__quantity = quantity
        self.__unit_price = unit_price
        self.__category = category

    def get_item_code(self):
        return self.__item_code

    def get_description(self):
        return self.__description

    def get_quantity(self):
        return self.__quantity

    def get_unit_price(self):
        return self.__unit_price

    def calculate_total_price(self):
        return self.__quantity * self.__unit_price


class Recipient:
    """This class represents the recipient of a delivery."""

    def __init__(self, name, contact, address, email, postal_code):
        self.__name = name
        self.__contact = contact
        self.__address = address
        self.__email = email
        self.__postal_code = postal_code

    def get_name(self):
        return self.__name

    def get_contact(self):
        return self.__contact

    def get_address(self):
        return self.__address

    def get_email(self):
        return self.__email

    def get_postal_code(self):
        return self.__postal_code


class DeliveryNote:
    """This class generates a delivery note with order and recipient details."""

    def __init__(self, delivery_order, recipient, items, note_date, note_id):
        self.__delivery_order = delivery_order
        self.__recipient = recipient
        self.__items = items
        self.__note_date = note_date
        self.__note_id = note_id

    def generate_note(self):
    #Generate and display a formatted delivery note.

        # Print header for the delivery note
        print("")
        print("========================================")
        print("             DELIVERY NOTE             ")
        print("========================================")

        # Print delivery note details
        print("Delivery Note ID:", self.__note_id)
        print("Date:", self.__note_date)
        print("----------------------------------------")

        # Print order details
        print("Order Number:", self.__delivery_order.get_order_number())
        print("Reference Number:", self.__delivery_order.get_reference_number())
        print("Delivery Date:", self.__delivery_order.get_delivery_date())
        print("Delivery Method:", self.__delivery_order.get_delivery_method())
        print("Total Weight:", self.__delivery_order.get_total_weight(), "kg")
        print("Status:", self.__delivery_order.get_status())
        print("----------------------------------------")

        # Print recipient details
        print("Recipient Information:")
        print("Name:", self.__recipient.get_name())
        print("Contact:", self.__recipient.get_contact())
        print("Address:", self.__recipient.get_address())
        print("Email:", self.__recipient.get_email())
        print("Postal Code:", self.__recipient.get_postal_code())
        print("----------------------------------------")

        # Print item details (header row)
        print("Items:")
        print("Item Code  Description                  Qty  Unit Price  Total")
        print("-------------------------------------------------------------")

        # Loop through each item and print its details
        for item in self.__items:
            print(item.get_item_code(), item.get_description(), item.get_quantity(), item.get_unit_price(),
                  item.calculate_total_price())

        # Print footer to mark the end of the delivery note
        print("========================================")
        print("         END OF DELIVERY NOTE           ")
        print("========================================")
        print("")


# Example Usage

# Create recipient
recipient = Recipient("Sarah Johnson", "123-456-7890", "45 Knowledge Avenue, Dubai, UAE", "sarah@example.com", "12345")

# Create items
item1 = Item("ITM001", "Wireless Keyboard", 1, 100, "Electronics")
item2 = Item("ITM002", "Wireless Mouse & Pad Set", 1, 75, "Accessories")
item3 = Item("ITM003", "Laptop Cooling Pad", 1, 120, "Electronics")
item4 = Item("ITM004", "Camera Lock", 3, 15, "Security")

# Create delivery order
order = DeliveryOrder("DEL123456789", "DN-2025-001", "January 25, 2025", "Courier", 7, "Shipped")

# Create delivery note
delivery_note = DeliveryNote(order, recipient, [item1, item2, item3, item4], "January 26, 2025", "DN123")

# Generate and display the delivery note
delivery_note.generate_note()
