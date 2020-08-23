from flask import request, session, render_template, redirect
from server import app, mysql
import requests

# Página principal, renderiza el template del perfil, si está logeado
@app.route('/')
def index():
    try:
        userid=session['id']
        return render_template('profile.html',userid=userid)
    except:
        return render_template('index.html')