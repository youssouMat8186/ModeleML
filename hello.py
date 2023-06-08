from flask import Flask, url_for,abort,redirect

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def hello_world():
    age = 18
    print(age)
    return 'hello world ! <img src="' + url_for('static',filename='flaskImage.png')+'"alt="logo flask" >'
@app.route("/profil/<string:username>/<int:age>")
def profil(username,age):
    return 'Bonjour '+username+' vous avez '+str(age) +' ans'

@app.route('/contact')
def contact1():
    return 'Page contact <a href= " '+ url_for('hello_world') + '">Retour acceuil </a>   '

@app.route('/protected/<int:code>')
def protected (code):
    if code ==1234:
        return 'Accés autorisé'
    else:
        #abort(404)
        return redirect(url_for('user_login'))


@app.route('/login')
def user_login():
    return 'Merci de vous identifier'