from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,DateField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class PersonajeForm(FlaskForm):
    nombre =StringField('Nombre : ',validators=[DataRequired()])
    boton = SubmitField("Guardar Libro")
