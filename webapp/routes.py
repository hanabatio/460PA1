from flask import render_template, flash, redirect, url_for, request
from webapp import app, db
from sqlalchemy import update
from webapp.forms import *
from webapp.models import *

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/business')
def business():
    return render_template('business.html')

@app.route('/business/insert', methods= ['GET', 'POST'])
def businessInsert():
    form = newBusinessForm(request.form)
    if form.validate_on_submit():
       
        business = Busines(business_id=form.business_id.data, active= form.active.data, categories= form.categories.data,
        business_name= form.business_name.data, review_count= form.review_count.data, stars= form.stars.data)
        db.session.add(business)
        db.session.commit()

        flash(f'Business Inserted!','success')
        return redirect(url_for('business'))
    return render_template('business-insert.html', form=form)

@app.route('/business/delete', methods= ['GET', 'POST'])
def businessDelete():
    form = deleteBusinessForm(request.form)
    if form.validate_on_submit():
        Busines.query.filter_by(business_id=form.business_id.data).delete()
        db.session.commit()

        flash(f'Businesss Deleted!','success')
        return redirect(url_for('business'))
    return render_template('business-delete.html', form=form)

@app.route('/business/update', methods= ['GET', 'POST'])
def businessUpdate():
    form = updateBusinessForm(request.form)
    if form.validate_on_submit():
        business = Busines.query.filter_by(business_id=form.business_id.data)
        business.name=form.business_name.data
        business.review_count=form.review_count.data
        business.active=form.active.data
        business.stars=form.stars.data
        business.categories=form.categories.data
        db.session.commit()

        flash(f'Business Updated!','success')
        return redirect(url_for('business'))
    return render_template('business-update.html', form=form)


@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/user/insert', methods= ['GET', 'POST'])
def userInsert():
    form = newUserForm(request.form)
    if form.validate_on_submit():

        user = User(user_id=form.userid.data, name= form.name.data, review_count= form.review_count.data)
        db.session.add(user)
        db.session.commit()

        flash(f'User Inserted!','success')
        return redirect(url_for('user'))
    return render_template('user-insert.html', form=form)

@app.route('/user/delete', methods= ['GET', 'POST'])
def userDelete():
    form = deleteUserForm(request.form)
    if form.validate_on_submit():
        User.query.filter_by(user_id=form.userid.data).delete()
        db.session.commit()

        flash(f'User Deleted!','success')
        return redirect(url_for('user'))
    return render_template('user-delete.html', form=form)

@app.route('/user/update', methods= ['GET', 'POST'])
def userUpdate():
    form = updateUserForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(user_id=form.userid.data)
        user.name=form.name.data
        user.review_count=form.review_count.data
        db.session.commit()

        flash(f'User Updated!','success')
        return redirect(url_for('user'))
    return render_template('user-update.html', form=form)


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


@app.route('/reviews')
def reviews():
    return render_template('reviews.html')

@app.route('/reviews/insert', methods= ['GET', 'POST'])
def reviewsInsert():
    form = newReviewForm(request.form)
    if form.validate_on_submit():

        review = Review(review_id= form.review_id.data, business_id=form.business_id.data, user_id=form.userid.data,
        stars= form.stars.data, review_text= form.review_text.data)
        db.session.add(business)
        db.session.commit()

        flash(f'Review Inserted!','success')
        return redirect(url_for('reviews'))
    return render_template('reviews-insert.html', form=form)

@app.route('/reviews/delete', methods= ['GET', 'POST'])
def reviewDelete():
    form = deleteReviewForm(request.form)
    if form.validate_on_submit():
        Review.query.filter_by(review_id=form.review_id.data).delete()
        db.session.commit()

        flash(f'Review Deleted!','success')
        return redirect(url_for('review'))
    return render_template('reviews-delete.html', form=form)

@app.route('/reviews/update', methods= ['GET', 'POST'])
def reviewUpdate():
    form = updateReviewForm(request.form)
    if form.validate_on_submit():
        review = Review.query.filter_by(review_id=form.review_id.data)
        review.user_id=form.userid.data
        review.business_id=form.business_id.data
        review.stars=form.stars.data
        review.review_text=form.review_text.data
        db.session.commit()

        flash(f'Review Updated!','success')
        return redirect(url_for('review'))
    return render_template('reviews-update.html', form=form)


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
    model_word = 'Pizza'
    rows = c.execute('SELECT "Business".business_name FROM postgres.public."Business" WHERE stars >=4 and categories LIKE %s', ("%" + model_word + "%"))   
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
    model_word6 = 'Arcadia Tavern'
    #The orginal SQL Query we wrote was: SELECT "Reviews".review_text FROM postgres.public."Reviews" WHERE business_id = (SELECT "Business".business_id FROM postgres.public."Business" WHERE "business_name" = 'Arcadia Tavern');
    #However it was switched to this in order for the code to work without errors
    rows = c.execute('SELECT "Reviews".review_text FROM postgres.public."Reviews" WHERE business_id = (SELECT "Business".business_id FROM postgres.public."Business" WHERE "business_name" LIKE %s)', ("%" + model_word6 + "%"))
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
    model_word8 = 'Kfc'
    rows = c.execute('SELECT AVG("Business".stars) AS "Average Rating of KFC Stores", SUM("Business".review_count) AS "Total Number of Reviews for All KFC Stores" FROM postgres.public."Business" WHERE business_name LIKE %s', ("%" + model_word8 + "%"))   
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

