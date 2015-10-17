import os

from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

path = os.path.dirname(os.path.realpath(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path + '/test.db'
db = SQLAlchemy(app)

class Categories(db.Model):
    __tablename__ = 'categories'
    category = db.Column(db.String(80), unique=True, primary_key=True)

class Activity(db.Model):
    __tablename__ = 'activity'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    category = db.Column(db.String(80),
                          db.ForeignKey("categories.category"),
                          nullable=False)
    title = db.Column(db.String(200), unique=True)
    text = db.Column(db.Text, unique=True)
    photo = db.Column(db.Text)
    location = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/categories")
def categories():
    cats = []
    for categories in Categories.query.all():
        cats.append(categories.category)
    return render_template('categories.html', cats=cats)

@app.route("/progress")
def profile():
    return render_template('progress.html')

@app.route('/categories/<category>')
def challenges(category=None):
    #category = Categories.query.filter_by(category=category).first()
    activities = Activity.query.filter_by(category=category).all()
    activity = {"id": 1}
    return render_template("list.html", category=category, activities=activities)

#@app.route('/categories/<category>/check/<_id>')
#def check(category, _id):
#    cat_check = Activity.query.filter_by(category=category).first()
#    cat_check.done = cat_check.done + 1
#    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
