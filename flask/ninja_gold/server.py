from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)

app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = 0
    if 'outcomes' not in session:
        session['outcomes'] = []
        earn = 0
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['building'] == 'farm':
        earn = random.randint(10,20)
        session['num'] += earn
        color = 'green'
        session['outcomes'].append({'message':f"Earned {earn} golds from the {request.form['building']}", 'color': color})
    elif request.form['building'] == 'cave':
        earn = random.randint(5,10)
        session['num'] += earn
        color = 'green'
        session['outcomes'].append({'message':f"Earned {earn} golds from the {request.form['building']}", 'color': color})
    elif request.form['building'] == 'house':
        earn = random.randint(2,5)
        session['num'] += earn
        color = 'green'
        session['outcomes'].append({'message':f"Earned {earn} golds from the {request.form['building']}", 'color': color})
    else:
        earn = random.randint(-50,50)
        session['num'] += earn
        if earn > 0:
            color = 'green'
            session['outcomes'].append({'message':f"Earned {earn} golds from the {request.form['building']}", 'color': color})
        elif earn < 0:
            color = 'red'
            session['outcomes'].append({'message':f"Entered the casino and lost {earn} golds!", 'color': color})
    return redirect('/')


@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5001)