from flask import request, session, render_template, redirect
from server import app, mysql
import requests


# Registro de nuevos usuarios
@app.route('/register', methods=['GET'])
def register():
    try:
        userid=session['id']
        return redirect('/', code=302)
    except:
        return render_template('register.html')



@app.route('/register', methods=['POST'])
def register_form():
    try:
        userid=session['id']
        return redirect('/', code=302)
    except:
        return render_template('register.html')