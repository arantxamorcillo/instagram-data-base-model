import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table, DateTime
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
    name = Column(String(250), nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(100), nullable= False)
    user_name = Column(String(100), unique = True, nullable=False)
    coments = relationship(
        "coment", backref="users")
    posts = relationship("post", backref="user")
    followers = relationship("follower", backref="follower")

class Coment(Base):
    __tablename__ = 'coment'
    # Here we define columns for the table Characters.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    body = Column( String(300))
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))


    

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table Characters.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    title = Column (String(200), nullable=False)
    location = Column (String, nullable=True)
    date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    coments = relationship(
        "coment", backref="post")

class Follower(Base):
    __tablename__="follower"
    id= Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e