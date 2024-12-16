import pytest
from app import app

@pytest.fixture
def client():
    """Test-Client für Flask-Anwendungen"""
    with app.test_client() as client:
        yield client

def test_add_order(client):
    """Testfall zum Hinzufügen eines neuen Auftrags"""

    # 1. Öffne die Add-Seite
    response = client.get('/add')
    assert response.status_code == 200  # Überprüfe, ob die Seite geladen wurde

    # 2. Füge einen neuen Auftrag hinzu
    response = client.post('/add', data={'name': 'Auftrag 1', 'description': 'Beschreibung 1'})
    assert response.status_code == 302  # 302: Weiterleitung zur Startseite
    
    # 3. Folge der Weiterleitung
    response = client.get(response.location)  # Folge der Weiterleitung (Startseite)
    
    # 4. Überprüfe, ob der Auftrag auf der Startseite angezeigt wird
    assert b'Auftrag 1' in response.data  # Überprüfe, ob der Auftrag auf der Startseite angezeigt wird

    # 5. Teste das Hinzufügen mit fehlenden Daten
    response = client.post('/add', data={'name': '', 'description': 'Beschreibung 2'})
    assert response.status_code == 200  # Sollte auf der Seite bleiben
    assert b'Fehlende Daten' in response.data  # Überprüfe, ob eine Fehlermeldung angezeigt wird
