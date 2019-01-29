# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 11:15:13 2019

@author: harri
"""
#----------------------------------------------------------------------------------------------------------------------
# CHAPTER 16 - FLASK
#----------------------------------------------------------------------------------------------------------------------


# TASK 1 - CREATE SIMPLE WEB APP
#--------------------------------------------------------------------------------------

# from the flask library, import the Flask class
# the render_template is a function that tells flask what HTML pages to display (template = HTML page)
from flask import Flask, request, render_template

# create a variable called app to save output from Flask
app = Flask("MyApp")


# TASK 2 - USE ROUTES AND DECORATORS
#--------------------------------------------------------------------------------------

# this is a decorator
# they allow you to execute code and functions at a particular location
# the @app.route is flask syntax
# the decorator always begins with @
# the decoratr goes on the line before a function is defined
# the decorator is not a function-it specifies the path in the web app where you want to run your functions
@app.route("/")

def index():
    return render_template("index.html", title="homepage")

# TASK 3 - USE RENDER TEMPLATE
#--------------------------------------------------------------------------------------


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/<name>")

def hello(name):
    return render_template("hello.html", title="Personal", name=name.title())
    



@app.route("/signup", methods=["POST"])

def sign_up():
    form_data = request.form
    email=form_data["email"]
    result= "All OK"
    return render_template("signup.html", title="Sign up", **locals())

# this lines makes flask run the app
# the debug part doesn't debug, it provides extra information about errors to help you debug
app.run(debug = True)


# the @app.route specifies the location
# if it were @app.route("/bio") you could visit http://127.0.0.1:5000/bio


