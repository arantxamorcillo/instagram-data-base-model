import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    password = Column(String(50), nullable=False, )

class Character(Base):
    __tablename__ = 'Character'
    # Here we define columns for the table Characters.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    hair_colour = Column(String(250))
    eye_colour = Column(String(250))
    planet_id = Column(Integer, ForeignKey('Planet.id'))

class Planet(Base):
    __tablename__ = 'Planet'
    # Here we define columns for the table Characters.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(Integer)
    density = Column(Integer)


class Favorites(Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table Characters.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('Planet.id'))
    character_id = Column(Integer, ForeignKey('Character.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e