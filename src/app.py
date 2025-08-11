# Importando Flask
from flask import Flask, jsonify, request

# Creando la instancia de Flask
app = Flask(__name__)

# Configurar la aplicacion
app.config['DEBUG'] = True

# Definiendo nuestra ruta principal
@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def main():
    
    data = {
        "message": "Hola mundo desde Flask"
    }
    
    return jsonify(data), 200

# Definiendo una ruta con parametros en la url
# ejemplo: /users/1
@app.route('/users/<int:id>', methods=['GET'])
def get_params_url(id):
    
    data = {
        "user": id
    }
    
    return  jsonify(data), 200

# Definiendo una ruta con parametros en la url a traves de query
# ejemplo: /users?limit=100
@app.route('/users', methods=['GET'])
def get_params_query():
    
    params = request.args
    
    return jsonify(params), 200

# Definiendo una ruta con informacion en el body
# ejemplo: /users/create
@app.route('/users/create', methods=['POST'])
def get_info_body():
    
    # recibir informacion sin formato
    # info = request.data
    
    # recibir informacion en formato json
    # info = request.get_json()
    # print(info["name"])
    # print(info["lastname"])
    
    # recibir informacion en formato json y acceder a cada individualmente
    # name = request.json.get("name")
    # lastname = request.json.get("lastname")
    # print(name)
    # print(lastname)
    
    # recibir informacion en formato formulario con archivos (opcional)
    name = request.form["name"]
    lastname = request.form["lastname"]
    
    # recibir informacion tipo archivo
    file = request.files["cv"]
    
    print(name)
    print(lastname)
    print(file.filename)
    
    #print(info)
    
    return jsonify({"message": "Data"}), 200
        
    
    


# Iniciando nuestra aplicacion
if __name__ == '__main__':
    app.run()