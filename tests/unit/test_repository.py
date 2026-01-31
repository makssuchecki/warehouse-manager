from src.products_repository import MongoProductsRepository
import pytest

class TestRepository:
    def test_load_all(self, mocker):
        repo = MongoProductsRepository()

        mock_collection = mocker.Mock()
        mock_collection.find.return_value = [
            {
                "name": "Electric_Guitar",
                "quantity": 10
            },
            {
                "name": "Grand_Piano",
                "quantity": 2
            }
        ]
        repo._collection = mock_collection

        products = repo.load_all()

        assert len(products) == 2
        assert products[0].name == "Electric_Guitar"
    def test_load_all_error(self, mocker):
        repo = MongoProductsRepository()

        mock_collection = mocker.Mock()
        mock_collection.find.return_value = [
            {
                "name": "Electric_Guitar",
                "quantity": 0
            },
            {
                "name": "Grand_Piano",
                "quantity": 2
            }
        ]
        repo._collection = mock_collection

        products = repo.load_all()

        assert len(products) == 1
        assert products[0].name == "Grand_Piano"
        
    def test_save_all(self, mocker):
        repo = MongoProductsRepository()

        mock_collection = mocker.Mock()
        repo._collection = mock_collection

        product1 = mocker.Mock()
        product1.quantity = 10
        product1.to_dict.return_value = {
            "name": "Electric_Guitar",
            "quantity": 10
        }
        product2 = mocker.Mock()
        product2.quantity = 2
        product2.to_dict.return_value = {
            "name": "Grand_Piano",
            "quantity": 2
        }
        products = [product1, product2]

        repo.save_all(products)

        mock_collection.delete_many.assert_called_once_with({})
        assert mock_collection.update_one.call_count == 2

        