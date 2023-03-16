from flask_app import app
from flask import render_template,redirect,session,request
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User

@app.route('/create_recipe',methods=['POST'])
def create_recipe():
    if 'user_id' not in session:#checks to see if user is logged in
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('create')
    data ={
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "date_cooked": request.form['date_cooked'],
        "under_30min": request.form['under_30min'],
        "user_id": session['user_id'],
    }
    recipe = Recipe.save(data) #recipe is a variable calls Recipe class and save method
    return redirect("/dashboard")

@app.route('/recipes/<int:id>')
def view_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    user_id ={
        "id": session['user_id']
    }
    data= {
        "id": id
    }
    return render_template('view.html', this_recipe=Recipe.get_by_id(data),this_user=User.get_by_id(user_id))

@app.route('/delete/<int:id>')
def delete(id):
    Recipe.delete(id)
    return redirect('/dashboard')

@app.route('/edit/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('logout')
    data = {
        "id" : id
    }
    return render_template('edit.html', this_recipe=Recipe.get_by_id(data))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    print(request.form)
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect(f'/edit/{id}')
    data ={
        "id": id,
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "date_cooked": request.form['date_cooked'],
        "under_30min": request.form['under_30min'],
    }
    Recipe.update(data)
    return redirect('/dashboard')