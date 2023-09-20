from flask import Flask, jsonify, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'

@app.route('/ping')
def ping():
    return jsonify({"message": "Pong"})

@app.route('/usuario/<string:nombre>')
def usuario_by_name(nombre):
    return jsonify({"name": nombre})

@app.route('/usuario/<int:id>')
def usuario_by_id(id):
    return jsonify({"id": id})

@app.route('/<path:nombre>')
def no_hacer(nombre):
    return nombre

# GET todos los 'recursos'
@app.route('/recurso', methods = ['GET'])
def get_recursos():
    return jsonify({"data": "lista de todos los items de este recurso"})

# POST nuevo 'recurso'
@app.route('/recurso', methods = ['POST'])# se puede simplificar con "@app.post('/recurso')"
def post_recurso():
    print(request.get_json())
    body = request.get_json()
    name = body["name"] # es lo mismo que "request.get_json()["name"]"
    modelo = body["modelo"]
    # insertar en la Base de Datos
    return jsonify({"recurso":{
         "name": name,
         "modelo": modelo
         }})

# GET de 'recurso' por id
@app.route('/recurso/<int:id>', methods = ['GET'])# se puede simplificar con "@app.get('/recurso/<int:id>')"
def get_recurso_by_id(id):
    # buscar en la Base de Datos un registro con ese id
    return jsonify({"recurso":{
        "name": "nombre correspondiente a ese id",
        "modelo": "modelo correspondiente a ese id"
        }})








if __name__ == '__main__':
    app.run(debug=True, port=5000)

