import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectID

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'walking_app'
app.config["MONGO_URI"] = 'mongodb+srv://root:johnbell@myfirstcluster-20lqh.mongodb.net/walking_app?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/add_walk")
def add_walk ():
    return render_template("add_walk.html")
    
@app.route("/leave_review")
def leave_review ():
    return render_template("leave_review.html")
    
@app.route("/read_review")
def read_review():
    return render_template("read_review.html")
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)