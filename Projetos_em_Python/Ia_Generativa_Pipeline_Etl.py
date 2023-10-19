#  Projeto 1: Explorando IA Generativa em um Pipeline de ETL com Python

# Passo três: upload arquivo .csv e extrair informações de ID da API do Santander 
# De início, foi criado uma variável com o endereço da API:

sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

# A seguir, importei a biblioteca pandas para extrair os dados e carreguei o meu arquivo .csv com os IDs.

import pandas as pd

df = pd.read_csv('SDW2023.csv')
user_ids = df['UserID'].tolist()
print(user_ids)

# O print() retornou:

[5200, 5201, 5203,]

# Após isso, rodei o código para importar os dados dos usuários que gerei no [Swagger UI](https://sdw-2023-prd.up.railway.app/swagger-ui/index.html#/Users%20Controller/findById).

import requests
import json

def get_user(id):
  response = requests.get(f'{sdw2023_api_url}/users/{id}')
  return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))

# Com isso, meus usuários foram retornados:
[
  {
    "id": 5200,
    "name": "Marina",
    "account": {
      "id": 5403,
      "number": "34200-4",
      "agency": "0018",
      "balance": 0.0,
      "limit": 500.0
    },
    "card": {
      "id": 4320,
      "number": "**** **** **** 5184",
      "limit": 1000.0
    },
    "features": [],
    "news": []
  },
  {
    "id": 5201,
    "name": "Alice",
    "account": {
      "id": 5404,
      "number": "34201-4",
      "agency": "0018",
      "balance": 0.0,
      "limit": 500.0
    },
    "card": {
      "id": 4321,
      "number": "**** **** **** 5186",
      "limit": 1000.0
    },
    "features": [],
    "news": []
  },
  {
    "id": 5202,
    "name": "Laura",
    "account": {
      "id": 5405,
      "number": "34202-4",
      "agency": "0018",
      "balance": 0.0,
      "limit": 500.0
    },
    "card": {
      "id": 5405,
      "number": "**** **** **** 5618",
      "limit": 1000.0
    },
    "features": [],
    "news": []
  },
]

# Passo quatro: fase de transformação de dados, onde deve ser gerado uma mensagem de marketing personalizada para cada usuário utilizando a IA Generatira GPT-4
# Primeiro foi necessário instalar o openai para conseguir utilizar o GPT-4:

!pip install openai

# Depois, informei minha API Key da Open IA para conseguir utilizar o Chat:

openai_api_key = 'inclua-key-aqui'

# Depois, passei as instruções para o Python informando que eu queria que ele gerasse, via IA GPT-4, mensagens personalizadas para cada um dos 5 usuários que criei, informando sobre a importância do investimento no planejamento financeiro do cliente:

import openai

openai.api_key = openai_api_key

def generate_ai_news(user):
  completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
      {
          "role": "system",
          "content": "Você é um gerente com conhecimento em markting bancário."
      },
      {
          "role": "user",
          "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos no planejamento financeiro (máximo de 100 caracteres)"
      }
    ]
  )
  return completion.choices[0].message.content.strip('\"')

for user in users:
  news = generate_ai_news(user)
  print(news)
  user['news'].append({
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": news
  })

# Ao executar o código anterior, tive como retorno:

"Mariana, invista em seu futuro com segurança!"
"Alice, planeje hoje para colher amanhã!"
"Laura, seu futuro merece investimentos inteligentes!"

# Passo cinco: fase de carregamento dos dados transformados de volta para a API do Santander
# Para isso, solicitei que o Python atualizasse a lista de "news" em cada usuário

def update_user(user):
  response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
  return True if response.status_code == 200 else False

for user in users:
  success = update_user(user)
  print(f"User {user['name']} updated? {success}!")

# Recebi como resposta ao código

"User Mariana updated? True!"
"User Alice updated? True!"
"User Laura updated? True!"

# Para conferência, se você consultar cada um dos usuários acima no "Get a user by ID" no Swagger UI, você terá como retorno:
# Ao pesquisar o ID 5200

{
  "id": 5200,
  "name": "Mariana",
  "account": {
    "id": 5403,
    "number": "34200-4",
    "agency": "0018",
    "balance": 0,
    "limit": 500
  },
  "card": {
    "id": 4320,
    "number": "**** **** **** 5184",
    "limit": 1000
  },
  "features": [
    {
      "id": 1520,
      "icon": "string",
      "description": "string"
    }
  ],
  "news": [
    {
      "id": 9239,
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": "Mariana, invista em seu futuro com segurança!"
    }
  ]
}

# Ao pesquisar o ID 5201

{
  "id": 5201,
  "name": "Alice",
  "account": {
    "id": 5404,
    "number": "34201-4",
    "agency": "0018",
    "balance": 0,
    "limit": 500
  },
  "card": {
    "id": 4321,
    "number": "**** **** **** 5186",
    "limit": 1000
  },
  "features": [
    {
      "id": 1521,
      "icon": "string",
      "description": "string"
    }
  ],
  "news": [
    {
      "id": 9240,
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": "Alice, planeje hoje para colher amanhã!"
    }
  ]
}

# Ao pesquisar o ID 5202

{
  "id": 5202,
  "name": "Laura",
  "account": {
    "id": 5405,
    "number": "34202-4",
    "agency": "0018",
    "balance": 0,
    "limit": 500
  },
  "card": {
    "id": 5405,
    "number": "**** **** **** 5618",
    "limit": 1000
  },
  "features": [
    {
      "id": 1522,
      "icon": "string",
      "description": "string"
    }
  ],
  "news": [
    {
      "id": 9241,
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": "Laura, seu futuro merece investimentos inteligentes!"
    }
  ]
}

# Esse é o final do código! 