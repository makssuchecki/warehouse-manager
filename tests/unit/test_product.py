from src.product import Product
import pytest 

class TestProduct:
    @pytest.fixture
    def make_product(self):
        def make(name, quantity):
            return Product(name, quantity)
        return make

    @pytest.mark.parametrize(
        "name, quantity, expected",
        [
            ("Acoustic Guitar", 0, "Invalid amount"),
            ("Grand Piano", -12, "Invalid amount"),
            ("Dynamic Microphone", 9999, "Invalid amount"),
            ("Violin", 10, 10),
        ]
    )

    def test_amount(self, make_product, name, quantity, expected):
        product = make_product(name, quantity)
        assert product.quantity == expected

    def test_product_creation(self, make_product):
        product = make_product("Electric Guitar", 2)
        assert product.name == "Electric Guitar"
        assert product.quantity == 2

    def test_receive_stock(self, make_product):
        product = make_product("Electric Guitar", 2)
        result = product.receive_stock(2)
        assert result == True
        assert product.quantity == 4
        assert len(product.history) == 1

    def test_release_stock(self, make_product):
        product = make_product("Electric Guitar", 4)
        result = product.release_stock(2)
        assert result == True
        assert product.quantity == 2
        assert len(product.history) == 1