from flask import render_template, session, request, url_for, flash, redirect
from shop import app, db, bcrypt
from .form import SigninForm, SignupForm
from .models import User




@app.route("/")
def home():
    return render_template("admin/index.html", title="admin tab")


@app.route("/admin")
def admin():
    if 'email' not in session:
        flash("Yuo are not logged")
        return redirect(url_for('signin'))
    return render_template("admin/index.html", title="admin tab")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_pass = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hash_pass)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering', 'success')
        return redirect(url_for('home'))
    return render_template('admin/signup.html', form=form, title="Sign up to Shop")


@app.route('/signin', methods=['GET','POST'])
def singin():
    form = SigninForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Welcome, {user.username}', 'success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash('Fail in sign in, try again.', 'danger')
            return redirect(url_for('home'))
    return render_template('admin/signin.html', form=form, title='Sign in to Shop')