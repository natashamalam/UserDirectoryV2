from flask import Flask, render_template

app = Flask(__name__)


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

@app.route("/")
def add_user():
    return render_template('add_user.html')

@app.route("/list")
def list_users():
    return render_template('list_users.html', users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)