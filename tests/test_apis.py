import requests
import pytest

#
# url invocation examples are here: https://realpython.com/api-integration-in-python/
#

def test_get_employees():
    api_url = "http://localhost:5000/employees"
    response = requests.get(api_url)
    assert response.status_code == 200, "Unable to get employees"

    print(response.json())

def test_sample1_method1():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"



