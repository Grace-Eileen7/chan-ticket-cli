from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Match(Base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True)
    home_team = Column(String, nullable=False)
    away_team = Column(String, nullable=False)
    date = Column(String, nullable=False)
    venue = Column(String, nullable=False)
    
    tickets = relationship("Ticket", back_populates="match", cascade="all, delete")

    def __repr__(self):
        return f"<Match {self.id}: {self.home_team} vs {self.away_team} @ {self.venue}>"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    tickets = relationship("Ticket", back_populates="user", cascade="all, delete")

    def __repr__(self):
        return f"<User {self.id}: {self.name} ({self.email})>"

class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True)
    seat_number = Column(String, nullable=False)
    match_id = Column(Integer, ForeignKey("matches.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    match = relationship("Match", back_populates="tickets")
    user = relationship("User", back_populates="tickets")

    # ensure no double-booking within the same match
    __table_args__ = (UniqueConstraint("seat_number", "match_id", name="_seat_match_uc"),)#tuples

    def __repr__(self):
        return f"<Ticket {self.id}: Seat {self.seat_number} | Match {self.match_id} | User {self.user_id}>"
