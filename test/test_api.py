# tests/test_api.py
import mongomock
import pytest
from app import create_app
from app.db import mongo
from bson.objectid import ObjectId

@pytest.fixture
def client(monkeypatch):
    """
    Create an app test client while monkeypatching mongo.init_app to use mongomock.
    """
    mock_client = mongomock.MongoClient()

    def fake_init_app(app):
        # set client and db the same way app's PyMongoWrapper does
        app.mongo_client = mock_client
        app.db = mock_client["testdb"]

    # Replace the real init_app with our fake
    monkeypatch.setattr(mongo, "init_app", fake_init_app)

    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c

def test_create_and_list_customer(client):
    # Create a customer
    rv = client.post("/api/customers", json={"name": "Alice", "email": "alice@example.com"})
    assert rv.status_code == 201
    data = rv.get_json()
    assert data["name"] == "Alice"
    assert "id" in data and isinstance(data["id"], str)

    # List customers
    rv2 = client.get("/api/customers")
    assert rv2.status_code == 200
    customers = rv2.get_json()
    assert isinstance(customers, list)
    assert any(c["email"] == "alice@example.com" for c in customers)

def test_unique_email_enforced(client):
    # Create first customer
    r1 = client.post("/api/customers", json={"name": "Bob", "email": "bob@example.com"})
    assert r1.status_code == 201

    # Try to create duplicate email
    r2 = client.post("/api/customers", json={"name": "Bobby", "email": "bob@example.com"})
    # app should return 409 Conflict or 400 depending on implementation
    assert r2.status_code in (400, 409)

def test_create_order_for_customer(client):
    # create customer
    r = client.post("/api/customers", json={"name": "C", "email": "c@example.com"})
    assert r.status_code == 201
    cid = r.get_json()["id"]

    # create order using that customer id
    r2 = client.post("/api/orders", json={"customer_id": cid, "item": "ball", "amount": 9.99})
    assert r2.status_code == 201
    order = r2.get_json()
    assert order["item"] == "ball"
    assert float(order["amount"]) == 9.99

def test_get_order_not_found(client):
    # Use a random ObjectId that won't exist
    fake_id = str(ObjectId())
    r = client.get(f"/api/orders/{fake_id}")
    assert r.status_code == 404
