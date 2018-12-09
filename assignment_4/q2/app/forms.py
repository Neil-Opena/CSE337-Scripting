from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

class TextForm(FlaskForm):
    text = TextAreaField('Text', validators=[DataRequired()])
    choices = RadioField(choices=[(1,'Word Count'), (2,'Character Count'), (3,'Most Frequent 5 words')], validators=[DataRequired()])
    delimiters = StringField('Delimeters:', validators=[DataRequired()])
    submit = SubmitField('Submit Text')

