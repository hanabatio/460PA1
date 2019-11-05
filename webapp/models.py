# coding: utf-8
from flask import request
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import relationship
from webapp import db


Base = automap_base()
Base.load(request.json, session=db.session)


class Busines(Base):
    __tablename__ = 'Business'
    __table_args__ = {'extend_existing': True}
    #Busines.load(request.json, session=db.session)

    business_id = Column(String(10000), primary_key=True)
    active = Column(Boolean)
    categories = Column(String(10000))
    review_count = Column(Integer)
    business_name = Column(String(10000))
    stars = Column(Float)


class User(Base):
    __tablename__ = 'Users'
    __table_args__ = {'extend_existing': True}
    #User.load(request.json, session=db.session)

    user_id = Column(String(10000), primary_key=True)
    name = Column(String(10000))
    review_count = Column(Integer)


class Checkins(Base):
    __tablename__ = 'Checkins'
    __table_args__ = {'extend_existing': True}
    #Checkins.load(request.json, session=db.session)

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
    __table_args__ = {'extend_existing': True}
    #Review.load(request.json, session=db.session)

    review_id = Column(String(10000), primary_key=True)
    business_id = Column(ForeignKey('Business.business_id'))
    user_id = Column(ForeignKey('Users.user_id'))
    stars = Column(Float)
    review_text = Column(String(100000))

    business = relationship('Busines')

Base.prepare(db.engine, reflect = True)