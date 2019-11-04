from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField, BooleanField
from wtforms.validators import DataRequired, NumberRange, ValidationError
from webapp.models import *

class newUserForm(FlaskForm):
    userid = StringField('User ID', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    review_count = IntegerField('Review Count', validators=[DataRequired()])
    submit = SubmitField('Insert')

    def validate_userid(self, uid):
        user = User.query.filter_by(user_id=uid.data)
        if user:
            raise ValidationError("User ID already Exists")

class newBusinessForm(FlaskForm):
    business_id = StringField('Business ID', validators=[DataRequired()])
    active = BooleanField('Active? Check for Yes')
    categories = StringField('Categories', validators=[DataRequired()])
    business_name = StringField('Business Name', validators=[DataRequired()])
    review_count = IntegerField('Review Count', validators=[DataRequired()])
    stars = FloatField('Stars', validators=[DataRequired(), NumberRange(0,5)])
    submit = SubmitField('Insert')

    def validate_business_id(self, bid):
        business = Busines.query.filter_by(business_id=bid.data)
        if business:
            raise ValidationError("Business ID already Exists")

class newReviewForm(FlaskForm):
    review_id = StringField('Review ID', validators=[DataRequired()])
    userid = StringField('User ID', validators=[DataRequired()])
    business_id = StringField('Business ID', validators=[DataRequired()])
    stars = FloatField('Stars', validators=[DataRequired(), NumberRange(0,5)])
    review_text = StringField('Review', validators=[DataRequired()])
    submit = SubmitField('Insert')

    def validate_review_id(self, rid):
        review = Review.query.filter_by(review_id=rid.data)
        if review:
            raise ValidationError("Review ID already Exists")

class newCheckInForm(FlaskForm):
    business_id = StringField('Business ID', validators=[DataRequired()])
    day_of_week = StringField('Day of the Week', validators=[DataRequired()])
    submit = SubmitField('Insert')