from base import Base, engine
from main import SessionLocal, User

Base.metadata.create_all(bind=engine)

db = SessionLocal()

users = [
    User(login="pavel", email="a@gmail.com"),
    User(login="yura", email="b@gmail.com")
]

db.add_all(users)
db.commit()
db.close()
