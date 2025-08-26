from models import Base, User, Match, Ticket
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///app.db")
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

# Add sample users
user1 = User(name="Alice", email="alice@example.com")
user2 = User(name="Bob", email="bob@example.com")
session.add_all([user1, user2])
session.commit()

# Add sample matches
match1 = Match(name="CHAN: Kenya vs Uganda", date="2025-08-30")
session.add(match1)
session.commit()

# Add sample tickets
ticket1 = Ticket(user_id=user1.id, match_id=match1.id, seat="A1")
session.add(ticket1)
session.commit()

print("Seeding complete!")
