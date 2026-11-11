<<<<<<< HEAD
from flask import Flask, render_template, request
from flask import Flask, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/")
def index():
    member_name = {
        "owner": "dharmik",
        "music director": "harsh",
        "singer": "hardik",
        "rapper": "tushar",
        "lyricist": "ankit",
        "script writer": "prashant",
        "investor": "laxit",
    }
    return render_template("index.html", member_name=member_name)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        user_name = request.form["name"]
        user_email = request.form["email"]
        user_message = request.form["message"]
        print(f"Received form submission: Name={user_name}, Email={user_email}, Message={user_message}")
        # Process the form data (e.g., save to database, send email)
        return render_template("formcontact.html", name=user_name, email=user_email, message=user_message)
    return render_template("formcontact.html")

=======
from flask import Flask, render_template, request
from flask import Flask, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/")
def index():
    member_name = {
        "owner": "dharmik",
        "music director": "harsh",
        "singer": "hardik",
        "rapper": "tushar",
        "lyricist": "ankit",
        "script writer": "prashant",
        "investor": "laxit",
    }
    return render_template("index.html", member_name=member_name)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        user_name = request.form["name"]
        user_email = request.form["email"]
        user_message = request.form["message"]
        print(f"Received form submission: Name={user_name}, Email={user_email}, Message={user_message}")
        # Process the form data (e.g., save to database, send email)
        return render_template("formcontact.html", name=user_name, email=user_email, message=user_message)
    return render_template("formcontact.html")

>>>>>>> 0be82eea013b4a95ecf7d92f4bd55fb50d4253d3
app.run(debug=True)