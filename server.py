from flask import Flask
from flask_mysqldb import MySQL
import os

# inicializar Flask
app = Flask(__name__)
app._static_folder = "static"
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
print("""\033[93m
         _          _           _            _           _       
        /\ \       /\ \        /\ \         /\ \     _  /\ \     
       /  \ \     /  \ \      /  \ \       /  \ \   /\_\\_\ \    
      / /\ \ \   / /\ \ \    / /\ \ \     / /\ \ \_/ / //\__ \   
     / / /\ \_\ / / /\ \_\  / / /\ \ \   / / /\ \___/ // /_ \ \  
    / /_/_ \/_// / /_/ / / / / /  \ \_\ / / /  \/____// / /\ \ \ 
   / /____/\  / / /__\/ / / / /   / / // / /    / / // / /  \/_/ 
  / /\____\/ / / /_____/ / / /   / / // / /    / / // / /        
 / / /      / / /\ \ \  / / /___/ / // / /    / / // / /         
/ / /      / / /  \ \ \/ / /____\/ // / /    / / //_/ /          
\/_/       \/_/    \_\/\/_________/ \/_/     \/_/ \_\/           
                      (By: Christivn)                                     
----------------------------------------------------------------\033[0m
""")

# Rutas
print("\033[92m",end="")
import routes
print("\033[0m",end="")
