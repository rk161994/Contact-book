contacts = {}

def add_contact(name, phone_number):
    contacts[name] = phone_number
    print(f"Added {name} to contacts with phone number {phone_number}")

def search_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"{name} not found in contacts")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts")
    else:
        print(f"{name} not found in contacts")

def print_contacts():
    print("Contacts:")
    for name, phone_number in contacts.items():
        print(f"{name}: {phone_number}")

# Example usage
add_contact("Alice", "1234567890")
add_contact("Bob", "9876543210")
print_contacts()
search_contact("Alice")
delete_contact("Bob")
print_contacts()
