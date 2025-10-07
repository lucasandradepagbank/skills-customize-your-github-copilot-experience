# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Aprenda a criar uma API REST simples utilizando o framework FastAPI em Python. Você irá construir endpoints para manipular dados de uma lista de tarefas (to-do list).

## 📝 Tasks

### 🛠️ Criar Estrutura Básica da API

#### Description
Implemente uma API com FastAPI que permita listar, adicionar e remover tarefas de uma lista.

#### Requirements
Completed program should:

- Inicializar um projeto FastAPI
- Criar endpoint GET para listar todas as tarefas
- Criar endpoint POST para adicionar uma nova tarefa
- Criar endpoint DELETE para remover uma tarefa pelo ID

### 🛠️ Validação e Mensagens de Erro

#### Description
Adicione validações para garantir que os dados recebidos estejam corretos e retorne mensagens de erro amigáveis.

#### Requirements
Completed program should:

- Validar se o campo "tarefa" não está vazio ao adicionar
- Retornar erro 404 se tentar remover uma tarefa inexistente
- Retornar mensagens claras para sucesso e erro
