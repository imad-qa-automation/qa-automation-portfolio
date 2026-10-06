import requests
import pytest

@pytest.fixture
def api_url():
    return "https://jsonplaceholder.typicode.com"

def test_get_utilisateur(api_url):
    response = requests.get(f"{api_url}/users/2")
    data = response.json()
    assert response.status_code == 200 
    assert data["name"] !="" 
   
def test_creer_utilisateur(api_url):

    nouvel_utilisateur = {
        "name": "Imad-Eddine",
        "username": "imad_qa",
        "email" : "imad@test.com"
    }

    response = requests.post(f"{api_url}/users", json=nouvel_utilisateur)
    data = response.json()
    assert response.status_code == 201

def test_utilisateur_introuvable (api_url):
    response = requests.get(f"{api_url}/users/9999")
    assert response.status_code == 404

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_plusieurs_utilisateurs(user_id,api_url):
    response = requests.get(f"{api_url}/users")
    assert response.status_code == 200 


