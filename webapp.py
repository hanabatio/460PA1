from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey, Float
from forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Junior7898@localhost/postgres'
db = SQLAlchemy(app)

#Class sysmtem for the DB; idk if we need it or not 
'''
class Business(db.Model):
    __tablename__ = 'Business'
    business_id = db.Column('business_id', db.String(30), primary_key=True)
    active = db.Column('active', db.Boolean, nullable = False)
    categories = db.Column('categories', db.String(200))
    review_count = db.Column('review_count', db.Integer, nullable = False)
    business_name = db.Column('business_name', db.String(200), nullable = False)
    stars = db.Column('stars', db.Float, nullable=False)

    def __init__(self, business_id, active, categories, review_count, business_name, stars):
        self.business_id = business_id
        self.active = active
        self.categories = categories
        self.review_count = review_count
        self.business_name = business_name
        self.stars = stars

    def __repr__(self):
        return f"Business('{self.business_id}', '{self.business_name}', '{self.categories}', '{self.review_count}', '{self.stars}')"

class Checkins(db.Model):
    __tablename__ = 'Checkins'
    business_id = db.Column('business_id', db.String(30), db.ForeignKey('business_id'), nullable=False)
    Sunday = db.Column('Sunday', db.Integer, nullable = False)
    Monday = db.Column('Monday', db.Integer, nullable = False)
    Tuesday = db.Column('Tuesday', db.Integer, nullable = False)
    Wednesday = db.Column('Wednesday', db.Integer, nullable = False)
    Thursday = db.Column('Thursday', db.Integer, nullable = False)
    Friday = db.Column('Friday', db.Integer, nullable = False)
    Saturday = db.Column('Saturday', db.Integer, nullable = False)

    def __repr__(self):
        return f"Checkins('{self.business_id}', '{self.Sunday}', '{self.Monday}', '{self.Tueday}', '{self.Wednesday}', '{self.Thursday}', '{self.Friday}', '{self.Saturday}')"

class Reviews(db.Model):
    __tablename__ = 'Reviews'
    review_id = db.Column('review_id', db.String(30), primary_key=True)
    business_id = db.Column('business_id', db.String(30), db.ForeignKey('business_id'), nullable=False)
    user_id = db.Column('user_id', db.String(30), db.ForeignKey('user_id'), nullable=False)
    stars = db.Column('stars', db.Float, nullable=False)
    review_text = db.Column('review_text', db.Text)

    def __repr__(self):
        return f"Reviews('{self.review_id}', '{self.review_id}', '{self.user_id}')"

class Users(db.model):
    __tablename__ = 'Users'
    user_id = db.Column('user_id', db.String(30), primary_key=True)
    name = db.Column('name', db.String(30), nullable = False)
    review_count = db.Column('review_count', db.Integer, nullable=False)

    review = db.relationship('Reviews', backref='user',lazy=True)

    def __repr__(self):
        return f"Users('{self.user_id}', '{self.name}', '{self.review_count}')"
'''


session = sessionmaker(bind=db)()

Base = automap_base()
Base.prepare(db.engine, reflect = True)


session = sessionmaker()
session.configure(bind=db.engine)
s = session()


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/business', methods= ['GET', 'POST'])
def business():
    form = newBusinessForm(request.form)
    if form.validate_on_submit():
        flash(f'Business Inserted!','success')
        return redirect(url_for('home'))
    return render_template('business.html', form=form)

@app.route('/user', methods= ['GET', 'POST'])
def user():
    form = newUserForm(request.form)
    if form.validate_on_submit():
        flash(f'User Inserted!','success')
        return redirect(url_for('home'))
    return render_template('user.html', form=form)

@app.route('/checkins', methods= ['GET', 'POST'])
def checkins():
    form = newCheckInForm(request.form)
    if form.validate_on_submit():
        flash(f'CheckIn Inserted!','success')
        return redirect(url_for('home'))
    return render_template('checkins.html', form=form)

@app.route('/reviews', methods= ['GET', 'POST'])
def reviews():
    form = newReviewForm(request.form)
    if form.validate_on_submit():
        flash(f'Review Inserted!','success')
        return redirect(url_for('home'))
    return render_template('reviews.html', form=form)

#ten queries
@app.route('/q1')
def querie1():
    #cur = db.connection.cursor()
    #cur.execute('''SELECT * FROM (mysql.Users) WHERE (review_count>=1)''')
    #rv = cur.fetchall()
    #return str(rv)
    return "HI"
    
@app.route('/q2')
def querie2():
    return "Hi"

@app.route('/q3')
def querie3():
    return "Hi"

@app.route('/q4')
def querie4():
    return "Hi"

@app.route('/q5')
def querie5():
    return "Hi"

@app.route('/q6')
def querie6():
    return "Hi"

@app.route('/q7')
def querie7():
    return "Hi"

@app.route('/q8')
def querie8():
    return "Hi"

@app.route('/q9')
def querie9():
    return "Hi"

@app.route('/q10')
def querie10():
    return "Hi"


if __name__ == '__main__':
    app.run(debug=True)