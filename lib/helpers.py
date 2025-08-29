from lib.db.models import Match, Ticket, User

# ---------------- MATCH ----------------
def create_match(session, home_team, away_team, date, venue):
    match = Match(home_team=home_team, away_team=away_team, date=date, venue=venue)
    session.add(match)
    session.commit()
    return match

def get_all_matches(session):
    return session.query(Match).all()

def find_match_by_id(session, match_id):
    return session.query(Match).filter(Match.id == match_id).first()

def delete_match(session, match_id):
    match = find_match_by_id(session, match_id)
    if match:
        session.delete(match)
        session.commit()

def update_match(session, match_id, home_team=None, away_team=None, date=None, venue=None):
    match = find_match_by_id(session, match_id)
    if not match:
        print(" Match not found.")
        return None

    if home_team:
        match.home_team = home_team
    if away_team:
        match.away_team = away_team
    if date:
        match.date = date
    if venue:
        match.venue = venue

    session.commit()
    return match


# ---------------- USER ----------------
def create_user(session, name, email):
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    return user

def get_all_users(session):
    return session.query(User).all()

def find_user_by_id(session, user_id):
    return session.query(User).filter(User.id == user_id).first()

def delete_user(session, user_id):
    user = find_user_by_id(session, user_id)
    if user:
        session.delete(user)
        session.commit()

# ---------------- TICKET ----------------
def create_ticket(session, seat_number, match_id, user_id):
    # prevent double booking for same match
    existing_ticket = session.query(Ticket).filter_by(
        seat_number=seat_number, match_id=match_id
    ).first()
    if existing_ticket:
        return None
    ticket = Ticket(seat_number=seat_number, match_id=match_id, user_id=user_id)
    session.add(ticket)
    session.commit()
    return ticket

def get_all_tickets(session):
    return session.query(Ticket).all()

def find_ticket_by_id(session, ticket_id):
    return session.query(Ticket).filter(Ticket.id == ticket_id).first()

def delete_ticket(session, ticket_id):
    ticket = find_ticket_by_id(session, ticket_id)
    if ticket:
        session.delete(ticket)
        session.commit()
