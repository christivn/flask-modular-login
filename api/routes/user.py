from flask import request, jsonify, abort
from server import app, mysql


# Info de mediante nick de usuario
@app.route('/user/<nick>', methods=['GET'])
def user_info(nick):
    try:
        cur = mysql.connection.cursor()
        cur.execute("select * from usuarios inner join userinfo on usuarios.id=userinfo.id where usuarios.nick='"+nick+"' LIMIT 1")
        resultado = cur.fetchall()
        cur.close()

        return jsonify({ 'id': resultado[0][0], 'nick': resultado[0][1], 'url_foto':'', 'bio':'', 'pais':'', 'fecha_registro':resultado[0][6].strftime("%Y/%m/%d"), 'fecha_ultima_conexion':resultado[0][7].strftime("%Y/%m/%d %H:%M:%S") }), 200
    except Exception as e:
        abort(400)



# Elimina el usuario de la base de datos
# Get rid of specified user
@app.route('/user/<nick>', methods=['DELETE'])
def delete_user(nick):
    try:
        cur = mysql.connection.cursor()
        res = cur.execute("delete from usuarios where id='"+id+"'")
        res2 = cur.execute("delete from userinfo where id='"+id+"'")
        cur.execute("delete from usuarios_proyectos where id_usuario='"+id+"'")
        if res and res2:
            mysql.connection.commit()
            return jsonify({ 'msg':'User successfully deleted'}), 200
        else: return jsonify({ 'msg':'User doesnt exist' }), 404
    except Exception as e:
        abort(400)



# Proyectos de un usuario (en los que participa o a participado)
@app.route('/user/proyects/<nick>', methods=['GET'])
def user_proyects(nick):
    try:
        cur = mysql.connection.cursor()
        cur.execute("select * from usuarios inner join usuarios_proyectos on usuarios.id=usuarios_proyectos.id_usuario where usuarios.nick='"+nick+"'")
        resultado = cur.fetchall()
        cur.close()

        json="{ 'id_proyect': '', 'id_usuario': '', 'fecha_entrada':'', 'fecha_salida':'' }"
        return jsonify(json), 200
    except Exception as e:
        abort(400)