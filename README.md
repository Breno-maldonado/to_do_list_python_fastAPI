# 📝 To-Do List API com FastAPI
Esta é uma API RESTful para gerenciamento de tarefas (To-Do List), desenvolvida para colocar em prática conceitos de ```CRUD```, persistência de dados em arquivos ```JSON``` e validação de esquemas.

## 🚀 Sobre o Projeto
O objetivo deste projeto foi construir uma aplicação funcional que permitisse:

- Create: Criar novas tarefas com IDs auto-incrementáveis.

- Read: Listar todas as tarefas ou buscar uma específica por ID.

- Update: Atualizar informações de tarefas existentes (como título, descrição ou status).

- Delete: Remover tarefas do sistema.

A API utiliza o ```FastAPI``` pela sua velocidade e pela geração automática de documentação interativa.

## 🛠️ Tecnologias Utilizadas
- Python 3.10+: Linguagem base do projeto.

- FastAPI: Framework moderno e de alta performance para construção de APIs.

- Pydantic: Utilizado para validação de dados e criação de modelos (schemas).

- Uvicorn: Servidor ASGI para rodar a aplicação.

- JSON: Utilizado como banco de dados simplificado para persistência de informações.

## 🏗️ Arquitetura e Lógica
Durante o desenvolvimento, focamos em conceitos importantes de engenharia:

1. Persistência (I/O): Implementamos funções para ler e escrever em um arquivo .json, garantindo que os dados não se percam ao reiniciar o servidor.

2. Tratamento de Erros: Utilizamos o HTTPException para retornar códigos de status corretos (como o 404 Not Found), facilitando a comunicação com o front-end.

3. Validação de Dados: O uso de Field e BaseModel do Pydantic garante que a API não aceite dados "sujos" (como títulos vazios ou descrições longas demais).

4. Auto-incremento: Criamos uma lógica para que o sistema gerencie os IDs automaticamente, evitando conflitos de dados.

## 📝 Acesse a Documentação
A API estará rodando em ```http://127.0.0.1:8000```. Para testar as rotas, acesse a documentação interativa (Swagger UI) em:
