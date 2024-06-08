from flask import Flask, jsonify, request

app = Flask(__name__)

# Example data (replace with actual data handling logic)
products = [
    {'id': 1, 'name': 'Product A', 'manufacturer': 'Manufacturer A'},
    {'id': 2, 'name': 'Product B', 'manufacturer': 'Manufacturer B'}
]

@app.route('/')
def index():
    return 'Welcome to the backend of Electronic Repair Tool'

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/api/products', methods=['POST'])
def add_product():
    new_product = request.json
    products.append(new_product)
    return jsonify({'message': 'Product added successfully'})

if __name__ == '__main__':
    app.run(debug=True)
