from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Match(Base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True)
    home_team = Column(String)
    away_team = Column(String)
    date = Column(String)
    venue = Column(String)
    tickets = relationship("Ticket", back_populates="match")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    tickets = relationship("Ticket", back_populates="user")

class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True)
    seat_number = Column(String, unique=True)   # ensures "no double booking"
    match_id = Column(Integer, ForeignKey("matches.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    match = relationship("Match", back_populates="tickets")
    user = relationship("User", back_populates="tickets")
