# import requests
# import random
# import time
# import pytest

# BASE_URL = "http://127.0.0.1:5000"

# class TestWarehousePerformance:
#     TIMEOUT = 0.5

#     def random_name(self):
#         return "product" + str(random.randint(0, 9999))

#     def test_create_and_delete(self):
#         start = time.time()

#         for _ in range(100):
#             name = self.random_name()

#             res = requests.post(
#                 f"{BASE_URL}/products",
#                 json={"name": name, "quantity": 10, "price": 10},
#                 timeout=self.TIMEOUT
#             )
#             assert res.status_code == 201

#             res = requests.delete(
#                 f"{BASE_URL}/products/{name}",
#                 headers={"Role": "admin"},
#                 timeout=self.TIMEOUT
#             )
#             assert res.status_code == 200
#         duration = time.time() - start
#         assert duration < 5

#     def test_repeated_warehouse_in(self):
#         name = self.random_name()

#         res = requests.post(
#             f"{BASE_URL}/products",
#             json={"name": name, "quantity": 5, "price": 10},
#             timeout=self.TIMEOUT
#         )
#         assert res.status_code == 201

#         start = time.time()

#         for _ in range(200):
#             res = requests.post(
#                 f"{BASE_URL}/warehouse/in",
#                 json={"name": name, "amount": 5},
#                 timeout=self.TIMEOUT
#             ) 
#             assert res.status_code == 200

#         duration = time.time() - start
#         assert duration < 5


