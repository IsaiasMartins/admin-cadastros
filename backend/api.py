from flask import Flask, request, jsonify
from flask_cors import CORS
import execute

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def fun_user():
    if request.method == 'GET':
        return execute.exec_list_users()
    elif request.method == 'POST':
        data = request.get_json()
        if data is None or not all(key in data for key in ('nome', 'rg', 'cpf', 'data_nascimento', 'data_admissao', 'funcao')):
            return jsonify({"message": "request body fora do padrão"}), 400
        return execute.exec_create_user(data['nome'], data['rg'], data['cpf'], data['data_nascimento'], data['data_admissao'], data['funcao']), 201
    elif request.method == 'PUT':
        data = request.get_json()
        if data is None or not all(key in data for key in ('id', 'nome', 'rg', 'cpf', 'data_nascimento', 'data_admissao', 'funcao')):
            return jsonify({"message": "request body fora do padrão"}), 400
        return execute.exec_edit_user(data['id'], data['nome'], data['rg'], data['cpf'], data['data_nascimento'], data['data_admissao'], data['funcao'])
    elif request.method == 'DELETE':
        data = request.get_json()
        if data is None or 'id' not in data:
            return jsonify({"message": "request body fora do padrão"}), 400
        return execute.exec_delete_user(data['id'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
