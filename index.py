# importing modules from flask library
from flask import Flask, render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__, template_folder="template")

# write the routes using decorator functions
# default route or 'URL'


@app.route("/index")
def home():

    name = "Jax"  # write your name
    age = "15"  # write your age

    return render_template('index.html', name=name, age=age)

# define the route to father webpage


@app.route("/father")
def home1():

    name = "Bob"  # write your name
    age = "87"  # write your age

    return render_template('father.html', name=name, age=age)

# define the route to mother webpage


@app.route("/mother")
def home2():

    name = "Sara"  # write your name
    age = "67"  # write your age

    return render_template('mother.html', name=name, age=age)

# define the route to friends webpage


@app.route("/freind")
def freind():

    name = "Jeff"  # write your name
    age = "17"  # write your age

    return render_template('friend.html', name=name, age=age)
# add other routes, if you want


# run the file
if __name__ == '__main__':
    app.run(debug=True)
