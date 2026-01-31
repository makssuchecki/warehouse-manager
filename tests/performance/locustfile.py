import time
from locust import HttpUser, task, between
import random

def random_name():
    return "product" + str(random.randint(0, 9999))

class QuistartUser(HttpUser):
    host = "http://127.0.0.1:5000"
    wait_time = between(0.5, 1)

    def on_start(self):
        self.product_name = random_name()
        self.client.post(f"/products",
                    json={"name": self.product_name, "quantity": 5, "price": 10})

    @task(3)
    def get_products(self):
        self.client.get("/products")

    @task(3)
    def get_single_product(self):
        self.client.get(f"/products/{self.product_name}")

    @task(3)
    def receive_stock(self):
        self.client.post(f"/warehouse/in",
                         json={"name": self.product_name, "amount": 1})
    @task(2)
    def release_stock(self):
        self.client.post(f"/warehouse/out",
                         json={"name": self.product_name, "amount": 1}, catch_response=True)


