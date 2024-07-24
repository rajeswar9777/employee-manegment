# reset_db.py

from app import db

def reset_database():
    db.drop_all()
    db.create_all()
    print("Database recreated successfully.")

if __name__ == '__main__':
    reset_database()
