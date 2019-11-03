from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Junior7898@localhost/postgres'
db = SQLAlchemy(app)


from webapp import routes

session = sessionmaker(bind=db)()

Base = automap_base()
Base.prepare(db.engine, reflect = True)

session = sessionmaker()
session.configure(bind=db.engine)
s = session()