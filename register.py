from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired


class RegisterForms(FlaskForm):
    email = EmailField("Почта", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    repeat_password = PasswordField(
        "Повторите пароль", validators=[DataRequired()])
    name = StringField("Имя", validators=[DataRequired()])
    submit = SubmitField("Зарегистрироваться", validators=[DataRequired()])
