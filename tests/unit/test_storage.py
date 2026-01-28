from src.storage import Storage
from src.product import Product
from src.user import User
import pytest

class TestStorage:
    @pytest.fixture()
    def storage(self):
        return Storage()

    def test_add_and_search(self, storage: Storage):
        new_product = Product("Guitar", 12)
        storage.add_product(new_product)

        found_product = storage.get_product_by_name("Guitar")
        assert found_product == new_product
    
    def test_search_not_found(self, storage: Storage):
        found_product = storage.get_product_by_name("Guitar")
        assert found_product == None

    def test_get_all_products(self, storage: Storage):
        new_product1 = Product("Guitar", 12)
        new_product2 = Product("Piano", 4)
        storage.add_product(new_product1)
        storage.add_product(new_product2)
        all_products = storage.get_all_products()
        assert all_products == [new_product1, new_product2]

    def test_admin_can_delete_product(self, storage: Storage):
        new_product1 = Product("Guitar", 12)
        user = User("Kurt Cobain", "admin")
        storage.add_product(new_product1)

        result = storage.delete_product("Guitar", user)
        assert result is True
        assert storage.get_product_by_name("Guitar") is None

    def test_user_cannot_delete_product(self, storage: Storage):
        new_product1 = Product("Guitar", 12)
        user = User("Alex Turner", "user")
        storage.add_product(new_product1)

        result = storage.delete_product("Guitar", user)
        assert result is False
        assert storage.get_product_by_name("Guitar") is not None

    def test_count_products(self, storage: Storage):
        new_product1 = Product("Guitar", 12)
        new_product2 = Product("Piano", 4)

        storage.add_product(new_product1)
        storage.add_product(new_product2)
        assert storage.count_products() == 2
