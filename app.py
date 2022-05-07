from asyncio.windows_events import NULL
from tkinter.tix import Tree
from xml.dom.expatbuilder import parseString
from click import command
from flask import Flask, jsonify, render_template, request, flash, redirect, session, send_from_directory, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
import sqlite3
import random
import json

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'Qwerty123!'

myConnection = sqlite3.connect('usersBase.sqlite')
myCursor = myConnection.cursor()
myCursor.execute("""CREATE TABLE IF NOT EXISTS users (
            login text,
            password text,
            ID integer primary key autoincrement,
            UNIQUE(login, password)
            )""")
myCursor.execute("""CREATE TABLE IF NOT EXISTS articles (
            title text,
            content text,
            ID integer primary key autoincrement,
            UNIQUE(title,content)
            )""")
myCursor.execute("""CREATE TABLE IF NOT EXISTS photos (
            link text,
            content text,
            ID integer primary key autoincrement,
            UNIQUE(link,content)
            )""")
myCursor.execute(
    "INSERT OR IGNORE INTO users (login,password) VALUES ('admin', 'admin')")
myCursor.execute(
    "INSERT OR IGNORE INTO photos (link,content) VALUES ('https://tueuropa.pl/uploads/articles_files/2021/11/05/6e7f9516-1948-d9e8-ca22-00007380aca5.jpg', 'XDDDDDDDDDDDD')")
myCursor.execute(
    "INSERT OR IGNORE INTO photos (link,content) VALUES ('https://tueuropa.pl/uploads/articles_files/2021/11/05/6e7f9516-1948-d9e8-ca22-00007380aca5.jpg', 'XDDDDDDDDDDDD')")
myCursor.execute(
    "INSERT OR IGNORE INTO photos (link,content) VALUES ('https://tueuropa.pl/uploads/articles_files/2021/11/05/6e7f9516-1948-d9e8-ca22-00007380aca5.jpg', 'XDDDDDDDDDDDD')")
myCursor.execute(
    "INSERT OR IGNORE INTO photos (link,content) VALUES ('https://tueuropa.pl/uploads/articles_files/2021/11/05/6e7f9516-1948-d9e8-ca22-00007380aca5.jpg', 'XDDDDDDDDDDDD')")
myCursor.execute(
    "INSERT OR IGNORE INTO articles (title,content) VALUES ('a', 'aaa')")
myCursor.execute(
    "INSERT OR IGNORE INTO articles (title,content) VALUES ('b', 'bbb')")
myCursor.execute(
    "INSERT OR IGNORE INTO articles (title,content) VALUES ('c', 'ccc')")
myCursor.execute(
    "INSERT OR IGNORE INTO articles (title,content) VALUES ('d', 'ddd')")

myConnection.commit()
myConnection.close()


class LoginForm(FlaskForm):
    login = StringField('Login:', validators=[DataRequired()])
    password = StringField('Password:', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    login = StringField('Login:', validators=[DataRequired()])
    password = StringField('Password:', validators=[DataRequired()])
    passwordAgain = StringField(
        'Repeat password:', validators=[DataRequired()])
    submit = SubmitField('Register')

loggedAs = ""
photos = []
articles = []

@app.route("/")

def base():
    return send_from_directory('client/public', 'index.html')

@app.route("/loggedAs")
def loggedas():
    return str(loggedAs)

@app.route("/photosbase")
def photosBase():
    global photos
    myConnection = sqlite3.connect('usersBase.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT *, oid FROM photos")
    records = myCursor.fetchall()

    for el in records:
        photos.append({"link":el[0],"content":el[1]})
    
    return jsonify(records)

@app.route("/articlesbase")
def articlesBase():
    global articles
    myConnection = sqlite3.connect('usersBase.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT *, oid FROM articles")
    records = myCursor.fetchall()

    for el in records:
        photos.append({"link":el[0],"content":el[1]})
    
    return jsonify(records)

@app.route("/features")
def features():
    return send_from_directory('client/public', 'index.html')


@app.route("/pricing")
def pricing():
    return send_from_directory('client/public', 'index.html')


@app.route("/faq")
def faq():
    return send_from_directory('client/public', 'index.html')


@app.route("/about")
def about():
    return send_from_directory('client/public', 'index.html')


@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)


@app.route('/login', methods=['POST', 'GET'])
def login():
    global loggedAs
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        print("LOGGED")
        print(login, password)
        isNow = False
        myConnection = sqlite3.connect('usersBase.sqlite')
        myCursor = myConnection.cursor()

        login = request.form['login']
        password = request.form['password']
        print(login, password)

        myCursor.execute("SELECT *, oid FROM users")
        records = myCursor.fetchall()

        for el in records:
            if(el[0] == login):
                isNow = True

        if isNow:
            if(login == "admin"):
                dane = records

                length = dane.count
                command = "Admin"
            else:
                for el in records:
                    if(el[0] == login):
                        dane = el

                        length = 1
                command = "Zalogowano"
        else:
            command = "Taki user nie istnieje"
            dane = []
            length = 0
        myConnection.commit()
        # pobieranie danych z bazy

        # zapisywanie zmian
        # kończenie połączenia
        myConnection.close()
        if(command == "Admin"):
            loggedAs = "admin"
            return send_from_directory('client/public', 'index.html')
        elif(command == "Zalogowano"):
            loggedAs = "user"
            return send_from_directory('client/public', 'index.html')
        elif(command == "Taki user nie istnieje"):
            loggedAs = "notLogged"
            return send_from_directory('client/public', 'index.html')
    else:
        login = request.form['login']
        password = request.form['password']
        print("LOGGED")
        print(login, password)
        isNow = False
        myConnection = sqlite3.connect('usersBase.sqlite')
        myCursor = myConnection.cursor()

        login = request.form['login']
        password = request.form['password']
        print(login, password)

        myCursor.execute("SELECT *, oid FROM users")
        records = myCursor.fetchall()

        for el in records:
            if(el[0] == login):
                isNow = True

        if isNow:
            if(login == "admin"):
                dane = records

                length = dane.count
                command = "Admin"
            else:
                for el in records:
                    if(el[0] == login):
                        dane = el

                        length = 1
                command = "Zalogowano"
        else:
            command = "Taki user nie istnieje"
            dane = []
            length = 0
        myConnection.commit()
        # pobieranie danych z bazy

        # zapisywanie zmian
        # kończenie połączenia
        myConnection.close()
        if(command == "Admin"):
            loggedAs = "admin"
            return send_from_directory('client/public', 'index.html')
        elif(command == "Zalogowano"):
            loggedAs = "user"
            return send_from_directory('client/public', 'index.html')
        elif(command == "Taki user nie istnieje"):
            loggedAs = "notLogged"
            return send_from_directory('client/public', 'index.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        print("REGISTERED")
        print(login, password)
        isntNow = True
        myConnection = sqlite3.connect('usersBase.sqlite')
        myCursor = myConnection.cursor()

        login = request.form['login']
        password = request.form['password']
        print(login, password)

        myCursor.execute("SELECT *, oid FROM users")
        records = myCursor.fetchall()

        for el in records:
            if(el[0] == login):
                print(el[0], login)
                isntNow = False

        if isntNow == True:
            myCursor.execute("INSERT INTO users (login,password) VALUES (:login, :password)",
                             {

                                 'login': login,
                                 'password': password

                             })
            command = "Zarejestrowano"
        else:
            command = "Nie udało się zarejestrowąć, dany login już istnieje"
        myConnection.commit()
        # pobieranie danych z bazy

        # zapisywanie zmian
        # kończenie połączenia
        myConnection.close()
        return send_from_directory('client/public', 'index.html')
    else:
        login = request.form['login']
        password = request.form['password']
        print("REGISTERED")
        print(login, password)
        isntNow = True
        myConnection = sqlite3.connect('usersBase.sqlite')
        myCursor = myConnection.cursor()

        login = request.form['login']
        password = request.form['password']
        print(login, password)

        myCursor.execute("SELECT *, oid FROM users")
        records = myCursor.fetchall()

        for el in records:
            if(el[0] == login):
                print(el[0], login)
                isntNow = False

        if isntNow == True:
            myCursor.execute("INSERT INTO users (login,password) VALUES (:login, :password)",
                             {

                                 'login': login,
                                 'password': password

                             })
            command = "Zarejestrowano"
        else:
            command = "Nie udało się zarejestrowąć, dany login już istnieje"
        myConnection.commit()
        # pobieranie danych z bazy

        # zapisywanie zmian
        # kończenie połączenia
        myConnection.close()
        return send_from_directory('client/public', 'index.html')


@app.route('/addArticle', methods=['POST', 'GET'])
def addArticle():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        myConnection = sqlite3.connect('usersBase.sqlite')
        myCursor = myConnection.cursor()
        myCursor.execute("INSERT INTO articles (title,content) VALUES (:title, :content)",
                         {

                             'title': title,
                             'content': content

                         })
        myConnection.commit()
        # pobieranie danych z bazy

        # zapisywanie zmian
        # kończenie połączenia
        myConnection.close()
        return send_from_directory('client/public', 'index.html')
    else:
        title = request.form['title']
        content = request.form['content']
        myConnection = sqlite3.connect('usersBase.sqlite')
        myCursor = myConnection.cursor()
        myCursor.execute("INSERT INTO articles (title,content) VALUES (:title, :content)",
                         {

                             'title': title,
                             'content': content

                         })
        myConnection.commit()
        # pobieranie danych z bazy

        # zapisywanie zmian
        # kończenie połączenia
        myConnection.close()
        return send_from_directory('client/public', 'index.html')


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html', title='404'), 404


@app.errorhandler(500)
def internalServerError(error):
    return render_template('500.html', title='500'), 500


if __name__ == '__main__':
    app.run(debug=True)
