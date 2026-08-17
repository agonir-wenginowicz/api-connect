# API de Gerenciamento de Usuários

API REST desenvolvida em **Python com Flask** como parte da atividade prática da disciplina de **Desenvolvimento Back-End**.

O projeto representa um **MVP (Produto Mínimo Viável)** de uma API para gerenciamento de usuários, permitindo realizar operações de criação, consulta, atualização e exclusão de registros.

## 1. Tecnologias utilizadas

* Python
* Flask
* Flask-CORS
* python-dotenv
* pytest
* HTTP/REST
* JSON

## 2. Objetivo

O objetivo da aplicação é disponibilizar uma API REST capaz de fornecer ao front-end operações básicas para gerenciamento de usuários.

Cada usuário possui:

* `id`
* `nome`
* `email`

Para simplificar o desenvolvimento do MVP, os dados são armazenados temporariamente em uma estrutura **em memória**, não sendo utilizado um banco de dados neste momento.

## 3. Estrutura do projeto

```text
api-usuarios/
│
├── app/
│   ├── __init__.py
│   ├── data.py
│   └── routes.py
│
├── tests/
│
├── venv/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── run.py
```

### Principais arquivos

**`run.py`**

Ponto de entrada da aplicação. Responsável por criar/inicializar o servidor Flask e definir a porta de execução.

**`app/data.py`**

Responsável pela estrutura de armazenamento dos usuários em memória e pela geração dos IDs.

**`app/routes.py`**

Contém as rotas e os controladores responsáveis pelas operações da API.

**`tests/`**

Diretório destinado aos testes automatizados da aplicação.

**`requirements.txt`**

Lista as dependências necessárias para executar o projeto.

**`.gitignore`**

Define arquivos e diretórios que não devem ser enviados para o controle de versão Git.

## 4. Instalação

### Pré-requisitos

É necessário possuir o Python instalado na máquina.

Para verificar a instalação:

```bash
python --version
```

No Linux ou macOS, pode ser necessário utilizar:

```bash
python3 --version
```

### Clonar o projeto

Caso o projeto esteja hospedado em um repositório Git:

```bash
git clone URL_DO_REPOSITORIO
```

Depois:

```bash
cd api-usuarios
```

## 5. Criar o ambiente virtual

No Windows:

```bash
python -m venv venv
```

Ativação no Prompt de Comando:

```bash
venv\Scripts\activate
```

Ativação no PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

## 6. Instalar as dependências

Com o ambiente virtual ativado:

```bash
pip install -r requirements.txt
```

Caso seja necessário instalar as dependências manualmente:

```bash
pip install Flask flask-cors python-dotenv pytest
```

Depois, pode-se atualizar o arquivo de dependências:

```bash
pip freeze > requirements.txt
```

## 7. Executar a aplicação

Com o ambiente virtual ativado, execute:

```bash
python run.py
```

O servidor será iniciado na porta `5000`.

A API estará disponível em:

```text
http://localhost:5000
```

## 8. Endpoints disponíveis

| Método | Endpoint         | Descrição                | Status          |
| ------ | ---------------- | ------------------------ | --------------- |
| GET    | `/usuarios`      | Lista todos os usuários  | 200             |
| GET    | `/usuarios/<id>` | Busca um usuário pelo ID | 200 / 404       |
| POST   | `/usuarios`      | Cadastra um novo usuário | 201 / 400       |
| PUT    | `/usuarios/<id>` | Atualiza um usuário      | 200 / 400 / 404 |
| DELETE | `/usuarios/<id>` | Remove um usuário        | 204 / 404       |

## 9. Cadastro de usuário

Para cadastrar um usuário, deve ser realizada uma requisição:

```http
POST /usuarios
Content-Type: application/json
```

Com o seguinte corpo:

```json
{
    "nome": "Carlos Santos",
    "email": "carlos@email.com"
}
```

Resposta de sucesso:

```json
{
    "data": {
        "id": 3,
        "nome": "Carlos Santos",
        "email": "carlos@email.com"
    }
}
```

Status:

```text
201 Created
```

Os campos `nome` e `email` são obrigatórios.

## 10. Listagem de usuários

Requisição:

```http
GET /usuarios
```

Resposta:

```json
{
    "data": [
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
}
```

Status:

```text
200 OK
```

## 11. Busca por ID

Para consultar um usuário específico:

```http
GET /usuarios/1
```

Resposta:

```json
{
    "data": {
        "id": 1,
        "nome": "João da Silva",
        "email": "joao@email.com"
    }
}
```

Caso o ID não exista:

```json
{
    "error": "Usuário não encontrado."
}
```

Status:

```text
404 Not Found
```

## 12. Atualização de usuário

A atualização utiliza o método `PUT`:

```http
PUT /usuarios/1
Content-Type: application/json
```

Corpo da requisição:

```json
{
    "nome": "João da Silva Atualizado",
    "email": "joao.novo@email.com"
}
```

Resposta:

```json
{
    "data": {
        "id": 1,
        "nome": "João da Silva Atualizado",
        "email": "joao.novo@email.com"
    }
}
```

Status:

```text
200 OK
```

Os campos `nome` e `email` são obrigatórios para a atualização.

## 13. Exclusão de usuário

Para remover um usuário:

```http
DELETE /usuarios/1
```

Se o usuário existir, o registro será removido da estrutura em memória.

Resposta:

```text
204 No Content
```

Caso o ID não exista:

```json
{
    "error": "Usuário não encontrado."
}
```

Status:

```text
404 Not Found
```

## 14. Validação de dados

A API realiza validações nas operações `POST` e `PUT`.

São verificadas as seguintes condições:

* O corpo da requisição deve estar no formato JSON.
* O campo `nome` deve ser informado.
* O campo `email` deve ser informado.
* `nome` e `email` devem ser textos.
* Os campos não podem estar vazios.
* O e-mail deve possuir um formato básico válido.

Quando uma dessas regras é violada, a API retorna:

```json
{
    "error": "Mensagem descrevendo o problema."
}
```

com o status:

```text
400 Bad Request
```

## 15. Padronização das respostas

As respostas da API seguem um formato padronizado.

### Sucesso

Os dados são retornados utilizando a chave `data`:

```json
{
    "data": {}
}
```

### Erro

As mensagens de erro utilizam a chave `error`:

```json
{
    "error": "Descrição do erro."
}
```

Essa padronização facilita o consumo da API pelo front-end e torna o comportamento dos endpoints mais previsível.

## 16. Persistência

Nesta primeira versão, os usuários são armazenados em uma lista Python na memória do servidor.

Essa abordagem foi escolhida devido ao objetivo de desenvolver um MVP de maneira rápida, evitando inicialmente a complexidade de configuração e gerenciamento de um banco de dados.

Como consequência, os dados armazenados são perdidos quando o servidor é encerrado ou reiniciado.

Em uma versão futura, a estrutura poderá ser substituída por um banco de dados relacional ou não relacional.

## 17. Status HTTP utilizados

A API utiliza códigos HTTP de acordo com a semântica das operações:

* **200 OK** — operação realizada com sucesso.
* **201 Created** — novo usuário criado.
* **204 No Content** — usuário removido com sucesso, sem conteúdo de resposta.
* **400 Bad Request** — dados enviados pelo cliente são inválidos.
* **404 Not Found** — usuário solicitado não foi encontrado.

## 18. Testes

Os testes automatizados poderão ser executados utilizando o `pytest`:

```bash
pytest
```

Os testes devem verificar principalmente:

* criação de usuários;
* listagem de usuários;
* busca por ID;
* atualização de usuários;
* exclusão de usuários;
* tentativa de acesso a usuários inexistentes;
* validação de campos obrigatórios;
* respostas HTTP esperadas.

## 19. Considerações finais

Este projeto representa uma implementação inicial de uma API REST para gerenciamento de usuários. A arquitetura foi desenvolvida com foco em simplicidade, organização e padronização das respostas, características importantes para um MVP.

A estrutura permite futuras evoluções, como implementação de banco de dados, autenticação de usuários, documentação da API, testes automatizados mais abrangentes e implantação em um ambiente de produção.
