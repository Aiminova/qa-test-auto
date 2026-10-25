import os
import pytest
import requests

API_BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")
UI_BASE_URL = os.getenv("UI_BASE_URL", "https://www.saucedemo.com")


@pytest.fixture(scope="session")
def api():
    """One shared HTTP session reused by all API tests."""
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json; charset=UTF-8"})
    session.base_url = API_BASE_URL
    return session


@pytest.fixture(scope="session")
def base_url():
    """Base URL used by pytest-playwright for page.goto('/')."""
    return UI_BASE_URL
