import pytest
from flask import Flask
from app import app, orders

# Fixture, um den Flask-Testclient zu erstellen
@pytest.fixture
def client():
    app.config['TESTING'] = True  # Setze die Testumgebung
    with app.test_client() as client:
        yield client

def test_index(client):
    """Testet die Startseite"""
    # Rufe die Startseite auf
    response = client.get('/')
    
    # Überprüfe, ob der Statuscode 200 ist (OK)
    assert response.status_code == 200
    
    # Überprüfe, ob keine Aufträge angezeigt werden (zu Beginn sind keine Aufträge vorhanden)
    assert 'Keine Aufträge' in response.data.decode('utf-8')


def test_add_order(client):
    """Testet das Hinzufügen eines neuen Auftrags"""
    # Sende POST-Anfrage, um einen neuen Auftrag hinzuzufügen
    response = client.post('/add', data={'name': 'Auftrag 1', 'description': 'Beschreibung 1'})
    
    # Überprüfe, ob eine Weiterleitung auf die Startseite erfolgt (Statuscode 302)
    assert response.status_code == 302
    
    # Überprüfe, ob der Auftrag jetzt auf der Startseite angezeigt wird
    response = client.get('/')
    assert b'Auftrag 1' in response.data
    assert b'Beschreibung 1' in response.data


