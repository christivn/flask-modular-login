from flask import request, session, render_template, redirect
from server import app, mysql
import requests


# Página del login
@app.route('/login', methods=['GET'])
def login():
    try:
        userid=session['id']
        return redirect('/', code=302)
    except:
        return render_template('login.html')



# POST formulario del login
@app.route('/login', methods=['POST'])
def login_post():
    try:
        userid=session['id']
        return render_template('profile.html',userid=userid)
    except:
        try:
            nick_email = request.form['nick-email']
            password = request.form['password']

            url = 'http://127.0.0.1:3000/auth/login'
            obj = {'nick': nick_email, 'password': password}
            r = requests.post(url, data=obj)

            if r.status_code==200:
                session['nick']=nick_email
                return render_template('profile.html',userid=userid)
            else:
                return redirect("/login", code=302)
        except Exception as e:
            print(e)
            return redirect("/login", code=302)



# Logout
@app.route('/logout', methods=['GET'])
def logout():
    try:
        session.pop('userid', None)
        return redirect("/", code=302)
    except:
        return redirect("/", code=302)