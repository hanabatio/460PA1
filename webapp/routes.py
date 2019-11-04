from flask import render_template, flash, redirect, url_for, request
from forms import *
from models import *

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
@app.route('/q1', methods=['GET','POST'])
def query1():
    table = []
    if request.method == 'POST':
        return render_template('q1.html')
    else:
        table = querie1()
        print (table)
        return render_template('q1.html', table=table)
def querie1():
    connection = db.engine.connect()
    query1command = 'SELECT * FROM postgres.public."Users" WHERE (review_count >=1)'
    response = connection.execute(query1command).fetchall()
    return str(response)
    
@app.route('/q2')
def querie2():
    connection = db.engine.connect()
    query2command = 'SELECT "Users"."name" FROM postgres.public."Users" WHERE (review_count <= 2);'
    response = connection.execute(query2command).fetchall()
    return str(response)

@app.route('/q3')
def querie3():
    connection = db.engine.connect()
    query3command = 'SELECT * FROM postgres.public."Business" WHERE (active=false);' 
    response = connection.execute(query3command).fetchall()
    return str(response)

@app.route('/q4')
def querie4():
    connection = db.engine.connect()
    query4command = 'SELECT "Business".business_name FROM postgres.public."Business" WHERE (stars >=4) AND (categories LIKE '%Pizza%') ;' 
    response = connection.execute(query4command).fetchall()
    return str(response)

@app.route('/q5')
def querie5():
    connection = db.engine.connect()
    query5command = 'SELECT COUNT(*) FROM postgres.public."Checkins" WHERE "Friday" >=1;' 
    response = connection.execute(query5command).fetchall()
    return str(response)

@app.route('/q6')
def querie6():
    connection = db.engine.connect()
    query6command = 'SELECT "Reviews".review_text FROM postgres.public."Reviews" WHERE business_id = (SELECT "Business".business_id FROM postgres.public."Business" WHERE "business_name" = ''Arcadia Tavern'');'
    response = connection.execute(query6command).fetchall()
    return str(response)
    return "Hi"

@app.route('/q7')
def querie7():
    connection = db.engine.connect()
    query7command = 'SELECT "Business".business_name FROM postgres.public."Business", postgres.public."Reviews" WHERE "Business".business_id = "Reviews".business_id AND ("Reviews".stars = 1 OR "Reviews".stars = 2);'
    response = connection.execute(query7command).fetchall()
    return str(response)

@app.route('/q8')
def querie8():
    connection = db.engine.connect()
    query8command = 'SELECT AVG("Business".stars) AS "Average Rating of All KFC Stores", SUM("Business".review_count) AS "Total Number of Reviews for All KFC Stores" FROM postgres.public."Business" WHERE business_name LIKE %' + 'Kfc' +'%;'
    response = connection.execute(query8command).fetchall()
    return str(response)
    return "Hi"

@app.route('/q9')
def querie9():
    connection = db.engine.connect()
    query9command = 'SELECT "Business".business_id AS "Business IDs of the Top 10 Most Reviewed Stores" FROM postgres.public."Business" ORDER BY "Business".review_count DESC LIMIT 10;'
    response = connection.execute(query9command).fetchall()
    return str(response)

@app.route('/q10')
def querie10():
    connection = db.engine.connect()
    query10command = 'SELECT "Users"."name" as "User with Most Reviews" FROM postgres.public."Users" ORDER BY "Users".review_count DESC LIMIT 1' 
    response = connection.execute(query10command).fetchall()
    return str(response)


if __name__ == '__main__':
    app.run(debug=True)

