from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()

class Product(BaseModel):
    p_name:str
    p_price:int

products=[]

@app.get("/product_details")
def get_product_details():
    return products

@app.post("/product_creation",status_code=201)
def create_product(pro: Product):
    products.append(pro)
    return {
        "message": "Product created successfully",
        "product": pro
    }

@app.delete("/product_deletion/{index}")
def delete(index: int):
    products.pop(index)
    return{
        "successfully deleted":{index}
    }
@app.put("/product_update/{index}")
def update_product(index: int,pro: Product):
    products[index]=pro
    return{
        "message":"Product updated successfully",
        "product":pro
    }

@app.get("/product/{index}")
def prod(index:int):

    if(index>=len(products)):
        raise HTTPException(status_code=500, detail="product_not_found")
   
    return "product is:" + str(products[index])