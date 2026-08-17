# app/routes.py

from flask import Blueprint, request, jsonify
from app.data import usuarios, obter_proximo_id

usuarios_bp = Blueprint("usuarios", __name__)


# ==========================================
# Função auxiliar para validar os dados
# ==========================================
def validar_usuario(dados):
    """
    Valida os dados recebidos para criação ou
    atualização de um usuário.
    """

    # Verifica se o corpo contém um JSON válido
    if not isinstance(dados, dict):
        return "O corpo da requisição deve conter um objeto JSON."

    # Verifica a existência dos campos obrigatórios
    if "nome" not in dados:
        return "O campo 'nome' é obrigatório."

    if "email" not in dados:
        return "O campo 'email' é obrigatório."

    # Verifica se os campos são strings
    if not isinstance(dados["nome"], str):
        return "O campo 'nome' deve ser um texto."

    if not isinstance(dados["email"], str):
        return "O campo 'email' deve ser um texto."

    # Remove espaços extras para realizar a validação
    nome = dados["nome"].strip()
    email = dados["email"].strip()

    # Verifica se os campos estão vazios
    if not nome:
        return "O campo 'nome' não pode estar vazio."

    if not email:
        return "O campo 'email' não pode estar vazio."

    # Validação básica do formato do e-mail
    if "@" not in email or "." not in email.split("@")[-1]:
        return "O campo 'email' deve possuir um formato válido."

    # Não foram encontradas inconsistências
    return None


# ==========================================
# POST /usuarios
# Cadastrar usuário
# ==========================================
@usuarios_bp.route("/usuarios", methods=["POST"])
def cadastrar_usuario():

    # Verifica se a requisição possui JSON
    if not request.is_json:
        return jsonify({
            "error": "A requisição deve utilizar o formato JSON."
        }), 400

    dados = request.get_json()

    # Executa a validação
    erro = validar_usuario(dados)

    if erro:
        return jsonify({
            "error": erro
        }), 400

    # Cria o novo usuário
    novo_usuario = {
        "id": obter_proximo_id(),
        "nome": dados["nome"].strip(),
        "email": dados["email"].strip()
    }

    # Adiciona o usuário à estrutura em memória
    usuarios.append(novo_usuario)

    # Retorno padronizado
    return jsonify({
        "data": novo_usuario
    }), 201


# ==========================================
# GET /usuarios
# Listar todos os usuários
# ==========================================
@usuarios_bp.route("/usuarios", methods=["GET"])
def listar_usuarios():

    return jsonify({
        "data": usuarios
    }), 200


# ==========================================
# GET /usuarios/<id>
# Buscar usuário pelo ID
# ==========================================
@usuarios_bp.route("/usuarios/<int:id>", methods=["GET"])
def buscar_usuario(id):

    for usuario in usuarios:
        if usuario["id"] == id:
            return jsonify({
                "data": usuario
            }), 200

    return jsonify({
        "error": "Usuário não encontrado."
    }), 404


# ==========================================
# PUT /usuarios/<id>
# Atualizar usuário
# ==========================================
@usuarios_bp.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):

    # Verifica se a requisição possui JSON
    if not request.is_json:
        return jsonify({
            "error": "A requisição deve utilizar o formato JSON."
        }), 400

    dados = request.get_json()

    # Valida os dados recebidos
    erro = validar_usuario(dados)

    if erro:
        return jsonify({
            "error": erro
        }), 400

    # Localiza o índice do usuário
    indice_usuario = None

    for indice, usuario in enumerate(usuarios):
        if usuario["id"] == id:
            indice_usuario = indice
            break

    # Usuário não encontrado
    if indice_usuario is None:
        return jsonify({
            "error": "Usuário não encontrado."
        }), 404

    # Atualiza o usuário mantendo seu ID
    usuario_atualizado = {
        "id": id,
        "nome": dados["nome"].strip(),
        "email": dados["email"].strip()
    }

    usuarios[indice_usuario] = usuario_atualizado

    # Retorno padronizado
    return jsonify({
        "data": usuario_atualizado
    }), 200


# ==========================================
# DELETE /usuarios/<id>
# Excluir usuário
# ==========================================
@usuarios_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def excluir_usuario(id):

    # Localiza o usuário
    indice_usuario = None

    for indice, usuario in enumerate(usuarios):
        if usuario["id"] == id:
            indice_usuario = indice
            break

    # Usuário não encontrado
    if indice_usuario is None:
        return jsonify({
            "error": "Usuário não encontrado."
        }), 404

    # Remove o usuário
    usuarios.pop(indice_usuario)

    # 204 não possui corpo de resposta
    return "", 204