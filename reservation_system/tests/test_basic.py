# import logging
# import pytest
# import requests
# import random
# import string
# from datetime import datetime, timedelta, timezone
# from dateutil.parser import parse


# BASE_URL = "http://localhost:8000"


# @pytest.fixture(scope="module")
# def base_url():
#     return BASE_URL

# def generate_random_email(role):
#     return f"test_{role}_{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}@example.com"


# def register_user(base_url, role):
#     user_data = {
#         "name": f"Test {role.capitalize()}",
#         "email": generate_random_email(role),
#         "password": "testpassword123",
#         "role": role
#     }
    
#     response = requests.post(f"{base_url}/register", json=user_data)
#     assert response.status_code == 200, f"{role.capitalize()} registration failed: {response.text}"
#     return response.json()["id"], user_data["email"], user_data["password"]

# def login_user(base_url, email, password):
#     login_data = {
#         "username": email,
#         "password": password
#     }
#     response = requests.post(f"{base_url}/token", data=login_data)
#     assert response.status_code == 200, f"Login failed: {response.text}"
#     return response.json()["access_token"]

