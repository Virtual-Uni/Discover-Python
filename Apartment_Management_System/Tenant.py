class Tenant:

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

    def set_address(self, address):
        self.address = address

    def set_phone(self, phone):
        self.phone = phone