from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

class TextForm(FlaskForm):
    text = TextAreaField('Text', validators=[DataRequired()])
    operations = RadioField(choices=[('a','Word Count'), ('b','Character Count'), ('c','Most Frequent 5 words')], validators=[DataRequired()])
    delimiters = StringField('Delimeters:')
    submit = SubmitField('Submit Text')

