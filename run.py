from server import app

#Lanzar
print("\033[33m")
if __name__ == '__main__':
    app.run(port=5000, debug=True, threaded=True)
print("\033[0m")