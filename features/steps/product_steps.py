from behave import *
import requests

URL = "http://localhost:5000"

@given("the warehouse system is running")
def system_running(context):
    res = requests.get(f"{URL}/products")
    assert res.status_code == 200


@given('a product "{name}" with quantity {quantity:d} exists')
def product_exists(context, name, quantity):
    requests.post(
        f"{URL}/products",
        json={"name": name, "quantity": quantity}
    )

@when('I add a product with name "{name}" and quantity {quantity:d}')
def add_product(context, name, quantity):
    context.response = requests.post(
        f"{URL}/products",
        json={"name": name, "quantity": quantity}
    )


@when("I request all products")
def get_products(context):
    context.response = requests.get(f"{URL}/products")


@when('I delete product "{name}" as admin')
def delete_admin(context, name):
    context.response = requests.delete(
        f"{URL}/products/{name}",
        headers={"Role": "admin"}
    )


@when('I delete product "{name}" as user')
def delete_user(context, name):
    context.response = requests.delete(
        f"{URL}/products/{name}",
        headers={"Role": "user"}
    )

@then("the product should be created successfully")
def created(context):
    assert context.response.status_code == 201


@then('I should receive a list containing product "{name}"')
def product_listed(context, name):
    data = context.response.json()
    names = [p["name"] for p in data]
    assert name in names


@then("the product should be deleted")
def deleted(context):
    assert context.response.status_code == 200


@then("the operation should be forbidden")
def forbidden(context):
    assert context.response.status_code == 403