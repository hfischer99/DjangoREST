# DjangoREST 
- **DESAFIO 1** (http://127.0.0.1:8000/categorias/):
  - Criar um novo projeto em DJANGO
  - Conectar ao banco de dados
  - Criar uma Model de Categorias
  - Essa Categoria deve ser única e isso deve ser garantido no banco de dados
  - Expor uma API de categorias implementando a segurança padrão do DJANGO


- **DESAFIO 2** (http://127.0.0.1:8000/admin/imoveis/orcamento/):
  - Existem X casas à venda. Juntas essas casas valem I reais. Você tem um orçamento de B reais para gastar. Qual o maior número de casas que você pode comprar com o orçamento?
  - A quantidade de casas e valor podem ser definidos da maneira que desejar, é possivel também efetuar pesquisas durante o desenvolvimento
Output. Ao final do processamento, exiba a quantidade de casas que puderam ser compradas, bem como o valor total gasto.
  

  - Cadastro de casas: 
    - http://127.0.0.1:8000/admin/imoveis/casa/ ou
    - http://127.0.0.1:8000/casas/
  - Adicionar Orçamentos: 
    - http://127.0.0.1:8000/admin/imoveis/orcamento/ ou 
    - http://127.0.0.1:8000/orcamentos/
  - Template Orçamento: 
    - http://127.0.0.1:8000/orcamento/ [id]  ou 
    - http://127.0.0.1:8000/orcamentos/ [id]/
    - ![Screenshot_5](https://user-images.githubusercontent.com/43329377/159197709-65eab0be-7302-4321-91d1-0ab6efa19de4.png)



## 🖥️ Comandos
```
git clone https://github.com/hfischer99/DjangoREST.git
```
```
cd DjangoREST
```
```
python3 -m venv venv
```
```
source env/bin/activate
```
```
pip install -r requirements.txt
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py createsuperuser
```
```
python manage.py runserver
```
## 🛠️ Recursos Django Implementados

- **DEFAULT_PERMISSION_CLASSES** - `A autenticação ou identificação por si só geralmente não é suficiente para obter acesso à informação ou código. Para isso, a entidade que solicita o acesso deve ter autorização.`
- **DEFAULT_PAGINATION_CLASS** - `O Django fornece algumas classes que ajudam a gerenciar dados paginados`

## 📦 Endpoint

-  **Listar registros**

Utilizar o método GET para a URL principal do recurso:

    GET /categorias/
   
Retorno (exemplo):

    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "nome": "Categoria"
            }
        ]
    }

-  **Obter um registro específico**

Utilizar o método GET para a URL principal do recurso:

    GET /categorias/[id]/
   
Retorno (exemplo):

    {
	    "id": 1,
	    "nome": "Categoria"
    }

-  **Editar um registro específico**

Utilizar o método GET para a URL principal do recurso:

    PUT /categorias/[id]/

    BODY:
    {
        "nome": "Categoria1"
    }
   
Retorno (exemplo):

    {
	    "id": 1,
	    "nome": "Categoria1"
    }

Obs: enviar apenas os campos a serem alterados. Necessário estar logado.

-  **Adicionar um NOVO registro**

Utilizar o método GET para a URL principal do recurso:

    POST /categorias/

    BODY:
    {
        "nome": "Nova Categoria"
    }
   
Retorno (exemplo):

    {
	    "id": 2,
	    "nome": "Nova Categoria"
    }

Obs: Necessário estar logado.

-  **Excluir um registro específico**

Utilizar o método GET para a URL principal do recurso:

    DELETE /categorias/[id]/

Obs: Necessário estar logado.
