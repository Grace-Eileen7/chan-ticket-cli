#am importing functions from helpers.py to use in cli.py
#something like menu loop that allows user to choose options
#the point is that each menu option should call a helper function. Making sure the loop keeps running untill user chooses to exit. just like in canvas 'Building pyrhon CLI'
from helpers import (
    create_match, list_matches, delete_match,
    create_user, list_users, delete_user,
    create_ticket, list_tickets, delete_ticket
)

def menu():
    print("Please select an option:")
    print("0. Exit")
    print("1. Create a match")
    print("2. List all matches")
    print("3. Delete a match")
    print("4. Create a user")
    print("5. List all users")
    print("6. Delete a user")
    print("7. Create a ticket")
    print("8. List all tickets")
    print("9. Delete a ticket")
    # Add more as needed

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            create_match()
        elif choice == "2":
            list_matches()
        # Continue for all options...
        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()
