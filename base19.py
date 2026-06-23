from sqlalchemy import create_engine

engine = create_engine("sqlite:///students.db")

print("Database created!")