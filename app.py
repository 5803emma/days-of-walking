import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'walking_app'
app.config["MONGO_URI"] = 'mongodb+srv://root:johnbell@myfirstcluster-20lqh.mongodb.net/walking_app?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_walk_names")
def get_walk_names():
    return render_template("walks.html", walks=mongo.db.walks.find())
    

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)