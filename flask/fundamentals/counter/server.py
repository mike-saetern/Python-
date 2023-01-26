from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key ='keep my name, keep my name'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count']+= 1
    return render_template("index.html")

@app.route('/destroy_session', methods=['POST'])
def delete():
    session.pop('count')
    return redirect ('/')

@app.route('/add_2', methods=['POST'])
def add_2():
    session['count']+= 1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)