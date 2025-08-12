import pytest
import requests

def test_duckgo_instant_answer_api():
    # Arrange
    url = "https://api.duckduckgo.com/?q=python&format=json"

    # Act
    response = requests.get(url)
    body = response.json()
    print(body)

    # Assert
    data = response.json()
    assert response.status_code == 200