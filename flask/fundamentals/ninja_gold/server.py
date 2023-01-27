from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)

app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index2.html", num = 0)

@app.route('/process_money', methods=['POST'])
def process_money():
    print('get gold')
    if request.form['building'] == 'farm':
        num += random.randint(10,20)
    elif request.form['building'] == 'cave':
        num += random.randint(5,10)
    elif request.form['building'] == 'house':
        num += random.randint(2,5)
    else:
        num += random.randint(-50,50)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)