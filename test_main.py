from main import get_temperature
import pytest
import requests
from unittest.mock import Mock

class MockResponse:
    @staticmethod
    def json():
        return{"currently": {"temperature": 62}}

def test_get_temperature_by_lat_lng():
    raise NotImplementedError
