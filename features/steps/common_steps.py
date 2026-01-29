from behave import *
import requests

URL = "http://localhost:5000"


@given('a product "{name}" with quantity {quantity:d} exists')
def product_exists(context, name, quantity):
    requests.post(
        f"{URL}/products",
        json={"name": name, "quantity": quantity}
    )
