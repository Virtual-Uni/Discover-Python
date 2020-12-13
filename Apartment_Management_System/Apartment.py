class Apartment:

    def __init__(self, apartment_type, size, no_rooms, rent, duration, bau_year, address, owner, tenant):
        self.apartment_type = apartment_type
        self.size = size
        self.no_rooms = no_rooms
        self.rent = rent
        self.duration = duration
        self.bau_year = bau_year
        self.address = address
        self.owner = owner
        self.tenant = tenant


    def get_apartment_type(self):
        return self.apartment_type

    def get_size(self):
        return self.size

    def get_no_rooms(self):
        return self.no_rooms

    def get_rent(self):
        return self.rent

    def get_duration(self):
        return self.duration

    def get_bau_year(self):
        return self.bau_year

    def get_address(self):
        return self.address

    def get_owner(self):
        return self.owner

    def get_tenant(self):
        return self.tenant

    def set_apartment_type(self, apartment_type):
        self.apartment_type = apartment_type

    def set_no_rooms(self, no_rooms):
        self.no_rooms = no_rooms

    def set_rent(self, rent):
        self.rent = rent

    def set_duration(self, duration):
        self.duration = duration

    def set_address(self, address):
        self.address = address

    def set_owner(self, owner):
        self.owner = owner

    def set_tenant(self, tenant):
        self.tenant = tenant
