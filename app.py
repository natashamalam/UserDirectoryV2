from flask import Flask, render_template, flash, redirect, url_for
from form import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '9ada898c7ee83b8c36da6d8affdcbf2a'

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
    return render_template('login.html', title = 'Register User', form = login_form)

@app.route("/list",  methods=['GET'])
def list_users():
    return render_template('list_users.html', users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)