from flask import Flask, render_template, request, redirect, url_for, flash
import random
import csv
import pyperclip

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/", methods=["GET", "POST"])
def home():
    website = ""
    email = "example@gmail.com"
    password = ""

    if request.method == "POST":
        action = request.form.get("action")

        if action == "generate":
            letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            numbers = "0123456789"
            symbols = "!#$%&()*+"

            password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
            password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
            password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

            password_list = password_letters + password_numbers + password_symbols
            random.shuffle(password_list)
            password = "".join(password_list)

            # pyperclip.copy(password)
            # flash("Password generated and copied to clipboard!", "info")

            website = request.form.get("website")
            email = request.form.get("email")

        elif action == "save":
            website = request.form.get("website")
            email = request.form.get("email")
            password = request.form.get("password")

            if not website or not email or not password:
                flash("Please don’t leave any fields empty!", "error")
            else:
                with open("data.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([website, email, password])
                flash("Password saved successfully!", "success")

                website, email, password = "", "example@gmail.com", ""

        elif action == "clear":
            website, email, password = "", "example@gmail.com", ""
            flash("Form cleared!", "info")

    return render_template("index.html", website=website, email=email, password=password)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
