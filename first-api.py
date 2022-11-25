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


@app.get("/products/{id}")
def get_products(id: int, response: Response):
    for product in products:
        if product.get('id') == id:
            return product

    response.status_code = 404
    return "Product not found"
