from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def add_user():
    return render_template('add_user.html')

@app.route("/list")
def list_users():
    return render_template('list_users.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)