class Venue:
    """A class representing a venue with ID, charge per hour, and venue type."""

    def __init__(self, venue_id, charge_per_hour, venue_type):
        self.__venue_id = venue_id
        self.__charge_per_hour = charge_per_hour
        self.__venue_type = venue_type

    # Getter methods
    def get_venue_id(self):
        return self.__venue_id

    def get_charge_per_hour(self):
        return self.__charge_per_hour

    def get_venue_type(self):
        return self.__venue_type

    # Setter methods
    def set_venue_id(self, venue_id):
        self.__venue_id = venue_id

    def set_charge_per_hour(self, charge_per_hour):
        self.__charge_per_hour = charge_per_hour

    def set_venue_type(self, venue_type):
        self.__venue_type = venue_type

    # Method to display venue details
    def display_details(self):
        print("Venue ID:", self.__venue_id, "Charge per Hour:", self.__charge_per_hour, "Venue Type:",
              self.__venue_type)


# Creating objects based on the table
table_venues = [
    Venue("001", 1000, "Auditorium"),
    Venue("002", 800, "Lab"),
    Venue("003", 500, "Classroom"),
    Venue("004", 700, "Lab")
]

# Displaying details of each venue
for venue in table_venues:
    venue.display_details()
