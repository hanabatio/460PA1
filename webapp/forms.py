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
        user = db.session.query(User.user_id).filter_by(user_id=uid.data).scalar()
        if user:
            raise ValidationError("User ID already exists.")

class deleteUserForm(FlaskForm):
    userid = StringField('User ID', validators=[DataRequired()])
    submit = SubmitField('Insert')

    def validate_userid(self, uid):
        user = db.session.query(User.user_id).filter_by(user_id=uid.data).scalar()
        if  not user:
            raise ValidationError("User ID does not exist.")

class updateUserForm(FlaskForm):
    userid = StringField('User ID', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    review_count = IntegerField('Review Count', validators=[DataRequired()])
    submit = SubmitField('Insert')

    def validate_userid(self, uid):
        user = db.session.query(User.user_id).filter_by(user_id=uid.data).scalar()
        if  not user:
            raise ValidationError("User ID does not exist.")


class newBusinessForm(FlaskForm):
    business_id = StringField('Business ID', validators=[DataRequired()])
    active = BooleanField('Active? Check for Yes')
    categories = StringField('Categories', validators=[DataRequired()])
    business_name = StringField('Business Name', validators=[DataRequired()])
    review_count = IntegerField('Review Count', validators=[DataRequired()])
    stars = FloatField('Stars', validators=[DataRequired(), NumberRange(0,5)])
    submit = SubmitField('Insert')

    def validate_business_id(self, bid):
        business = db.session.query(Busines.business_id).filter_by(business_id=bid.data).scalar()
        if business:
            raise ValidationError("Business ID already Exists")

class deleteBusinessForm(FlaskForm):
    business_id = StringField('Business ID', validators=[DataRequired()])
    submit = SubmitField('Insert')

    def validate_business_id(self, bid):
        business = db.session.query(Busines.business_id).filter_by(business_id=bid.data).scalar()
        if  not business:
            raise ValidationError("Business ID does not exist.")

class updateBusinessForm(FlaskForm):
    business_id = StringField('Business ID', validators=[DataRequired()])
    active = BooleanField('Active? Check for Yes')
    categories = StringField('Categories', validators=[DataRequired()])
    business_name = StringField('Business Name', validators=[DataRequired()])
    review_count = IntegerField('Review Count', validators=[DataRequired()])
    stars = FloatField('Stars', validators=[DataRequired(), NumberRange(0,5)])
    submit = SubmitField('Insert')

    def validate_business_id(self, bid):
        business = db.session.query(Busines.business_id).filter_by(business_id=bid.data).scalar()
        if  not business:
            raise ValidationError("Business ID does not exist.")


class newReviewForm(FlaskForm):
    review_id = StringField('Review ID', validators=[DataRequired()])
    userid = StringField('User ID', validators=[DataRequired()])
    business_id = StringField('Business ID', validators=[DataRequired()])
    stars = FloatField('Stars', validators=[DataRequired(), NumberRange(0,5)])
    review_text = StringField('Review', validators=[DataRequired()])
    submit = SubmitField('Insert')

    def validate_review_id(self, rid):
        review = db.session.query(Review.review_id).filter_by(review_id=rid.data).scalar()
        if review:
            raise ValidationError("Review ID already Exists")

class deleteReviewForm(FlaskForm):
    review_id = StringField('Review ID', validators=[DataRequired()])
    submit = SubmitField('Insert')

    def validate_review_id(self, rid):
        review = db.session.query(Review.review_id).filter_by(review_id=rid.data).scalar()
        if  not review:
            raise ValidationError("Review ID does not exist.")

class updateReviewForm(FlaskForm):
    review_id = StringField('Review ID', validators=[DataRequired()])
    userid = StringField('User ID', validators=[DataRequired()])
    business_id = StringField('Business ID', validators=[DataRequired()])
    stars = FloatField('Stars', validators=[DataRequired(), NumberRange(0,5)])
    review_text = StringField('Review', validators=[DataRequired()])
    submit = SubmitField('Insert')

    def validate_review_id(self, rid):
        review = db.session.query(Review.review_id).filter_by(review_id=rid.data).scalar()
        if  not review:
            raise ValidationError("Review ID does not exist.")

class newQueryForm(FlaskForm):
    top_number = IntegerField('Top #', validators=[DataRequired()])
    category_finder = StringField('Type of Business', validators=[DataRequired()])
    submit = SubmitField('Search')

class newCheckInForm(FlaskForm):
    business_id = StringField('Business ID', validators=[DataRequired()])
    day_of_week = StringField('Day of the Week', validators=[DataRequired()])
    submit = SubmitField('Insert')
