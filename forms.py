from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField, BooleanField
from wtforms.validators import DataRequired, NumberRange

class newUserForm(FlaskForm):
    userid = StringField('User ID', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    review_count = IntegerField('Review Count', validators=[DataRequired()])
    submit = SubmitField('Insert')

class newBusinessForm(FlaskForm):
    business_id = StringField('Business ID', validators=[DataRequired()])
    active = BooleanField('Active Status', validators=[DataRequired()])
    categories = StringField('Categories', validators=[DataRequired()])
    business_name = StringField('Business Name', validators=[DataRequired()])
    review_count = IntegerField('Review Count', validators=[DataRequired()])
    stars = FloatField('Stars', validators=[DataRequired(), NumberRange(0,5)])
    submit = SubmitField('Insert')