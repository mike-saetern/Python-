from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def ninjas():
    
    return render_template('ninja.html',dojos= dojo.Dojo.get_all())


@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')

@app.route('/ninja/edit/<int:id>')
def edit(id):
    data = {
        "id":id
    }
    return render_template('edit.html', dojo=ninja.Ninja.get_one(data))

@app.route('/ninja/delete/<int:id>')
def delete(id):
    ninj = ninja.Ninja.get_one({'id':id})
    ninja.Ninja.delete(id)
    return redirect(f'/dojo/{ninj.dojo_id}')

@app.route('/ninja/update/<int:id>', methods=['POST'])
def update(id):
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'id': id
    }
    ninja.Ninja.update(data)
    return redirect(f'/dojo/{request.form["dojo_id"]}')