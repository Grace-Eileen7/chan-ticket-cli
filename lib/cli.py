from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.helpers import (
    create_match, get_all_matches, delete_match,
    create_user, get_all_users, delete_user,
    create_ticket, get_all_tickets, delete_ticket
)
from lib.db.models import Match, Ticket, User

# Setup DB session
engine = create_engine("sqlite:///lib/db/app.db")
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()


def welcome():
    print("\n 🇰🇪 Welcome to CHAN Ticket CLI 🇰🇪 ")
    print("---------------------------------")


def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. User Menu")
        print("2. Admin Menu")
        print("0. Exit")

        choice = input("> ").strip()
        if choice == "1":
            user_menu()
        elif choice == "2":
            admin_menu()
        elif choice == "0":
            print("Goodbye!!")
            break
        else:
            print(" Invalid option, try again.")


# ---------------- USER MENU ----------------
def user_menu():
    while True:
        print("\n--- User Menu ---")
        print("1. View Matches")
        print("2. Buy Ticket")
        print("3. View My Tickets")
        print("0. Back to Main Menu")

        choice = input("> ").strip()

        if choice == "1":
            view_matches()
        elif choice == "2":
            buy_ticket()
        elif choice == "3":
            view_my_tickets()
        elif choice == "0":
            break
        else:
            print(" Invalid option.")


def view_matches():
    matches = get_all_matches(session)
    if not matches:
        print(" No matches found.")
        return
    print("\n Upcoming Matches:")
    for m in matches:
        print(f"{m.id}. {m.home_team} vs {m.away_team} on {m.date} at {m.venue}")


def buy_ticket():
    view_matches()
    try:
        match_id = int(input("Enter Match ID: ").strip())
        user_id = int(input("Enter your User ID: ").strip())
    except ValueError:
        print(" Invalid input. IDs must be numbers.")
        return

    seat = input("Choose Seat Number: ").strip()

    ticket = create_ticket(session, seat, match_id, user_id)
    if ticket:
        print(f" Ticket booked: Seat {seat} for Match {ticket.match.home_team} vs {ticket.match.away_team}")
    else:
        print(" ! Seat already booked, please try another.")


def view_my_tickets():
    try:
        user_id = int(input("Enter your User ID: ").strip())
    except ValueError:
        print(" Invalid input. ID must be a number.")
        return

    tickets = session.query(Ticket).filter_by(user_id=user_id).all()
    if not tickets:
        print(" You have no tickets.")
        return
    print("\n Your Tickets:")
    for t in tickets:
        match = session.get(Match, t.match_id)
        print(f"- Seat {t.seat_number}: {match.home_team} vs {match.away_team} on {match.date}")


# ---------------- ADMIN MENU ----------------
def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Create a Match")
        print("2. List Matches")
        print("3. Delete a Match")
        print("4. Create a User")
        print("5. List Users")
        print("6. Delete a User")
        print("7. List Tickets")
        print("8. Delete a Ticket")
        print("0. Back to Main Menu")

        choice = input("> ").strip()

        if choice == "1":
            home = input("Home team: ").strip()
            away = input("Away team: ").strip()
            date = input("Match date: ").strip()
            venue = input("Venue: ").strip()
            match = create_match(session, home, away, date, venue)
            print(f" Match {match.home_team} vs {match.away_team} created.")
        elif choice == "2":
            view_matches()
        elif choice == "3":
            view_matches()
            try:
                match_id = int(input("Enter Match ID to delete: ").strip())
                delete_match(session, match_id)
                print(" Match deleted (if existed).")
            except ValueError:
                print(" Invalid ID.")
        elif choice == "4":
            name = input("User name: ").strip()
            email = input("User email: ").strip()
            user = create_user(session, name, email)
            print(f" User {user.name} created.")
        elif choice == "5":
            users = get_all_users(session)
            if not users:
                print(" No users found.")
            for u in users:
                print(f"{u.id}. {u.name} ({u.email})")
        elif choice == "6":
            try:
                user_id = int(input("Enter User ID to delete: ").strip())
                delete_user(session, user_id)
                print(" User deleted (if existed).")
            except ValueError:
                print(" Invalid ID.")
        elif choice == "7":
            tickets = get_all_tickets(session)
            if not tickets:
                print(" No tickets found.")
            for t in tickets:
                match = session.get(Match, t.match_id)
                user = session.get(User, t.user_id)
                print(f"Ticket {t.id}: Seat {t.seat_number} | {match.home_team} vs {match.away_team} | Buyer: {user.name}")
        elif choice == "8":
            try:
                ticket_id = int(input("Enter Ticket ID to delete: ").strip())
                delete_ticket(session, ticket_id)
                print(" Ticket deleted (if existed).")
            except ValueError:
                print(" Invalid ID.")
        elif choice == "0":
            break
        else:
            print(" Invalid option.")


if __name__ == "__main__":
    welcome()
    main_menu()
