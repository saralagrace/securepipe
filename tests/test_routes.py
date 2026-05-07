import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_tickets_vide(client):
    res = client.get("/tickets")
    assert res.status_code == 200
    assert res.get_json() == []

def test_creer_ticket(client):
    res = client.post("/tickets", json={"title": "Bug critique"})
    assert res.status_code == 201
    assert res.get_json()["title"] == "Bug critique"

def test_creer_ticket_sans_titre(client):
    res = client.post("/tickets", json={})
    assert res.status_code == 400

def test_get_ticket_inexistant(client):
    res = client.get("/tickets/999")
    assert res.status_code == 404