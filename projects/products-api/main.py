from fastapi import FastAPI, HTTPException
from models.product_model import Product


app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello word'}
    

products = []

@app.get('/product')
def get_products():
    return products

@app.post('/product')
def create_product(product: Product):
    products.append(product)
    return {
        'message': 'Product created'
    }
    
@app.get('/product/{product_id}')
def get_product_by_id(product_id: str):
    result = list(filter(lambda p: p.id == product_id, products))
    
    if result:
        return result[0]
    
    raise HTTPException(status_code=404, detail=f'Product {product_id} not found')

@app.delete('/product/{product_id}')
def delete_product_by_id(product_id: str):
    result = list(filter(lambda p: p.id == product_id, products))
    
    if result:
        return products.remove(result[0])
    
    raise HTTPException(status_code=404, detail=f'Product {product_id} not found')


@app.put('/product/{product_id}')
def delete_product_by_id(product_id: str, product: Product):
    result = list(filter(lambda p: p.id == product_id, products))
    
    if result:
        result[0].name = product.name
        result[0].purchase_price = product.purchase_price
        result[0].sales_price = product.sales_price
        result[0].provider = product.provider
        
        return result[0]
    
    raise HTTPException(status_code=404, detail=f'Product {product_id} not found')
    