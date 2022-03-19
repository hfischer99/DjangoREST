# DjangoREST
Django REST by Henrique Fischer

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
