from flask import Flask
from flask_mysqldb import MySQL
import os

# inicializar Flask
app = Flask(__name__)
app.secret_key = '123456'

# Deshabilitar Console Logs
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'b2b'
mysql = MySQL(app)


os.system('cls' if os.name == 'nt' else 'clear')
print("""
\033[34m     ___       ______    __ \033[0m 
\033[34m    /   \     |   _  \  |  |\033[0m 
\033[34m   /  ^  \    |  |_)  | |  |\033[0m 
\033[34m  /  /_\  \   |   ___/  |  |\033[0m 
\033[34m /  _____  \  |  |      |  |\033[0m \033[36m[v 1.0]\033[0m
\033[34m/__/     \__\ | _|      |__|\033[0m \033[36m(By: christivn)\033[0m

--------------------------------------------
""")


# Rutas
@app.route("/")
def index():
    return """<pre>
         ___       ______    __ 
        /   \     |   _  \  |  |
       /  ^  \    |  |_)  | |  |
      /  /_\  \   |   ___/  |  |
     /  _____  \  |  |      |  | 
    /__/     \__\ | _|      |__| [v 1.0]

    --------------------------------------------

    < Author >
    Christian Ramos Ortiz <b>(christivn)</b></pre>"""


print("\033[92m",end="")
import routes
print("\033[0m",end="")
