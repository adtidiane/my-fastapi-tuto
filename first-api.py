from fastapi import FastAPI, Response

app = FastAPI()

products = [
    {"id": 1, "name": "iPad", "price": 599},
    {"id": 2, "name": "iPhone", "price": 999},
    {"id": 3, "name": "iWatch", "price": 699},
]


@app.get("/products")
def index():
    return products


@app.get("/products/search")
def index(name, response: Response):
    founded_products = [product for product in products if name.lower() in product.get('name').lower()]
    if not founded_products:
        response.status_code = 404
        return "Product not found"
    return founded_products if len(founded_products) > 1 else founded_products[0]


@app.get("/products/{id}")
def index(id: int, response: Response):
    for product in products:
        if product.get('id') == id:
            return product

    response.status_code = 404
    return "Product not found"
