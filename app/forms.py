from flask_wtf import FlaskForm # 从flask_wtf包导入FlaskForm类
from wtforms.validators import DataRequired, Email,ValidationError,EqualTo
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('<PASSWORD>', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        # 如果用户已被注册
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        # 如果用户email 已被注册
        if user is not None:
            raise ValidationError('Please use a different email address.')