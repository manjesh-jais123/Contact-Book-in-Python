import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, 'r') as file:
        return json.load(file)

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts = load_contacts()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    print("Contact added successfully!\n")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.\n")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")
    print()

def search_contact():
    query = input("Search by name or phone: ").lower()
    contacts = load_contacts()
    found = [c for c in contacts if query in c['name'].lower() or query in c['phone']]

    if not found:
        print("No matching contacts found.\n")
    else:
        for c in found:
            print(f"{c['name']} | {c['phone']} | {c['email']} | {c['address']}")
        print()

def update_contact():
    name = input("Enter the name of the contact to update: ")
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Leave blank to keep current value.")
            contact['phone'] = input(f"Phone [{contact['phone']}]: ") or contact['phone']
            contact['email'] = input(f"Email [{contact['email']}]: ") or contact['email']
            contact['address'] = input(f"Address [{contact['address']}]: ") or contact['address']
            save_contacts(contacts)
            print("Contact updated successfully.\n")
            return
    print("Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    contacts = load_contacts()
    updated_contacts = [c for c in contacts if c['name'].lower() != name.lower()]

    if len(updated_contacts) == len(contacts):
        print("Contact not found.\n")
    else:
        save_contacts(updated_contacts)
        print("Contact deleted successfully.\n")

def menu():
    while True:
        print("===== Contact Book =====")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")
        print()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    menu()
