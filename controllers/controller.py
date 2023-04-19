from app import app
from flask import render_template
from models.order_list import order_list

@app.route('/orders')
def index():
    return render_template('index.jinja', title = "Home", order_list = order_list)

@app.route('/orders/<index>')
def single_order(index):
    return render_template('order.jinja', title = f"Single Order {index}")

