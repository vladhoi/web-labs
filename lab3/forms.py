from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, AnyOf


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired('A username is required!'), Length(min=5, max=10,
                                                                                                    message='Must be between 5 and 10 characters.')])
    password = PasswordField('password',
                             validators=[InputRequired('Password is required!'), AnyOf(values=['password', 'secret'])])
    recaptcha = RecaptchaField()
