class ContactBook:
    def __init__(self):
        """
        Initializes the ContactBook class with an empty contact list.
        """
        self.contacts = {}

    def add_contact(self, name: str, phone: str, email: str) -> None:
        """
        Adds a contact to the contact book.

        Args:
            name (str): The contact's name.
            phone (str): The contact's phone number.
            email (str): The contact's email address.
        """
        self.contacts[name] = {"phone": phone, "email": email}
        print(f"Contact '{name}' added to the contact book.")

    def view_contact(self, name: str) -> None:
        """
        Displays the details of a contact.

        Args:
            name (str): The name of the contact to view.
        """
        contact = self.contacts.get(name)
        if contact:
            print(f"Name: {name}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
        else:
            print(f"No contact found with the name '{name}'.")

    def delete_contact(self, name: str) -> None:
        """
        Deletes a contact from the contact book.

        Args:
            name (str): The name of the contact to delete.
        """
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted from the contact book.")
        else:
            print(f"No contact found with the name '{name}'.")

    def view_all_contacts(self) -> None:
        """
        Displays all contacts in the contact book.
        """
        if not self.contacts:
            print("No contacts in the contact book.")
        else:
            for name, details in self.contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {details['phone']}")
                print(f"Email: {details['email']}")
                print("")


if __name__ == "__main__":
    contact_book = ContactBook()
    while True:
        print("\nOptions:")
        print("1. Add contact")
        print("2. View contact")
        print("3. Delete contact")
        print("4. View all contacts")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            name = input("Enter contact name: ").strip()
            phone = input("Enter contact phone number: ").strip()
            email = input("Enter contact email address: ").strip()
            contact_book.add_contact(name, phone, email)
        elif choice == "2":
            name = input("Enter contact name to view: ").strip()
            contact_book.view_contact(name)
        elif choice == "3":
            name = input("Enter contact name to delete: ").strip()
            contact_book.delete_contact(name)
        elif choice == "4":
            contact_book.view_all_contacts()
        elif choice == "5":
            print("Exiting Contact Book application.")
            break
        else:
            print("Invalid option. Please choose a valid option.")
