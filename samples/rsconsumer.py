import requests
import json
from types import SimpleNamespace

response = requests.get("http://localhost:5000/countries")
print(response.json())

x = json.loads(response.json(), object_hook=lambda d: SimpleNamespace(**d))

print(x)



