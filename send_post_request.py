import requests
import json

url = 'http://127.0.0.1:5000/test'
data = {
    "Ambient Temperature": 25,
    "Calibration": 1,
    "Unwanted substance deposition": 0,
    "Humidity": 50,
    "H2S Content": 0.5,
    "detected by": 1
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json())
