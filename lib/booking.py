from datetime import datetime

class Booking:
    def __init__(self, id, listing_id, user_id, check_in, check_out, status):
        self.id = id
        self.listing_id = listing_id
        self.user_id = user_id
        self.check_in = datetime.strptime(check_in, "%Y-%m-%d").date()
        self.check_out = datetime.strptime(check_out, "%Y-%m-%d").date()
        self.status = status

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Booking({self.id}, {self.listing_id}, {self.user_id}, {self.check_in}, {self.check_out}, {self.status})"
