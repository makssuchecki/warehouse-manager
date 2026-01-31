from src.product import Product
import pytest 

class TestProduct:
    @pytest.fixture
    def make_product(self):
        def make(name, quantity):
            return Product(name, quantity)
        return make

    @pytest.mark.parametrize(
        "name, quantity",
        [
            ("Acoustic Guitar", 0),
            ("Grand Piano", -12),
            ("Dynamic Microphone", 9999),
        ]
    )
    def test_invalid_amount_raises_error(self, make_product, name, quantity):
        with pytest.raises(ValueError):
            make_product(name, quantity)

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

    def test_receive_stock_invalid_amount(self, make_product):
        product = make_product("Electric Guitar", 5)

        result = product.receive_stock(0)

        assert result is False
        assert product.quantity == 5
        assert len(product.history) == 0

    def test_release_stock_invalid_amount(self, make_product):
        product = make_product("Electric Guitar", 5)
        result = product.release_stock(0)

        assert result is False
        assert product.quantity == 5
        assert len(product.history) == 0

    def test_release_stock_not_enough_quantity(self, make_product):
        product = make_product("Electric Guitar", 2)
        result = product.release_stock(10)

        assert result is False
        assert product.quantity == 2
        assert len(product.history) == 0

    def test_history_entry_structure(self, make_product):
        product = make_product("Electric Guitar", 3)

        product.receive_stock(2)

        entry = product.history[0]
        assert "change" in entry
        assert "timestamp" in entry
    def test_release_stock_history_negative_change(self, make_product):
        product = make_product("Electric Guitar", 5)

        product.release_stock(3)

        assert product.history[0]["change"] == -3

    def test_to_dict(self, make_product):
        product = make_product("Electric Guitar", 2)
        result = product.to_dict()
        assert result == {"name": "Electric Guitar", "quantity": 2}
