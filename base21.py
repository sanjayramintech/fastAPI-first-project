from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import declarative_base,sessionmaker

engine=create_engine("sqlite:///sample.db")

base1=declarative_base()

class sambu(base1):
    __tablename__="shupandi"
    id=Column(Integer, primary_key=True)
    name=Column(String)

base1.metadata.create_all(engine)
print("table created")

Session=sessionmaker(bind=engine)
session=Session()

p1=(sambu( name="sambhu"))
session.add(p1)
session.commit()

students = session.query(sambu).all()

for student in students:
    print(student.id, student.name)
