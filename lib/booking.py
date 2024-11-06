class Booking:
    def __init__(self, id, listing_id, guest_id, check_in, check_out, status):
        self.id = id
        self.listing_id = listing_id
        self.guest_id = guest_id
        self.check_in = check_in
        self.check_out = check_out
        self.status = status

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Booking({self.id}, {self.listing_id}, {self.guest_id}, {self.check_in}, {self.check_out}, {self.status})"

    def is_valid(self):
        if self.listing_id is None or self.listing_id == "":
            return False
        if self.guest_id is None or self.guest_id == "":
            return False
        if self.status is None or self.status == "":
            return False
        return True
      
    def generate_errors(self):
        errors = []
        if self.listing_id is None or self.listing_id == "":
            errors.append("Please select a property")
        if self.guest_id is None or self.guest_id == "":
            errors.append("Please log in")
        if self.status is None or self.status =="":
            errors.append("Please submit valid dates")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)
