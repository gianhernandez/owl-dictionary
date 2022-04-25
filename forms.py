from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class FindWord(FlaskForm):
    title = StringField(validators=[DataRequired()],
                        render_kw={'autofocus': True, 'placeholder': 'Search for a definition'})
    submit = SubmitField("Search")
