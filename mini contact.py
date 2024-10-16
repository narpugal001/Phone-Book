import sys
import re

class Contact:
    def __init__(self, name, phone, email, category):
        self.name = name
        self.phone = phone
        self.email = email
        self.category = category

    def __repr__(self):
        return f"{self.name}, {self.phone}, {self.email or 'N/A'}, {self.category or 'N/A'}"

def phonebook():
    x = int(input("Enter the initial number of contacts: "))
    phone_book = []

    for i in range(x):
        print(f"\nEnter contact {i + 1} details:")
        name = input("Enter Name: ").strip()
        if not name:
            sys.exit("Name is a mandatory field. Process exiting due to blank field...")

        phone = input("Enter the Phone Number (at least 10 digits): ").strip()
        while not phone.isdigit() or len(phone) < 10:
            phone = input("Invalid number. Enter a valid Phone Number (at least 10 digits): ").strip()

        email = input("Enter Your Email ID (or press Enter to skip): ").strip() or None
        if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            email = None
            print("Invalid email format. It will be set to None.")

        category = input("Enter category (Family/Friends/Work/Others or press Enter to skip): ").strip() or None

        contact = Contact(name, phone, email, category)
        phone_book.append(contact)

    return phone_book

def menu():
    print("\n<><><><><><><><><><><<><><><<><><<><><><><><><><<><><><><")
    print("\t\t\t DIRECTORY ")
    print("<><><><><><><><><><><<><><><<><><<><><><><><><><<><><><><")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit Phonebook")
    
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in range(1, 7):
                return choice
            else:
                print("Please enter a valid choice between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_contact(pb):
    name = input("Enter Name: ").strip()
    if not name:
        print("Name is mandatory.")
        return pb

    phone = input("Enter the Phone Number (at least 10 digits): ").strip()
    while not phone.isdigit() or len(phone) < 10:
        phone = input("Invalid number. Enter a valid Phone Number (at least 10 digits): ").strip()

    email = input("Enter Your Email ID (or press Enter to skip): ").strip() or None
    if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        email = None
        print("Invalid email format. It will be set to None.")

    category = input("Enter category (Family/Friends/Work/Others or press Enter to skip): ").strip() or None

    contact = Contact(name, phone, email, category)
    pb.append(contact)
    print(f"Contact {name} has been added.")
    return pb 

def remove_contact(pb):
    name = input("Please enter the name of the contact you wish to remove: ").strip()
    for i, contact in enumerate(pb):
        if name.lower() == contact.name.lower():
            pb.pop(i)
            print(f"{contact.name} has been removed.")
            return pb
    print("Sorry, no contact found with that name.")
    return pb

def delete_all(pb):
    pb.clear()
    print("All contacts have been deleted.")
    return pb

def search_existing(pb):
    choice = int(input("Enter search criteria:\n1. Name\n2. Number\n3. Email\n4. Category\nPlease enter: "))
    search_term = input("Please enter your search term: ").strip()
    results = []

    for contact in pb:
        if (choice == 1 and search_term.lower() in contact.name.lower()) or \
           (choice == 2 and search_term in contact.phone) or \
           (choice == 3 and (contact.email and search_term in contact.email)) or \
           (choice == 4 and (contact.category and search_term.lower() in contact.category.lower())):
            results.append(contact)

    if results:
        print("Search Results:")
        for contact in results:
            print(contact)
    else:
        print("No contacts found matching your criteria.")

def display_all(pb):
    if not pb:
        print("The phone book is empty.")
    else:
        print("All Contacts:")
        for contact in pb:
            print(contact)

def greetings():
    print("*******************************************************")
    print("Thank You")
    print("*******************************************************")
    sys.exit("Good Bye!!!")

print("Welcome to our phone book!")
pb = phonebook()

while True:
    ch = menu()
    if ch == 1:
        pb = add_contact(pb)
    elif ch == 2:
        pb = remove_contact(pb)
    elif ch == 3:
        pb = delete_all(pb)
    elif ch == 4:
        search_existing(pb)
    elif ch == 5:
        display_all(pb)
    elif ch == 6:
        greetings()


