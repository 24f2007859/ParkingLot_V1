from flask import request, flash, redirect, render_template
from app import app, db
from ParkingLot_V1.models import User

@app.route("/user/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if User.query.filter((User.username == username) | (User.email == email)).first():
            flash("Username or email already taken.")
        else:
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash("Registration successful!")
            return redirect("/login")

    return render_template("/register.html")