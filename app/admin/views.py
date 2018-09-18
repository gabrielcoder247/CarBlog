from flask import render_template, redirect, url_for, flash, request
from ..models import User
from flask_login import login_user, login_required, logout_user, current_user
from .. import db
from .forms import RegistrationForm, LoginForm, ResetPassword, NewPassword
from . import admin
from ..email import send_email, send_reset_email, send_registration_email

@admin.route('/register', methods = ['GET','POST'])
# @login_required
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        pass_key = form.password.data
        db.session.add(user)
        db.session.commit()

        # mail_message('Welcome to Watchlist', 'email/welcome_user', user.email, user=user)
        # send_email(subject="Registration", sender=os.environ.get('MAIL_USERNAME'),recepients=[user.email],text_body='Test Email',html_body=render_template('500.html'))
        send_registration_email(user, pass_key)

       
    
    title = "Create New Account"

    return render_template('admin/register.html',registration_form = form, title = title)

@admin.route('/login', methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or Password')

    title = "Admin Login | BeauCar "
    return render_template('admin/login.html', login_form = login_form,title=title)
    
@admin.route('/logout')
@login_required
def logout():
    logout_user()
    # flash("You have been successfully logged out")
    return redirect(url_for('main.index'))


@admin.route('/reset',methods=['GET','POST'])
def reset_password():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPassword()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_reset_email(user)
            flash('Check email on how to reset password')
            return redirect(url_for('admin.login'))
        elif not user:
            flash('The email does not exist')
    return render_template('admin/reset.html',title='Reset Password',form=form)

@admin.route('/new_password/<token>', methods=['GET','POST'])
def new_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = User.verify_reset_password(token)
    if not user:
        return redirect(url_for('main.index'))
    form = NewPassword()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset')
        return redirect(url_for('admin.login'))
    return render_template('admin/change_password.html',title='Reset Password',form=form)
