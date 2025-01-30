from flask import Flask,render_template, request,redirect,url_for
from fake_db import users

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("pages/home.html")

@app.route('/about')
def about():
    return render_template("pages/about.html")


@app.route('/contact', methods = ["GET", "POST"])
def contact():
    if request.method == "POST":
        message = request.form['message']
        print(f"Uživatel poslal dotaz: {message}")
        return render_template("pages/success.html",message=message)
    return render_template("pages/contact.html")

@app.route('/success')
def success():
    return render_template("pages/success.html")

@app.route('/user_list')
def user_list():
    return render_template("pages/user_list.html",users=users)

@app.route('/profile/<int:id>')
def profile(id):
    return render_template("pages/profile.html", **users[id])

if __name__ == "__main__":
    app.run(debug=True)