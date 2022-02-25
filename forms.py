from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email


class Domowe_wydatkiForm(FlaskForm):
    nazwa_produktu = StringField('Nazwa produktu', validators=[DataRequired()])   ## title
    opis = TextAreaField('Opis produktu', validators=[DataRequired()]) ## description
    zrealizowane = BooleanField('Zakupione ?', validators=[])   ## done