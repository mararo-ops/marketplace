#populating the database
from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Consumer,Farmer,Produce,Order

fake=Faker()

if __name__=='__main__':
    engine= create_engine('sqlite:///farmers.db')
    Session = sessionmaker(bind=engine) #creating a session
    session = Session()
    session.query(Consumer).delete() #to delete the previous records to avoid duplication
    session.query(Farmer).delete()
    session.query(Produce).delete()
    session.query(Order).delete()


print("Seeding Farmers")