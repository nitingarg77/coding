# *args and ** kwargs are used to allow for flexible argument passing.
def create_shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip_code')}")


create_shipping_label("Mr.", "John", "Doe", "2nd", street="123 Main St", city="Anytown", state="CA", zip_code="12345")