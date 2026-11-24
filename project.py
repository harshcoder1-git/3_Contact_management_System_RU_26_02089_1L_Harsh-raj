contacts = []


def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10


def is_duplicate_phone(phone):
    for person in contacts:
        if person["phone"] == phone:
            return True
    return False


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()

    if not is_valid_phone(phone):
        print("Invalid phone number. Enter exactly 10 digits.")
        return

    if is_duplicate_phone(phone):
        print("Contact with this number already exists.")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    print(f"Contact added: {name} | {phone}")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    for person in contacts:
        print(f"{person['name']} | {person['phone']} | {person['email']}")


def search_contact():
    query = input("Enter name to search: ").strip().lower()
    found = False

    for person in contacts:
        if query in person["name"].lower():
            print(f"{person['name']} | {person['phone']} | {person['email']}")
            found = True

    if not found:
        print("Contact not found.")


def update_contact():
    name = input("Enter name to update: ").strip().lower()
    new_phone = input("Enter new phone: ").strip()

    if not is_valid_phone(new_phone):
        print("Invalid phone number. Enter exactly 10 digits.")
        return

    for person in contacts:
        if person["name"].lower() == name:
            if person["phone"] != new_phone and is_duplicate_phone(new_phone):
                print("Contact with this number already exists.")
                return
            person["phone"] = new_phone
            print(f"Phone updated: {new_phone}")
            return

    print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ").strip().lower()

    for i, person in enumerate(contacts):
        if person["name"].lower() == name:
            deleted_name = person["name"]
            contacts.pop(i)
            print(f"Contact '{deleted_name}' deleted. Total contacts: {len(contacts)}")
            return

    print("Contact not found.")


def main():
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()