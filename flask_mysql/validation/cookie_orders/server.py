from flask_app import app
from flask_app.controllers import cookies_controller
from flask import render_template, session, redirect, request

if __name__ == "__main__":
    app.run(debug=True, port = 5001)