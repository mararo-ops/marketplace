from sqlalchemy import Column, Integer, String, ForeignKey,create_engine
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# define the database connection 
DATABASE_URI = 'sqlite:///farmers.db' #path to the database

engine = create_engine(DATABASE_URI,echo=False)
 #creating the engine

Session = sessionmaker(bind=engine) #creating a session
session = Session()

#base class for allthe classes
Base =declarative_base()

#creating the tables
class Farmer(Base):
    __tablename__='farmers'
    id=Column(Integer, primary_key=True)
    name=Column(String,nullable=False)
    email = Column(String(255), nullable=True)
    phone_number = Column(String(20), nullable=True)
    city = Column(String(100), nullable=True)

    #relationships 
    produce =relationship('Produce',back_populates='farmer') #one to many relationship between farmer and produce
    orders = relationship('Order',back_populates='farmer') #a farmer can have many orders


# produce table
class Produce(Base):
    __tablename__='produce'
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    farmer_id =Column(Integer,ForeignKey('farmers.id'))
    price=Column(Integer,nullable=False)
    review = Column(Integer, nullable=True)

    #relationships
    farmer = relationship('Farmer',back_populates='produce') # one farmer can produce many produce many-one
    orders= relationship('Order',back_populates='produce') # one produce can have many orders 1-many
