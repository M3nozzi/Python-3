from main import get_temperature
import pytest
import requests


class MockResponse:
    @staticmethod
    def json():
        return {"currently": {"temperature": 62}}

@pytest.fixture
def mock_res(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse

    monkeypatch.setattr(requests, "get", mock_get)

def test_get_temperature_by_lat_lng(mock_res):
    exp = get_temperature(-14.235004, -51.92528)
    assert exp == 16

