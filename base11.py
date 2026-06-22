from pydantic import BaseModel
from fastapi import FastAPI     
class Product(BaseModel):
    name: str
    price: int
app=FastAPI()
@app.post("/product")
def create_product(product: Product):
    return {
        "product_name": product.name,
        "price": product.price
    }