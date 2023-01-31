from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional


class AddPetForm(FlaskForm):
    name = StringField("Pet Name",  validators=[
                       InputRequired(message="Pet name cannot be left blank")])
    species = StringField("Species", InputRequired(message = "Species cannot be left blank"))                   
    photo_url = StringField("Pet Photo", validators=[Optional()])
    age = StringField("Age", validators=[Optional()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available", validators =[InputRequired()])




