import requests

BASE_URL = 'http://127.0.0.1:5000'

# Add a new product
def add_product(name, description, price):
    response = requests.post(f'{BASE_URL}/products',json={
        'name': name, 
        'description': description, 
        'price': price}
    )
    if response.status_code == 201:
        print(f'Product added: {response.json()}')
    else:
        print(f'Failed to add product: {response.json()}')

# Retrieves all products
def get_products():
    response = requests.get(f'{BASE_URL}/products')
    if response.status_code == 200:
        print(f'Products: {response.json()}')
    else:
        print(f'Failed to get products: {response.json()}')

        