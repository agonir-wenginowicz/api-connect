# app/data.py

# Estrutura de persistência simulada em memória.
# Os dados permanecerão disponíveis enquanto a aplicação estiver em execução.
usuarios = [
    {
        "id": 1,
        "nome": "João da Silva",
        "email": "joao@email.com"
    },
    {
        "id": 2,
        "nome": "Maria Oliveira",
        "email": "maria@email.com"
    }
]


def obter_proximo_id():
    """
    Retorna um novo ID para o próximo usuário cadastrado.
    """
    if not usuarios:
        return 1

    return max(usuario["id"] for usuario in usuarios) + 1