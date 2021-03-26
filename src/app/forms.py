# forms.py

from flask_wtf import FlaskForm
from wtforms.fields import SubmitField
from wtforms.fields.html5 import URLField
from wtforms.validators import InputRequired, URL, Regexp


class SmuleForm(FlaskForm):
    url = URLField(validators=[
        InputRequired(),
        URL(),
        Regexp('.*smule.*', message='Not smule.com domain')
    ], description='Paste link to smule video')

    submit = SubmitField('Download')
