from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="studentdb"
)

cursor = db.cursor()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():

    name = request.form["name"]
    email = request.form["email"]

    sql = "INSERT INTO students(name,email) VALUES(%s,%s)"
    values = (name,email)

    cursor.execute(sql, values)
    db.commit()

    return "Student Registered Successfully"


if __name__ == "__main__":
    app.run(debug=True)