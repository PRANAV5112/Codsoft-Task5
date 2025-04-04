import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from a JSON file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    """Save contacts to a JSON file."""
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    """Add a new contact."""
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    contacts = load_contacts()
    
    if name in contacts:
        print("Contact already exists!")
        return
    
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts():
    """Display all contacts."""
    contacts = load_contacts()
    if not contacts:
        print("\nNo contacts found.")
        return
    
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"{name} - {details['Phone']}")

def search_contact():
    """Search for a contact by name or phone number."""
    contacts = load_contacts()
    query = input("Enter Name or Phone Number to search: ").strip()

    for name, details in contacts.items():
        if query.lower() in name.lower() or query == details["Phone"]:
            print(f"\nFound Contact:\nName: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}")
            return
    
    print("Contact not found.")

def update_contact():
    """Update contact details."""
    contacts = load_contacts()
    name = input("Enter the Name of the contact to update: ").strip()
    
    if name not in contacts:
        print("Contact not found!")
        return
    
    print("\nEnter new details (leave blank to keep current info):")
    phone = input(f"New Phone ({contacts[name]['Phone']}): ").strip() or contacts[name]['Phone']
    email = input(f"New Email ({contacts[name]['Email']}): ").strip() or contacts[name]['Email']
    address = input(f"New Address ({contacts[name]['Address']}): ").strip() or contacts[name]['Address']

    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    save_contacts(contacts)
    print("Contact updated successfully!")

def delete_contact():
    """Delete a contact."""
    contacts = load_contacts()
    name = input("Enter the Name of the contact to delete: ").strip()

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

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
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
