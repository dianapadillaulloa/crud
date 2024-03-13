from flask import Flask, request, jsonify
from conexion import connection_mysql
import pymysql

app = Flask(__name__)

@app.route('/crear', methods=["POST"])
def create():
    data = request.get_json()
    connection = connection_mysql()
    with connection:
        with connection.cursor() as cursor:
            sql= "INSERT INTO users (usuario,password) VALUES (%s,%s)"
            cursor.execute(sql, (data['usuario'], data['password']))
        connection.commit()

    return jsonify({
        'message': 'Creacion exitosa'
    }), 201


@app.route('/leer', methods=["POST"])
def list():
    connection = connection_mysql()

    with connection.cursor() as cursor:

        sql = 'SELECT * FROM users'
        cursor.execute(sql)

        result = cursor.fetchall()

        return jsonify({
            'data': result
        }), 200


@app.route('/edit/<string:id>', methods=['POST'])
def upadte_data(id):

    data = request.get_json()
    connection = connection_mysql()

    with connection:
        with connection.cursor() as cursor:

            sql= "UPDATE users SET usuario = %s, password = %s WHERE id = %s"
            cursor.execute(sql, (data['id'], data['usuario'], data['password']))

        connection.commit()


    return jsonify({'message': 'Usuario actualizado correctamente'})



@app.route('/delete/<string:id>')
def delete(id):

    data = request.get_json()
    connection = connection_mysql()

    with connection:
        with connection.cursor() as cursor:

            sql= "DELETE FROM users WHERE id = %s"
            cursor.execute(sql, data['id'])

        connection.commit()

    return jsonify({'message': 'Usuario eliminado correctamente'})


if __name__ == '__main__':
    app.run(debug=True)

