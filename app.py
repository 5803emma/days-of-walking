import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'walking_app'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_walks")
def get_walks():
    return render_template("home.html", walks=mongo.db.walks.find())
    
@app.route("/about")
def about():
    return render_template("about.html")
    

@app.route("/add_new_walk")
def add_new_walk():
    return render_template("add_walk.html")


@app.route("/insert_walk", methods=['POST'])
def insert_walk():
    walk = mongo.db.walks
    walk.insert_one(request.form.to_dict())
    return redirect(url_for('get_walks'))

# Update Information About Walk

@app.route("/edit_walk/<walk_id>")
def edit_walk(walk_id):
    the_walk = mongo.db.walks.find_one({"_id": ObjectId(walk_id)})
    return render_template("update_walk.html", walk=the_walk)
    
@app.route("/update_walk/<walk_id>", methods=["POST"])
def update_walk(walk_id):
    walk = mongo.db.walks
    walk.update({'_id': ObjectId(walk_id)}, {
        'walk_name' : request.form.get('walk_name'),
        'walk_location' : request.form.get('walk_location'),
        'walk_length' : request.form.get('walk_length'),
        'walk_difficulty' : request.form.get('walk_difficulty'),
        'walk_terrain' : request.form.get('walk_terrain')
    })
    return redirect(url_for('get_walks'))

# Delete Option

@app.route("/delete_walk/<walk_id>")
def delete_walk(walk_id):
    mongo.db.walks.remove({'_id': ObjectId(walk_id)})
    return redirect(url_for('get_walks'))
    
@app.route("/leave_review")
def walk_review():
    return render_template("walk_review.html", walks=mongo.db.walks.find())    
    
# Sends the data that the user inserts to the database

@app.route("/walk_review", methods=['POST'])
def insert_review():
    review = mongo.db.reviews
    review.insert_one(request.form.to_dict())
    return redirect(url_for('walk_review'))


@app.route("/read_review")
def read_review():
    return render_template("read_reviews.html", reviews=mongo.db.reviews.find())
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "0.0.0.0"),
    port=int(os.environ.get("PORT", "5000")),
    debug=False)