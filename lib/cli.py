import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Farmer,Produce,Order,Consumer

# define the database connection 
DATABASE_URI = 'sqlite:///farmers.db' #path to the database

engine = create_engine(DATABASE_URI,echo=False)
 #creating the engine
Session = sessionmaker(bind=engine) #creating a session
session = Session()

@click.group()
def cli():
    """ Farmer Market Place"""

@cli.command()
def farmer_profile(): # creating a farmer profile 
    """Create a new farmer profile"""
    click.echo("Enter farmer details:")
    while True:
        name = click.prompt("Name",default='')
        if name:
            break  # Exiting  the loop if a non-empty name is provided
        else:
            click.echo("Name cannot be empty. Please provide a name.")
    while True:
        email = click.prompt("Enter email" ,default='')
        if email:
            break  # Exiting  the loop if a non-empty email is provided
        else:
            click.echo("Email cannot be empty. Please provide an email.")
    while True:
        phone_number = click.prompt("Enter phone Number")
        if phone_number:
            if phone_number.isdigit():  # making sure its a numeric string 
                break  # Exiting the loop if a valid phone number is provided
            else:
                click.echo("Phone Number must be a numeric value.")
        else:
            click.echo("Phone Number cannot be empty. Please provide a phone number.")
    while True:
        city = click.prompt("Enter City",default='')
        if city:
            break  # Exiting  the loop if a non-empty city is provided
        else:
            click.echo("City cannot be empty. Please provide a city.")
