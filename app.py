import os

from flask import Flask
from flask_cors import CORS

from api.addtocart_route import addtocart_bp
from api.buy_route import buy_bp
from api.orders_route import order_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(buy_bp)
app.register_blueprint(order_bp)
app.register_blueprint(addtocart_bp)


if __name__ == "__main__":
    port = os.environ.get("PORT", 10000)
    app.run(port=5002, debug=True)
