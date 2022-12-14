from flask import Flask, make_response, jsonify, request
from flask_cors import CORS
from model.User import User as user

app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def root():
    return "<h1>API de Usuários</h1>" 

@app.route('/usuarios', methods=['GET'])
def get_users():
    return make_response(jsonify(
        user.getAll()))
        

@app.route('/usuarios/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return make_response(jsonify(
        user.getById(user_id)))

@app.route('/usuarios', methods=['POST'])
def create_user():
    user = request.json
    user.create(user)
    return make_response(jsonify(
        mensagem='Usuario cadastrado com sucesso.',
        user=user))

@app.route('/usuarios/<int:user_id>', methods=['DELETE'])
def delete_users(user_id: int):
    user.delete(user_id)
    return make_response(jsonify(
        mensagem='Usuario excluido com sucesso.',
        user=user.getAll()))
    
@app.route('/usuarios/<int:user_id>', methods=['PUT'])
def update(user_id: int):
    body = request.json
    user.update(user_id, body)
    return make_response(jsonify(
        mensagem='Usuario atualizado com sucesso.',
        user=user.getById(user_id)))
