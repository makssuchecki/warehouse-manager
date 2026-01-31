from pymongo import MongoClient
from src.product import Product

class MongoProductsRepository:
    def __init__(self, uri="mongodb://localhost:27017"):
        self._client = MongoClient(uri)
        self.db = self._client["warehouse"]
        self._collection = self.db["products"]

    def save_all(self, products):
        self._collection.delete_many({})
        for product in products:
            self._collection.update_one(
                {"name": product.name},
                {"$set": product.to_dict()},
                upsert=True,
            )
    def load_all(self):
        documents = self._collection.find({}, {"_id": 0})

        products = []
        for doc in documents:
            try:
                products.append(Product(doc["name"], int(doc["quantity"])))
            except (ValueError, KeyError, TypeError):
                continue

        return products