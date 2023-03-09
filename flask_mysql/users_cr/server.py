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
    User.save(request.form)
    return redirect('/show_user')
    # return redirect(f'/user/show/{id}' )

@app.route('/show_user')
def show_user():
    id=request.form['id']
    user=User.get_one(id)
    return render_template('read_one.html', one_user=user)

@app.route('/new_user')
def new_user():
    return render_template('create.html')

@app.route('/home')
def home():
    return redirect('/')



if __name__ == "__main__":
    app.run(debug = True, port=5001)