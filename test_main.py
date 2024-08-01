import requests

BASE_URL = "http://127.0.0.1:8000"  # Assuming the FastAPI server runs on this URL

def test_read_root():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_read_item():
    item_id = 1
    query = "test"
    response = requests.get(f"{BASE_URL}/items/{item_id}?q={query}")
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id, "q": query}

def test_greet_name():
    name = "John"
    response = requests.get(f"{BASE_URL}/hello/{name}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello, {name}"}

def test_get_day():
    response = requests.get(f"{BASE_URL}/day")
    assert response.status_code == 200
    assert "day" in response.json()

def test_get_day_of_month():
    response = requests.get(f"{BASE_URL}/day-of-month")
    assert response.status_code == 200
    assert "day_of_month" in response.json()

def test_get_current_time():
    response = requests.get(f"{BASE_URL}/current-time")
    assert response.status_code == 200
    assert "current_time" in response.json()

def test_get_prime_count():
    n = 10
    response = requests.get(f"{BASE_URL}/primes/{n}")
    assert response.status_code == 200
    assert response.json() == {"prime_count": 4}  # There are 4 primes less than 10: 2, 3, 5, 7

def test_birthday_true(monkeypatch):
    class MockDateTime:
        @classmethod
        def now(cls):
            return datetime.datetime(2023, 7, 31)
    
    monkeypatch.setattr(datetime, 'datetime', MockDateTime)
    response = requests.get(f"{BASE_URL}/birthday")
    assert response.status_code == 200
    assert response.json() == {"message": "Happy Birthday!"}

def test_birthday_false(monkeypatch):
    class MockDateTime:
        @classmethod
        def now(cls):
            return datetime.datetime(2023, 8, 1)
    
    monkeypatch.setattr(datetime, 'datetime', MockDateTime)
    response = requests.get(f"{BASE_URL}/birthday")
    assert response.status_code == 200
    assert response.json() == {"message": "Today is not your birthday."}