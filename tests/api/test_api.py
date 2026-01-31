import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"

class TestAPI:
    
    def test_add_product(self):
        response = requests.post(
            f"{BASE_URL}/products",
            json={"name": "Guitar", "quantity": 10, "price": 100}
        )
        assert response.status_code == 201
    
    def test_get_products(self):
        response = requests.get(f"{BASE_URL}/products")
        assert response.status_code == 200

    def test_get_single_product(self):
        response = requests.get(f"{BASE_URL}/products/Guitar")
        assert response.status_code == 200
        assert response.json()["quantity"] == 10

    def test_receive_stock(self):
        response = requests.post(
            f"{BASE_URL}/warehouse/in",
            json={"name": "Guitar", "amount": 5}
        )
        assert response.status_code == 200

        product = requests.get(f"{BASE_URL}/products/Guitar").json()
        assert product["quantity"] == 15

    def test_release_stock_success(self):
        response = requests.post(
            f"{BASE_URL}/warehouse/out",
            json={"name": "Guitar", "amount": 3}
        )
        assert response.status_code == 200

    def test_release_stock_fail_not_enough(self):
        response = requests.post(
            f"{BASE_URL}/warehouse/out",
            json={"name": "Guitar", "amount": 9999}
        )
        assert response.status_code == 400

    def test_receive_stock_fail_not_enough(self):
        response = requests.post(
            f"{BASE_URL}/warehouse/in",
            json={"name": "Guitar", "amount": 0}
        )
        assert response.status_code == 400

    def test_delete_product_forbidden_for_user(self):
        response = requests.delete(
            f"{BASE_URL}/products/Guitar",
            headers={"Role": "user"}
        )
        assert response.status_code == 403

    def test_delete_product_as_admin(self):
        response = requests.delete(
            f"{BASE_URL}/products/Guitar",
            headers={"Role": "admin"}
        )
        assert response.status_code == 200

    def test_save_all(self):
        response = requests.post(f"{BASE_URL}/products/save")
        assert response.status_code == 200
        assert response.json()["message"] == "Products saved to a database"

    def test_load_all(self):
        response = requests.post(f"{BASE_URL}/products/load")
        assert response.status_code == 200
        assert response.json()["message"] == "Products loaded from a database"