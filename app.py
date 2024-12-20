from flask import Flask, request, jsonify

app = Flask(__name__)
# Creates a flask app instance

# In-memory storage for products
products = [
    {'id': 1, 'name': 'Product A', 'description': 'Description A', 'price': 10.99},
    {'id': 2, 'name': 'Product B', 'description': 'Description B', 'price': 29.99}
]
# This is a list that will store the products details temporarily in memory(will restart when the server restarts)

# Generate a unique ID for new products
def generate_id():
    return max(product['id'] for product in products) + 1
    # This function will generate a unique ID for the new products by finding the maximum ID in the products list and adding 1 to it

# POST /products - Create a new product
@app.route('/products', methods=['POST'])
# This route will handle the POST request to create a new products
def create_product():
    # Get the data from the POST request
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data or 'price' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    try:
        product = {
            "name": data['name'],
            "description": data['description'],
            "price": float(data['price'])
        }
        # Create a new product object with the data from the request
        products.append(product)
        # Append the new product to the products list
        return jsonify(product), 201
        # Return the new product as a JSON response
    except ValueError:
        return jsonify({'error': 'Invalid price format'}), 400
        # If there is an error in the price format, return an error response

# Endpoint to get all products
@app.route('/products', methods=['GET'])
# This route will handle the GET request to get all products
def get_products():
    return jsonify(products), 200
    # Return the list of products as a JSON response
    # Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
    # This will run the app if this script is executed directly
    # This is a simple Flask application that provides an API to create and retrieve products. The products are stored in an in-memory list and can be accessed via the /products endpoint. The create_product function handles the POST request to create a new product, while the get_products function handles the GET request to retrieve all products. The app.run(debug=True) line at the end of the script starts the Flask application in debug mode. You can run this script in your terminal to start the Flask server and access the API endpoints.  