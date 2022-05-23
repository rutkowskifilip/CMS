from asyncio.windows_events import NULL

from tkinter.tix import Tree
from xml.dom.expatbuilder import parseString
from click import command
from flask import Flask, jsonify, render_template, request, flash, redirect, session, send_from_directory, url_for

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
import sqlite3
import random
import json

app = Flask(__name__)

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
            UNIQUE(link, content)
            )""")
myCursor.execute("""CREATE TABLE IF NOT EXISTS comments (
            author text,
            content text,
            ID integer primary key autoincrement
            )""")
myCursor.execute("""CREATE TABLE IF NOT EXISTS menuElements (
            name text,
            url text,
            ID integer primary key autoincrement,
            UNIQUE(name, url)
            )""")

myCursor.execute("""CREATE TABLE IF NOT EXISTS article (
            content text,
            ID integer primary key autoincrement,
            UNIQUE(content)
            )""")

myCursor.execute("""CREATE TABLE IF NOT EXISTS gallery (
            link text,
            ID integer primary key autoincrement,
            UNIQUE(link)
            )""")
myCursor.execute("""CREATE TABLE IF NOT EXISTS time (
            time integer,
            ID integer primary key autoincrement,
            UNIQUE(time)
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
myCursor.execute(
    "INSERT OR IGNORE INTO menuElements (name,url) VALUES ('Elem', 'xdddddd')")
myCursor.execute(
    "INSERT OR IGNORE INTO article (content) VALUES ('The cat (Felis catus) is a domestic species of small carnivorous mammal.It is the only domesticated species in the family Felidae and is oftenreferred to as the domestic cat to distinguish it from the wild members of the family. A cat can either be a house cat, a farm cat or a feral cat;the latter ranges freely and avoids human contact. Domestic cats are valued by humans for companionship and their ability to kill rodents. About 60 cat breeds are recognized by various cat registries. The cat is similar in anatomy to the other felid species: it has a strong flexible body, quick reflexes, sharp teeth and retractable claws adapted to killing small prey. Its night vision and sense of smell are well developed. Cat communication includes vocalizations like meowing, purring, trilling, hissing, growling and grunting as well as cat-specific body language. A predator that is most active at dawn and dusk (crepuscular), the cat is a solitary hunter but a social species. It can hear sounds too faint or too high in frequency for human ears, such as those made by mice and other small mammals. Cats also secrete and perceive pheromones.')")
myCursor.execute(
    "INSERT OR IGNORE INTO gallery (link) VALUES ('https://tueuropa.pl/uploads/articles_files/2021/11/05/6e7f9516-1948-d9e8-ca22-00007380aca5.jpg')")
myCursor.execute(
    "INSERT OR IGNORE INTO time (time) VALUES ('1')")
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
userLogin = ""
timeSlider = 5
article = "The cat (Felis catus) is a domestic species of small carnivorous mammal.It is the only domesticated species in the family Felidae and is oftenreferred to as the domestic cat to distinguish it from the wild members of the family. A cat can either be a house cat, a farm cat or a feral cat;the latter ranges freely and avoids human contact. Domestic cats are valued by humans for companionship and their ability to kill rodents. About 60 cat breeds are recognized by various cat registries. The cat is similar in anatomy to the other felid species: it has a strong flexible body, quick reflexes, sharp teeth and retractable claws adapted to killing small prey. Its night vision and sense of smell are well developed. Cat communication includes vocalizations like meowing, purring, trilling, hissing, growling and grunting as well as cat-specific body language. A predator that is most active at dawn and dusk (crepuscular), the cat is a solitary hunter but a social species. It can hear sounds too faint or too high in frequency for human ears, such as those made by mice and other small mammals. Cats also secrete and perceive pheromones."
photos = []
articles = []
comments = []
headerElements = []
users = []


@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')


@app.route("/loggedAs")
def loggedas():
    return str(loggedAs)


@app.route("/userlogin")
def userlogin():
    return str(userLogin)


@app.route("/getarticle")
def articlecontent():

    return str(article)


@app.route('/getgallery')
def getGallery():
    global article
    myConnection = sqlite3.connect('usersBase.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT *, oid FROM gallery")
    records = myCursor.fetchall()

    return jsonify(records)


@app.route('/settime', methods=['GET', 'POST'])
def setTime():
    global timeSlider
    setTime = str(request.form["sliderChangeTime"])
    timeSlider = str(setTime)
    myConnection = sqlite3.connect('usersBase.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("UPDATE time SET time ='" + str(setTime) + "' WHERE ID = 1")
    myConnection.commit()
    return send_from_directory('client/public', 'index.html')


@app.route('/gettime')
def getTime():
    return str(timeSlider)


@app.route("/addgallery", methods=['GET', 'POST'])
def addgallery():
    print("DZIAŁA")
    if request.method == 'POST':
        link = request.form['url']
        print(link)
        myConnection = sqlite3.connect('usersBase.sqlite')
        myCursor = myConnection.cursor()
        if(link != ""):
            myCursor.execute("INSERT  INTO gallery (link) VALUES (:link)",
                             {

                                 'link': link
                             })
            myConnection.commit()
        return send_from_directory('client/public', 'index.html')
    else:
        link = request.form['url']
        print(link)
        myConnection = sqlite3.connect('usersBase.sqlite')
        myCursor = myConnection.cursor()
        if(link != ""):
            myCursor.execute("INSERT INTO gallery (link) VALUES (:link)",
                             {

                                 'link': link
                             })
            myConnection.commit()
        return send_from_directory('client/public', 'index.html')


@app.route("/editarticle", methods=['POST'])
def editarticle():
    req = request.get_json()
    article = req["content"]
    myConnection = sqlite3.connect('usersBase.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("UPDATE article SET content ='" +
                     req["content"] + "' WHERE ID = " + 1)
    myConnection.commit()


@app.route("/photosbase")
def photosBase():
    global photos
    photos = []
    myConnection = sqlite3.connect('usersBase.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT *, oid FROM photos")
    records = myCursor.fetchall()

    for el in records:
        photos.append({"link": el[0], "content": el[1]})

    return jsonify(records)


@app.route("/usersbase")
def usersBase():
    global users
    users = []
    myConnection = sqlite3.connect('usersBase.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT *, oid FROM users")
    records = myCursor.fetchall()

    for el in records:
        users.append({"link": el[0], "content": el[1]})

    return jsonify(records)


@app.route("/articlesbase")
def articlesBase():
    global articles
    articles = []
    myConnection = sqlite3.connect('usersBase.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT *, oid FROM articles")
    records = myCursor.fetchall()

    for el in records:
        photos.append({"link": el[0], "content": el[1]})

    return jsonify(records)


@app.route("/getcomments")
def getComments():
    global comments
    comments = []
    myConnection = sqlite3.connect('usersBase.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT *, oid FROM comments")
    records = myCursor.fetchall()

    for el in records:
        comments.append({"author": el[0], "content": el[1]})

    return jsonify(records)


@app.route("/getelements")
def getElements():
    global headerElements
    headerElements = []
    myConnection = sqlite3.connect('usersBase.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT *, oid FROM menuElements")
    records = myCursor.fetchall()

    for el in records:
        headerElements.append({"name": el[0], "url": el[1]})

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
    global loggedAs, userLogin
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
            if(el[0] == login and el[1] == password):
                isNow = True

        if isNow:
            if(login == "admin"):
                dane = records

                length = dane.count
                command = "Admin"
                userLogin = "admin"
            else:
                for el in records:
                    if(el[0] == login):
                        dane = el

                        length = 1
                command = "Zalogowano"
                userLogin = login
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
            if(el[0] == login and el[1] == password):
                isNow = True

        if isNow:
            if(login == "admin"):
                dane = records

                length = dane.count
                command = "Admin"
                userLogin = "Admin"
            else:
                for el in records:
                    if(el[0] == login):
                        dane = el

                        length = 1
                command = "Zalogowano"
                userLogin = login
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

        if (isntNow == True and login != "" and password != ""):
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

        if (isntNow == True and login != "" and password != ""):
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


@app.route('/addarticle', methods=['POST', 'GET'])
def addArticle():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        myConnection = sqlite3.connect('usersBase.sqlite')
        myCursor = myConnection.cursor()
        if(title != "" and content != ""):
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
        if(title != "" and content != ""):
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


@app.route('/addelement', methods=['POST', 'GET'])
def addelement():
    if request.method == 'POST':
        name = request.form['name']
        url = request.form['url']
        print("added")
        print(name, url)

        myConnection = sqlite3.connect('usersBase.sqlite')
        myCursor = myConnection.cursor()
        if(name != "" and url != ""):
            myCursor.execute("INSERT INTO menuElements (name,url) VALUES (:name, :url)",
                             {

                                 'name': name,
                                 'url': url

                             })
            command = "Zarejestrowano"
            # else:
            command = "Nie udało się zarejestrowąć, dany login już istnieje"
            myConnection.commit()
            # pobieranie danych z bazy

            # zapisywanie zmian
            # kończenie połączenia
            myConnection.close()
        return send_from_directory('client/public', 'index.html')
    else:
        name = request.form['name']
        url = request.form['url']
        print("added")
        print(name, url)

        myConnection = sqlite3.connect('usersBase.sqlite')
        myCursor = myConnection.cursor()
        if(name != "" and url != ""):
            myCursor.execute("INSERT INTO menuElements (name,url) VALUES (:name, :url)",
                             {

                                 'name': name,
                                 'url': url

                             })
            command = "Zarejestrowano"
            # else:
            command = "Nie udało się zarejestrowąć, dany login już istnieje"
            myConnection.commit()
            # pobieranie danych z bazy

            # zapisywanie zmian
            # kończenie połączenia
            myConnection.close()
        return send_from_directory('client/public', 'index.html')


@app.route('/addphoto', methods=['POST', 'GET'])
def addphoto():
    if request.method == 'POST':
        link = request.form['link']
        content = request.form['content']
        print("added")
        print(link, content)
        if(link != "" and content != ""):
            myConnection = sqlite3.connect('usersBase.sqlite')
            myCursor = myConnection.cursor()

            myCursor.execute("INSERT INTO photos (link,content) VALUES (:link, :content)",
                             {

                                 'link': link,
                                 'content': content

                             })
            command = "Zarejestrowano"
            # else:
            command = "Nie udało się zarejestrowąć, dany login już istnieje"
            myConnection.commit()
        # pobieranie danych z bazy

        # zapisywanie zmian
        # kończenie połączenia
            myConnection.close()
        return send_from_directory('client/public', 'index.html')
    else:
        link = request.form['link']
        content = request.form['content']
        print("added")
        print(link, content)
        if(link != "" and content != ""):
            myConnection = sqlite3.connect('usersBase.sqlite')
            myCursor = myConnection.cursor()

            myCursor.execute("INSERT INTO photos (link,content) VALUES (:link, :content)",
                             {

                                 'link': link,
                                 'content': content

                             })
            command = "Zarejestrowano"
            # else:
            command = "Nie udało się zarejestrowąć, dany login już istnieje"
            myConnection.commit()
        # pobieranie danych z bazy

        # zapisywanie zmian
        # kończenie połączenia
        myConnection.close()
        return send_from_directory('client/public', 'index.html')


@app.route('/addcomment', methods=['POST', 'GET'])
def addComment():
    if request.method == 'POST':
        text = request.form['comment']

        if text != "":
            myConnection = sqlite3.connect('usersBase.sqlite')
            myCursor = myConnection.cursor()
            myCursor.execute("INSERT INTO comments (author,content) VALUES (:author, :text)",
                             {

                                 'author': userLogin,
                                 'text': text

                             })
            myConnection.commit()
        # pobieranie danych z bazy

        # zapisywanie zmian
        # kończenie połączenia
        myConnection.close()
        return send_from_directory('client/public', 'index.html')
    else:
        text = request.form['comment']

        myConnection = sqlite3.connect('usersBase.sqlite')
        myCursor = myConnection.cursor()
        myCursor.execute("INSERT INTO comments (author,text) VALUES (:author, :text)",
                         {

                             'author': userLogin,
                             'text': text

                         })
        myConnection.commit()
        # pobieranie danych z bazy

        # zapisywanie zmian
        # kończenie połączenia
        myConnection.close()
        return send_from_directory('client/public', 'index.html')


@app.post("/deleteuser")
def deleteUser():
    userToDel = request.form["delLogin"]
    myConnection = sqlite3.connect('usersBase.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT *, oid FROM users")
    records = myCursor.fetchall()

    for el in records:
        if(el[0] == userToDel):
            isTrue = True

    if(userToDel != "admin" and isTrue == True and userToDel != ""):
        sql = "DELETE FROM users WHERE = '" + userToDel + "'"
        myConnection = sqlite3.connect('usersBase.sqlite')
        myCursor = myConnection.cursor()
        myCursor.execute("DELETE FROM users WHERE login = '" + userToDel + "'")
        myConnection.commit()
        # pobieranie danych z bazy

        # zapisywanie zmian
        # kończenie połączenia
        myConnection.close()

        return send_from_directory('client/public', 'index.html')
    else:
        return send_from_directory('client/public', 'index.html')


@app.post("/deleteelement")
def deleteElement():
    nameToDel = request.form["delName"]
    textToDel = request.form["delText"]
    myConnection = sqlite3.connect('usersBase.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT *, oid FROM menuElements")
    records = myCursor.fetchall()

    for el in records:
        if(el[0] == nameToDel and el[1] == textToDel):
            isTrue = True

    if(isTrue == True):
        myConnection = sqlite3.connect('usersBase.sqlite')
        myCursor = myConnection.cursor()
        myCursor.execute("DELETE FROM menuElements WHERE name = '" +
                         nameToDel + "' AND url = '" + textToDel + "'")
        myConnection.commit()
        # pobieranie danych z bazy

        # zapisywanie zmian
        # kończenie połączenia
        myConnection.close()

        return send_from_directory('client/public', 'index.html')
    else:
        return send_from_directory('client/public', 'index.html')


@app.post("/deletephoto")
def deletePhoto():
    delLink = request.form["delLink"]
    delContent = request.form["delContent"]
    myConnection = sqlite3.connect('usersBase.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT *, oid FROM menuElements")
    records = myCursor.fetchall()

    for el in records:
        if(el[0] == delLink and el[1] == delContent):
            isTrue = True

    isTrue = True

    if(isTrue == True):
        myConnection = sqlite3.connect('usersBase.sqlite')
        myCursor = myConnection.cursor()
        myCursor.execute("DELETE FROM photos WHERE link = '" +
                         delLink + "' AND content = '" + delContent + "'")
        myConnection.commit()
        # pobieranie danych z bazy

        # zapisywanie zmian
        # kończenie połączenia
        myConnection.close()

        return send_from_directory('client/public', 'index.html')
    else:
        return send_from_directory('client/public', 'index.html')


@app.post('/edituser')
def editUserBase():
    editLogin = request.form["editLogin"]
    editPassword = request.form["editPassword"]
    newLogin = request.form["newLogin"]
    newPassword = request.form["newPassword"]

    myConnection = sqlite3.connect('usersBase.sqlite')
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT *, oid FROM users")
    records = myCursor.fetchall()

    for el in records:
        if(el[0] == editLogin and el[1] == editPassword):
            isTrue = True

    if(isTrue == True):
        myConnection = sqlite3.connect('usersBase.sqlite')
        myCursor = myConnection.cursor()
        myCursor.execute("UPDATE users SET login ='" + newLogin + "', password ='" +
                         newPassword + "' WHERE login = '" + editLogin + "' AND password = '" + editPassword + "'")
        myConnection.commit()
        # pobieranie danych z bazy

        # zapisywanie zmian
        # kończenie połączenia
        myConnection.close()

        return send_from_directory('client/public', 'index.html')
    else:
        return send_from_directory('client/public', 'index.html')


@app.route('/editPhoto')
def editPhoto():
    req = request.get_json()
    # ID = 0
    # myConnection = sqlite3.connect('usersBase.sqlite')
    # myCursor = myConnection.cursor()

    # myCursor.execute("SELECT *, oid FROM users")
    # records = myCursor.fetchall()

    # for el in records:
    #     if(el[0] == editLogin and el[1] == editPassword):
    #         isTrue = True
    print(req)
    return 0


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html', title='404'), 404


@app.errorhandler(500)
def internalServerError(error):
    return render_template('500.html', title='500'), 500


if __name__ == '__main__':
    app.run(debug=True)
