from flask import render_template, session, request, url_for, flash, redirect
from shop import app, db
from .form import RegistrationForm


@app.route("/")
def home():
    return "<h1>Welcome to flask page<h1/>"

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # user = User(form.username.data, form.email.data,
        #             form.password.data)
        # db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('admin/signup.html', form=form)

