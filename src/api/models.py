from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

Base = declarative_base()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(Integer, primary_key=True)
    username = db.Column(String(250), nullable=False)
    password = db.Column(String(250), nullable=False)
    person = db.relationship("Person")


class Planet(Base):
    __tablename__ = 'planet'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(250), nullable=False)
    climate = db.Column(String(250))
    terrain = db.Column(String(250))
    population = db.Column(Integer)
    favorites = db.relationship("Favorite")

class Character(Base):
    __tablename__ = 'character'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(250), nullable=False)
    height = db.Column(Integer)
    hair_color = db.Column(String(250))
    eye_color = db.Column(String(250))
    gender = db.Column(String(250))
    favorites = db.relationship("Favorite")

class Starship(Base):
    __tablename__ = 'starship'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(250), nullable=False)
    model = db.Column(String(250))
    manufacturer = db.Column(String(250))
    crew = db.Column(Integer)
    passengers = db.Column(Integer)
    favorites = db.relationship("Favorite")
    # Add any additional fields as necessary

class Favorite(Base):
    __tablename__ = 'favorite'
    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(Integer, ForeignKey('user.id'))
    planet_id = db.Column(Integer, ForeignKey('planet.id'))
    character_id = db.Column(Integer, ForeignKey('character.id'))
    starship_id = db.Column(Integer, ForeignKey('starship.id'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')