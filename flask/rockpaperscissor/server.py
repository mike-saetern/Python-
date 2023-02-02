from flask import Flask, render_template, request,redirect,session
import random
app = Flask(__name__)
app.secret_key = "rock_paper_scissors"

@app.route("/")
def index():
    if 'draw' not in session:
        session['draw'] = 0
        session['win'] = 0
        session['loses'] = 0
        # session['outcomes'] = []
    return render_template("index.html")

@app.route("/selection", methods=['post'])
def selection():
    if 'outcomes' not in session:
        session['outcomes'] = []
    rand_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    session['our_choice'] = request.form['selection']
    session['opponents_choice'] = rand_choice
    if session['our_choice'] == session['opponents_choice']:
        session['draw'] += 1
        session['current_result'] = 'draw'
        color = 'blue'
        session['outcomes'].append({'message': f"Your opponent chose {session['opponents_choice']}, You chose {session['our_choice']}, it was a {session['current_result']}", 'color': color})
        
    elif (session['our_choice'] == 'Rock' and session['opponents_choice'] == 'Scissors') or (session['our_choice'] == 'Paper' and session['opponents_choice'] == 'Rock') or (session['our_choice'] == 'Scissors' and session['opponents_choice'] == 'Paper'):
        session['win'] += 1
        session['current_result'] = 'win'
        color = 'green'

    else: 
        session['loses'] += 1
        session['current_result'] = 'lose'
        color = 'red'
    
    if session['current_result'] != 'draw':
        session['outcomes'].append({'message': f"Your opponent chose {session['opponents_choice']}, You chose {session['our_choice']}, You {session['current_result']}", 'color': color})
    # rock beats scissors
    # paper beats rock
    # scissors beats paper
    return redirect("/")

@app.route("/clear_session")
def clear_session():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)