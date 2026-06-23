from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

# Connect to database
engine = create_engine("sqlite:///students.db")

# Base class
Base = declarative_base()

# Table class
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create the table
Base.metadata.create_all(engine)

print("Table created!")