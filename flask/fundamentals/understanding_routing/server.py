from flask import Flask
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')
def hello():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def say_name(name):
    return f"Hi {name.capitalize()}!"#capitalize makes first letter capital

@app.route('/repeat/<int:num>/<string:word>')#int:num makes it an integer string:word turns into a string
def repeat_word(num,word):
    output = ''

    for i in range(0,num):
        output += f"{word.capitalize()}"

    return output


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)

# run pipenv install flask in the project folder. then run pipenv shell for the virtual environment