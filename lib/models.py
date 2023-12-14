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