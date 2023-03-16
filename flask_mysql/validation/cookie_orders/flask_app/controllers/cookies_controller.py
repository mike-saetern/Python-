from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models.cookie import Cookie


@app.route('/')
def index():
    return render_template('cookies.html', orders = Cookie.get_all())


@app.route('/new')
def new():
    return render_template('new_order.html')

@app.route('/change/<int:id>')
def change(id):
    order = Cookie.get_by_id(id)
    return render_template('change_order.html', order = order)

@app.route("/cookies/edit/<int:id>", methods=["POST"])
def update_cookie(id):
    if not Cookie.is_valid(request.form):
        return redirect(f"/change/{request.form['id']}")
    Cookie.update(data)
    return redirect("/")

@app.route('/cookies/create', methods=['POST'])
def create_order():
    if not Cookie.is_valid(request.form):
        return redirect('/new')
    Cookie.save(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    Cookie.delete(id)
    return redirect ('/')

