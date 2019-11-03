from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey, Float
from forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///postgre.db'
db = SQLAlchemy(app)

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