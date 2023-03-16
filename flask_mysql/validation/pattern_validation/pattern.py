r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'

import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    @staticmethod
    def validate_user( user ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid
    
from flask_app.models.user import User
@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
    # we redirect to the template with the form.
        return redirect('/')
    # ... do other things
    return redirect('/dashboard')

#Say we want to categorize flash messages into different labels or buckets. 
# We can utilize categories by passing a second argument in the flash function:
flash("Email cannot be blank!", 'email')

