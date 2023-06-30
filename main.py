from flask import Flask, render_template, redirect
from register import RegisterForms
from login import AuthForms

app = Flask(__name__)
app.config["SECRET_KEY"] = "hello hello"


@app.route('/', methods=["GET", "POST"])
def idex():
    return render_template('index.html', title="Mane page")


@app.route('/students')
def students():
    list_students = ["Иван Иванович Иванов", "Иван Иванович Иванов",
                     "Иван Иванович Иванов", "Иван Иванович Иванов", "Иван Иванович Иванов"]
    return render_template('students.html', title="List of students", list=list_students)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = AuthForms()
    if form.validate_on_submit():
        mail = form.data['mail']
        password = form.data['password']
        return render_template('reg.html', title="Authorisation", form=form, message="Wellcome")
    return render_template('reg.html', title="Authorisation", form=form)


@app.route('/profile', methods=["GET", "POST"])
def profil():
    return render_template('profile.html', title="Profile")


@app.route('/registr', methods=["GET", "POST"])
def registr():
    form = RegisterForms()
    if form.validate_on_submit():
        if form.data['password'] != form.data['repeat_password']:
            return render_template('reg.html', title="Registration", form=form, message="The passes are not equal")
    return render_template('reg.html', title="Registration", form=form)


if __name__ == '__main__':
    app.run()
