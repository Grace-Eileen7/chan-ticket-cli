from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, User, Match, Ticket

engine = create_engine("sqlite:///lib/db/app.db")
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

def seed():
    # reset DB
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # sample users
    user1 = User(name="Jane", email="jane@example.com")
    user2 = User(name="Doe", email="doe@example.com")

    # sample matches
    match1 = Match(home_team="Kenya", away_team="Uganda", date="2025-08-30", venue="Nairobi Kasarani Stadium")
    match2 = Match(home_team="Tanzania", away_team="Morocco", date="2025-09-02", venue="Dar es Salaam B.Mkapa Stadium")
    match3 = Match(home_team="Uganda", away_team="Senegal", date="2025-09-05", venue="Kampala Mandela National Stadium")

    session.add_all([user1, user2, match1, match2, match3])
    session.commit()

    # sample tickets
    ticket1 = Ticket(user_id=user1.id, match_id=match1.id, seat_number="A1")
    ticket2 = Ticket(user_id=user2.id, match_id=match2.id, seat_number="B5")

    session.add_all([ticket1, ticket2])
    session.commit()

    print("✅ Database seeded!")

if __name__ == "__main__":
    seed()
