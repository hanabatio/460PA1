# coding: utf-8
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from webapp import db, Base


class Busines(Base):
    __tablename__ = 'Business'

    business_id = Column(String(10000), primary_key=True)
    active = Column(Boolean)
    categories = Column(String(10000))
    review_count = Column(Integer)
    business_name = Column(String(10000))
    stars = Column(Float)


class User(Base):
    __tablename__ = 'Users'

    user_id = Column(String(10000), primary_key=True)
    name = Column(String(10000))
    review_count = Column(Integer)


class Checkins(Base):
    __tablename__ = 'Checkins'

    business_id = Column(ForeignKey('Business.business_id'), primary_key=True)    
    sunday = Column(Integer)
    monday = Column(Integer)
    tuesday =Column(Integer)
    wednesday = Column(Integer)
    thursday = Column(Integer)
    friday = Column(Integer)
    saturday = Column(Integer)


class Review(Base):
    __tablename__ = 'Reviews'

    review_id = Column(String(10000), primary_key=True)
    business_id = Column(ForeignKey('Business.business_id'))
    user_id = Column(ForeignKey('Users.user_id'))
    stars = Column(Float)
    review_text = Column(String(100000))

    business = relationship('Busines')
