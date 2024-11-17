from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'system',
    'database': 'ShoppingDB'
}

@app.route('/')
def index():
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    # Fetch products
    cursor.execute("SELECT * FROM Products LIMIT 2")
    products = cursor.fetchall()

    # Close connection
    cursor.close()
    conn.close()

    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    # Fetch product details by ID
    cursor.execute("SELECT * FROM Products WHERE id = %s", (product_id,))
    product = cursor.fetchone()

    # Close connection
    cursor.close()
    conn.close()

    # Handle case where product is not found
    if not product:
        return render_template('404.html'), 404

    return render_template('product_detail.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
