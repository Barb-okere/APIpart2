from flask import Flask, request, jsonify

app = Flask(__name__)
# Creates a flask app instance

# In-memory storage for products
products = []
# This is a list that will store the products in memory

# POST /products - Create a new product
@app.route('/products', methods=['POST'])
# This route will handle the POST request to create a new products