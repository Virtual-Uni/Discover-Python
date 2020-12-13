from Owner import Owner
from Tenant import Tenant
from Apartment import Apartment


def create_owner(name, address, phone):
    return Owner(name, address, phone)


def create_apartment(apartment_type, size, no_rooms, bau_year, address, apartment_owner):
    return Apartment(apartment_type, size, no_rooms, None, None, bau_year, address, apartment_owner, None)


def create_tenant(name, address, phone):
    return Tenant(name, address, phone)


def rent_apartment(apartment, tenant, duration, rent):
    apartment.set_tenant(tenant=tenant)
    apartment.set_duration(duration=duration)
    apartment.set_rent(rent=rent)


def change_owner(owner, apartment):
    apartment.set_owner(owner=owner)


def search_apartment(apartment) :
    print("apartment information")
    print("#####################")
    print("apartemnt owner:", apartment.get_owner().get_name())
    print("#####################")

if __name__ == '__main__':
    owner = create_owner("Asif", "Munich", "0123")
    apartment = create_apartment("private", 30, 3, 1990, "Munich", owner)
    tenant = create_tenant("Saiful", "Munich", "01234")

    rent_apartment(apartment, tenant, 2, 500)
    search_apartment(apartment)


