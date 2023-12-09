from flask import Flask, render_template, flash, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from form import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '9ada898c7ee83b8c36da6d8affdcbf2a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///profiles.db'

db = SQLAlchemy(app)

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=True)
    last_name = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    image = db.Column(db.String(20), nullable=True)
    profile = db.relationship('Profile', backref='author', lazy=True)

    def __repr__(self):
        return f"User ='{self.email}'"

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    skill = db.Column(db.Text, nullable=True)
    experience = db.Column(db.Text, nullable=True)
    certification = db.Column(db.Text, nullable=True)
    last_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=False)


    def __repr__(self):
        return f"User ='{self.title}', '{self.last_updated}' "

users = [
    {
        'first_name': 'Mahjabin',
        'last_name': 'Alam',
        'email': 'natasha.mahjabin@gmail.com'
    },
    {
        'first_name': 'Shoriful',
        'last_name': 'Islam',
        'email': 'shoriful.islam@gmail.com'
    },
    {
        'first_name': 'Tinder',
        'last_name': 'Lominer',
        'email': 'tinder.lominer@gmail.com'
    }
]

@app.route("/", methods=['GET', 'POST'])
@app.route("/register", methods=['GET', 'POST'])
def register():
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register User', form = registration_form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "natasha.test@gmail.com" and login_form.password.data == "Test@123":
            flash('the form should be submitted', 'success')
            return redirect(url_for("list_users"))
        else:
            flash('something wrong', 'error')
    return render_template('login.html', title = 'Register User', form = login_form)

@app.route("/list",  methods=['GET'])
def list_users():
    return render_template('list_users.html', users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)