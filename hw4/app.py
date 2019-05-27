from flask import Flask, render_template
from products import get_products, get_product

app = Flask(__name__)
app.config.from_object('conf.DevelopentConfig')


@app.route("/")
def index():
    return render_template('index.html', products=get_products())


@app.route("/product/<int:product_id>")
def detail(product_id):
    return render_template('product.html', product=get_product(product_id))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


app.run()
