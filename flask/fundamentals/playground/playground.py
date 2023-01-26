from flask import Flask, render_template  # Import Flask to allow us to create our app, render_template to link html
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')
def index():
    return "Welcome"

@app.route('/play')
def boxes():
  return render_template("index.html",num=3,color="blue")

@app.route('/play/<int:num>')
def num_boxes(num):
    return render_template("index.html",num=num, color="blue")

@app.route('/play/<int:num>/<string:color>')
def num_box_color(num,color):
    return render_template("index.html",num=num, color=color)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.