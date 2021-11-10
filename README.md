# API E-commerce

Uma API REST feita para cadastrar, obter, alterar e deletar produtos.

## Bibliotecas utilzadas

* PyMySQL
* Flask_httpauth
* Flask_restful
* Flask

Para instalar essas bibliotecas, acesse a raíz do projeto e rode o comando:

```
$ pip3 install -r requirements.txt
```

## Como utilizar

Faça seu teste da API seguindo as orientações abaixo.

### Obter todos os produtos

Basta fazer uma requisição GET (sem parâmetros) para a URN **/admin/products**. O resultado pode ser este:

```json
[
  {
    "id": 1,
    "name": "O guia do mochileiro Python",
    "description": "Este livro mostra como ser um programador Python melhor",
    "price": 84.99,
    "inventory": 2470,
    "barcode": 12345678923
  },
  {
    "id": 2,
    "name": "UX/UI: as melhores práticas",
    "description": "Uma série de conceitos sobre UX",
    "price": 40.5,
    "inventory": 140,
    "barcode": 12348468923
  },

]
```

### Obter um produto especifico

Especifique o ID do produto nos parâmetros de URI para obter-lo:

```
/admin/products?id=2
```

O resultado poderá ser assim:

```json
{
    "id": 2,
    "name": "UX/UI: as melhores práticas",
    "description": "Uma série de conceitos sobre UX",
    "price": 40.5,
    "inventory": 140,
    "barcode": 12348468923
},
```

### Cadastrar produtos

Utilize o método **POST** na URN **/admin/products** e envie as informações em body como **JSON**:

```json
{
    "name": "Nome do produto",
    "description": "Descrição",
    "price": 3670.00, /* Preço do produto */
    "inventory": 5679, /* Quantidade disponível */
    "barcode": 92348468923 /* Cód. de barras até 20 números */
}
```

### Atualizar produtos

Aqui é usado o método PUT na mesma URN, enviando as novas informações em JSON e especificando nos parâmetros de URI o ID do produto a ser atualizado (obtenha o ID do produto utilizando o método GET):

```
/admin/products?id=2
```

```json
{
    "name": "Nome do produto",
    "description": "Descrição",
    "price": 3670.00, /* Preço do produto */
    "inventory": 5679, /* Quantidade disponível */
    "barcode": 92348468923 /* Cód. de barras até 20 números */
}
```