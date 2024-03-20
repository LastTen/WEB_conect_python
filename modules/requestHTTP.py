import http.client
import os
from dotenv import load_dotenv


url = os.getenv("URL")
path = "/api"
data = "key=value"

conn = http.client.HTTPConnection(url)
headers = {"Content-type": "application/x-www-form-urlencoded"}

conn.request("POST", path, data, headers)
response = conn.getresponse()

print(response.status)
print(response.read().decode())
