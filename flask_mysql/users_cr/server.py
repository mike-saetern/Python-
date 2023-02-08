from flask import Flask, render_template, redirect, request
from users import User
app = Flask(__name__)
app.secret_key = "user user user user"
@app.route('/')
def index():
    users = User.get_all()
    return render_template('read.html', all_users = users)

@app.route('/create_user', methods=['POST'])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/')

@app.route('/new_user')
def new_user():
    return render_template('create.html')

@app.route('/home')
def home():
    return redirect('/')



if __name__ == "__main__":
    app.run(debug = True, port=5001)