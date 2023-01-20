from flask_app import app, render_template, request, redirect, session
from flask_app.models.user import User

# when the page open it will route to /user/new
@app.route('/')
def index():
    return render_template("create_page.html")


@app.route('/users/new', methods=['POST'])
def create_users():
    User.create(request.form)
    return redirect('/users')

@app.route('/users')
def display_users():
    return render_template("display_users.html", users=User.get_all())

@app.route('/users/<int:id>/edit')
def edit_user(id): #Have to pass id in as a parameter
    data = {
        "id": id
    }
    return render_template("edit_user.html", user=User.get_one_user(data))

@app.route('/show/user/<int:id>')
def show_user(id):
    data = {
        "id": id
    }
    user = User.get_one_user(data)
    if user: #Checks to see if user exist if doesn't redirects to home page
        return render_template("show_user_edit.html", user=user)
    return redirect("/")

@app.route('/user/<int:id>', methods=['POST'])
def update_user(id):
    data = {
        **request.form, #takes all the key value pairs out of dictionary and puts it into new dictionary
        "id": id
    }
    User.update(data)
    return redirect(f'/show/user/{id}')

@app.route('/users/delete/<int:id>')
def delete_user(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect('/users')
