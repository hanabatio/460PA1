# coding: utf-8
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


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


t_Checkins = Table(
    'Checkins', metadata,
    Column('business_id', ForeignKey('Business.business_id')),
    Column('Sunday', Integer),
    Column('Monday', Integer),
    Column('Tuesday', Integer),
    Column('Wednesday', Integer),
    Column('Thursday', Integer),
    Column('Friday', Integer),
    Column('Saturday', Integer)
)


class Review(Base):
    __tablename__ = 'Reviews'

    review_id = Column(String(10000), primary_key=True)
    business_id = Column(ForeignKey('Business.business_id'))
    user_id = Column(String(10000))
    stars = Column(Float)
    review_text = Column(String(100000))

    business = relationship('Busines')
