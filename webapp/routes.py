from flask import render_template, flash, redirect, url_for, request
from webapp import app, db
from sqlalchemy import update
from webapp.forms import *
from webapp.models import *

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/business', methods= ['GET', 'POST'])
def business():
    form = newBusinessForm(request.form)
    if form.validate_on_submit():
       
        business = Busines(business_id=form.business_id.data, active= form.active.data, categories= form.categories.data,
        business_name= form.business_name.data, review_count= form.review_count.data, stars= form.stars.data)
        db.session.add(business)
        db.session.commit()

        flash(f'Business Inserted!','success')
        return redirect(url_for('home'))
    return render_template('business.html', form=form)

@app.route('/user', methods= ['GET', 'POST'])
def user():
    form = newUserForm(request.form)
    if form.validate_on_submit():

        user = User(user_id=form.userid.data, name= form.name.data, review_count= form.review_count.data)
        db.session.add(user)
        db.session.commit()

        flash(f'User Inserted!','success')
        return redirect(url_for('home'))
    return render_template('user.html', form=form)

@app.route('/checkins', methods= ['GET', 'POST'])
def checkins():
    form = newCheckInForm(request.form)
    if form.validate_on_submit():
        business=Checkins.query.filter_by(business_id=form.business_id.data)
        days=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        if form.day_of_week.data not in days:
            flash(f'Invalid Day','failure')
        else:
            if form.day_of_week.data == "Sunday":
                if business:
                    business.sunday+=1
                else:
                    checkin = Checkins(business_id=form.business_id.data, sunday=1, monday=0, tuesday=0, wednesday=0, thursday=0, friday=0,
                    saturday=0)
            elif form.day_of_week.data == "Monday":
                if business:
                    business.monday+=1
                else:
                    checkin = Checkins(business_id=form.business_id.data, sunday=0, monday=1, tuesday=0, wednesday=0, thursday=0, friday=0,
                    saturday=0)
            elif form.day_of_week.data == "Tuesday":
                if business:
                    business.tuesday+=1
                else:
                    checkin = Checkins(business_id=form.business_id.data, sunday=0, monday=0, tuesday=1, wednesday=0, thursday=0, friday=0,
                    saturday=0)
            elif form.day_of_week.data == "Wednesday":
                if business:
                    business.wednesday+=1
                else:
                    checkin = Checkins(business_id=form.business_id.data, sunday=0, monday=0, tuesday=0, wednesday=1, thursday=0, friday=0,
                    saturday=0)
            elif form.day_of_week.data == "Thursday":
                if business:
                    business.thursday+=1
                else:
                    checkin = Checkins(business_id=form.business_id.data, sunday=0, monday=0, tuesday=0, wednesday=0, thursday=1, friday=0,
                    saturday=0)
            elif form.day_of_week.data == "Friday":
                if business:
                    business.friday+=1
                else:
                    checkin = Checkins(business_id=form.business_id.data, sunday=0, monday=0, tuesday=0, wednesday=0, thursday=0, friday=1,
                    saturday=0)
            else:
                if business:
                    business.saturday+=1
                else:
                    checkin = Checkins(business_id=form.business_id.data, sunday=0, monday=0, tuesday=0, wednesday=0, thursday=0, friday=0,
                    saturday=1)

            if not business:
                db.session.add(checkin)
            db.session.commit()

        flash(f'CheckIn Inserted!','success')
        return redirect(url_for('home'))
    return render_template('checkins.html', form=form)

@app.route('/reviews', methods= ['GET', 'POST'])
def reviews():
    form = newReviewForm(request.form)
    if form.validate_on_submit():

        review = Review(review_id= form.review_id.data, business_id=form.business_id.data, user_id=form.userid.data,
        stars= form.stars.data, review_text= form.review_text.data)
        db.session.add(business)
        db.session.commit()

        flash(f'Review Inserted!','success')
        return redirect(url_for('home'))
    return render_template('reviews.html', form=form)

#ten queries
@app.route('/q1', methods=['GET','POST'])
def query1():
    table1 = []
    if request.method == 'POST':
        return render_template('q1.html')
    else:
        table1 = makeTable1()
        print (table1)
        return render_template('q1.html', table1=table1)

def makeTable1():
    c = db.engine.connect()
    rows = c.execute('SELECT * FROM postgres.public."Users" WHERE (review_count >=1)')
    return rows
    
@app.route('/q2')
def query2():
    table2 = []
    if request.method == 'POST':
        return render_template('q2.html')
    else:
        table2 = makeTable2()
        print (table2)
        return render_template('q2.html', table2=table2)

def makeTable2():
    c = db.engine.connect()
    rows = c.execute('SELECT "Users"."name" FROM postgres.public."Users" WHERE (review_count <= 2);')
    return rows

@app.route('/q3')
def query3():
    table3 = []
    if request.method == 'POST':
        return render_template('q3.html')
    else:
        table3 = makeTable3()
        print (table3)
        return render_template('q3.html', table3=table3)

def makeTable3():
    c = db.engine.connect()
    rows = c.execute('SELECT * FROM postgres.public."Business" WHERE (active=false);')   
    return rows

@app.route('/q4')
def query4():
    table4 = []
    if request.method == 'POST':
        return render_template('q4.html')
    else:
        table4 = makeTable4()
        print (table4)
        return render_template('q4.html', table4=table4)

def makeTable4():
    c = db.engine.connect()
    rows = c.execute('SELECT "Business".business_name FROM postgres.public."Business" WHERE stars >=4 and categories LIKE '%Pizza%';')   
    return rows

@app.route('/q5')
def query5():
    table5 = []
    if request.method == 'POST':
        return render_template('q5.html')
    else:
        table5 = makeTable5()
        print (table5)
        return render_template('q5.html', table5=table5)

def makeTable5():
    c = db.engine.connect()
    rows = c.execute('SELECT COUNT(*) FROM postgres.public."Checkins" WHERE "Friday" >=1;')    
    return rows

@app.route('/q6')
def query6():
    table6 = []
    if request.method == 'POST':
        return render_template('q6.html')
    else:
        table6 = makeTable6()
        print (table6)
        return render_template('q6.html', table6=table6)

def makeTable6():
    c = db.engine.connect()
    rows = "Hi"#c.execute('SELECT "Reviews".review_text FROM postgres.public."Reviews" WHERE business_id = (SELECT "Business".business_id FROM postgres.public."Business" WHERE "business_name" = 'Arcadia Tavern');')   
    return rows

@app.route('/q7')
def query7():
    table7 = []
    if request.method == 'POST':
        return render_template('q7.html')
    else:
        table7 = makeTable7()
        print (table7)
        return render_template('q7.html', table7=table7)

def makeTable7():
    c = db.engine.connect()
    rows = c.execute('SELECT "Business".business_name FROM postgres.public."Business", postgres.public."Reviews" WHERE "Business".business_id = "Reviews".business_id AND ("Reviews".stars = 1 OR "Reviews".stars = 2);')   
    return rows

@app.route('/q8')
def query8():
    table8 = []
    if request.method == 'POST':
        return render_template('q8.html')
    else:
        table8 = makeTable8()
        print (table8)
        return render_template('q8.html', table8=table8)

def makeTable8():
    c = db.engine.connect()
    rows = "Hi"#c.execute('SELECT AVG("Business".stars) AS "Average Rating of KFC Stores", SUM("Business".review_count) AS "Total Number of Reviews for All KFC Stores" FROM postgres.public."Business" WHERE business_name LIKE '%Kfc%';')  
    return rows


@app.route('/q9')
def query9():
    table9 = []
    if request.method == 'POST':
        return render_template('q9.html')
    else:
        table9 = makeTable9()
        print (table9)
        return render_template('q9.html', table9=table9)

def makeTable9():
    c = db.engine.connect()
    rows = c.execute('SELECT "Business".business_id AS "Business IDs of the Top 10 Most Reviewed Stores" FROM postgres.public."Business" ORDER BY "Business".review_count DESC LIMIT 10;')
    return rows

@app.route('/q10')
def query10():
    table10 = []
    if request.method == 'POST':
        return render_template('q10.html')
    else:
        table10 = makeTable10()
        print (table10)
        return render_template('q10.html', table10=table10)

def makeTable10():
    c = db.engine.connect()
    rows = c.execute('SELECT "Users"."name" as "User with Most Reviews" FROM postgres.public."Users" ORDER BY "Users".review_count DESC LIMIT 1') 
    return rows


if __name__ == '__main__':
    app.run(debug=True)

