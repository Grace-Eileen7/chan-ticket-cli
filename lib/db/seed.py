from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, User, Match, Ticket
from faker import Faker

# Initialize Faker (Kenyan locale optional)
fake = Faker()

engine = create_engine("sqlite:///lib/db/app.db")
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

def seed():
    # Reset DB
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # Realistic CHAN teams
    chan_teams = [
        "Kenya Harambee Stars", "Uganda Cranes", "Tanzania Taifa Stars",
        "Senegal Lions", "Morocco Atlas Lions", "Mali Eagles",
        "Ghana Black Stars", "Zambia Chipolopolo", "Nigeria Super Eagles",
        "Algeria Desert Warriors", "Cameroon Indomitable Lions", "Egypt Pharaohs"
    ]

    # Kenyan stadiums
    kenyan_stadiums = [
        "Kasarani Stadium, Nairobi", "Nyayo National Stadium, Nairobi",
        "Moi International Sports Centre, Kasarani", "Bukhungu Stadium, Kakamega",
        "Kipchoge Keino Stadium, Eldoret", "Mbaraki Sports Club, Mombasa"
    ]

    # --- Create Users ---
    users = []
    for _ in range(10):
        user = User(
            name=fake.name(),
            email=fake.unique.email()
        )
        session.add(user)
        session.flush()  # generate .id before commit
        users.append(user)
    session.commit()  # commit all users

    # --- Create Matches ---
    matches = []
    for _ in range(6):
        home_team = fake.random_element(chan_teams)
        away_team = fake.random_element([team for team in chan_teams if team != home_team])
        match = Match(
            home_team=home_team,
            away_team=away_team,
            date=fake.date_this_year(),
            venue=fake.random_element(kenyan_stadiums)
        )
        session.add(match)
        session.flush()  # generate .id
        matches.append(match)
    session.commit()

    # --- Create Tickets ---
    tickets = []
    for match in matches:
        for _ in range(fake.random_int(min=5, max=10)):
            row = fake.random_letter().upper()
            number = fake.random_int(min=1, max=30)
            seat_number = f"{row}{number}"

            ticket = Ticket(
                user_id=fake.random_element(users).id,
                match_id=match.id,
                seat_number=seat_number
            )
            session.add(ticket)
            tickets.append(ticket)
    session.commit()

    # --- Print Summary ---
    print("✅ Database seeded with realistic data!")
    print(f"   Created: {len(users)} users")
    print(f"   Created: {len(matches)} matches")
    print(f"   Created: {len(tickets)} tickets")
    print("\nSample Match:", f"{matches[0].home_team} vs {matches[0].away_team}")
    print("Sample User:", users[0].name)
    print("Sample Ticket:", f"Seat {tickets[0].seat_number} for Match #{tickets[0].match_id}")

if __name__ == "__main__":
    seed()
