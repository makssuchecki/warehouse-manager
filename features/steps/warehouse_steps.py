from behave import *
import requests

URL = "http://localhost:5000"


@when('I receive {amount:d} items of product "{name}"')
def receive_stock(context, amount, name):
    context.response = requests.post(
        f"{URL}/warehouse/in",
        json={"name": name, "amount": amount}
    )


@when('I release {amount:d} items of product "{name}"')
def release_stock(context, amount, name):
    context.response = requests.post(
        f"{URL}/warehouse/out",
        json={"name": name, "amount": amount}
    )


@then("the stock should be increased")
@then("the stock should be decreased")
def success(context):
    assert context.response.status_code == 200


@then("the operation should fail")
def failed(context):
    assert context.response.status_code == 400