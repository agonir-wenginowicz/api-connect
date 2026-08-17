from flask import Flask
from app.routes import usuarios_bp

# Criação da aplicação Flask
app = Flask(__name__)

# Registro das rotas de usuários
app.register_blueprint(usuarios_bp)


# Inicialização do servidor
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )