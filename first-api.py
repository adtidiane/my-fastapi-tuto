from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    name: str
    price: float


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


@app.post("/products")
def create_product(new_product: Product, response: Response):
    product = new_product.dict()
    product['id'] = len(products) + 1
    products.append(product)
    response.status_code = 201
    return product


@app.put("/products/{id}")
def edit_product(id: int, edited_product: Product, response: Response):
    for product in products:
        if product["id"] == id:
            product["name"] = edited_product.name
            product["price"] = edited_product.price
            response.status_code = 200
            return product
    response.status_code = 404
    return "Product Not found"


@app.delete("/products/{id}")
def delete_product(id: int, response: Response):
    for product in products:
        if product["id"] == id:
            products.remove(product)
            response.status_code = 204
            return "Product deleted"
    response.status_code = 404
    return "Product Not found"
