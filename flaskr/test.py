from flaskr import app
from flask import render_template
import os 

# @app.route("/")
# def index():
#     return render_template("index.html")

@app.route("/")
def index():
    my_var = os.getenv("mama") 
    return render_template("index.html", my_var=my_var)