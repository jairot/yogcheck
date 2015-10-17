from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/categories")
def categories():
    return render_template('categories.html')

@app.route('/categories/<category>')
def challenges(category=None):
    return render_template("category.html", category=category)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
