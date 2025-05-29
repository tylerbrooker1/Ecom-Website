from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)
app.secret_key = "secret-key"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

products = {
    "minimalist-lamp": {
        "title": "Modern Minimalist Lamp",
        "price": 79.99,
        "description": "A sleek and stylish minimalist lamp perfect for modern interiors. Features adjustable brightness and a touch-sensitive base.",
        "images": [
            "/static/images/minimalist-lamp_1.jpg",
            "/static/images/minimalist-lamp_2.jpg",
            "/static/images/minimalist-lamp_3.jpg",
        ],
        "variants": ["Black", "White", "Grey"],
    },
    "vintage-lamp": {
        "title": "Vintage Brass Lamp",
        "price": 89.99,
        "description": "A vintage-style lamp with brass finish and Edison bulb. Brings a touch of classic charm to any room.",
        "images": [
            "/static/images/vintage-lamp_1.jpg",
            "/static/images/vintage-lamp_2.jpg",
            "/static/images/vintage-lamp_3.jpg",
            "/static/images/vintage-lamp_4.jpg",
        ],
        "variants": ["Brass", "Antique Bronze"],
    },
    "smart-lamp": {
        "title": "Smart LED Lamp",
        "price": 99.99,
        "description": "Voice-controlled smart LED lamp with adjustable colors and brightness. Compatible with Alexa and Google Home.",
        "images": [
            "/static/images/smart-lamp_1.jpg",
            "/static/images/smart-lamp_2.jpg",
            "/static/images/smart-lamp_3.jpg",
        ],
        "variants": ["Black", "White"],
    },
}


@app.route("/")
def index():
    cart = session.get("cart", [])
    cart_items = []
    for i, item in enumerate(cart):
        product = products.get(item["product_id"])
        if product:
            cart_items.append(
                {
                    "index": i,
                    "title": product["title"],
                    "variant": item["variant"],
                    "quantity": item["quantity"],
                    "price": product["price"],
                }
            )
    return render_template("index.html", products=products, cart_items=cart_items)


@app.route("/product/<product_id>")
def product_page(product_id):

    cart = session.get("cart", [])
    cart_items = []
    for i, item in enumerate(cart):
        product = products.get(item["product_id"])
        if product:
            cart_items.append(
                {
                    "index": i,
                    "title": product["title"],
                    "variant": item["variant"],
                    "quantity": item["quantity"],
                    "price": product["price"],
                }
            )

    product = products.get(product_id)
    if not product:
        return "Product not found", 404

    return render_template(
        "product.html", product=product, product_id=product_id, cart_items=cart_items
    )


@app.route("/add-to-cart", methods=["POST"])
def add_to_cart():
    data = request.get_json()
    product_id = data.get("product_id")
    variant = data.get("variant")

    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(
        {"product_id": product_id, "variant": variant, "quantity": 1}
    )
    session.modified = True

    return jsonify({"message": "Item added to cart successfully"})


@app.route("/clear-cart", methods=["POST"])
def clear_cart():
    session.pop("cart", None)
    return redirect(request.referrer)


@app.route("/remove-from-cart", methods=["POST"])
def remove_from_cart():
    index = int(request.form.get("index"))
    if "cart" in session and 0 <= index < len(session["cart"]):
        session["cart"].pop(index)
        session.modified = True
    return redirect(request.referrer + "#your-cart")


if __name__ == "__main__":
    app.run(debug=True)
