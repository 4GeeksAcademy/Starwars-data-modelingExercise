import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(100))
    email = Column(String(50))
    
class Planet(Base): 
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name =  Column(String(50))
    population = Column(Integer)

class Favorite_planet(Base): 
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key=True)
    id_planet = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Vehicle(Base): 
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    model = Column(String(100))

class Favorite_vehicle(Base):
    __tablename__ = 'favorite_vehicle'
    id = Column(Integer, primary_key=True)
    id_vehicle = Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship(Vehicle)
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Character(Base): 
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    height = Column(Integer)
    mass = Column(Integer)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

class Favorite_character(Base): 
    __tablename__ = 'favorite_character'
    id = Column(Integer, primary_key=True)
    id_character = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

  


## Draw from SQLAlchemy base
try: 
    result= render_er(Base, 'diagram.png')
    print("Success!")
except Exception as e: 
    print("hay un problema")
    raise e