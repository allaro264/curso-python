# Comó hacer peticiones a APIS con Python 
# con y sin dependincias 

# 1. Sin dependencias (díficil y sin dependencias)

import urllib.request
import json
# api_posts = "https://jsonplaceholder.typicode.com/posts/"


# try:
#     response = urllib.request.urlopen(api_posts)
#     data = response.read()
#     json_data = json.loads(data.decode('utf-8'))
#     print(json_data)
#     response.close()
# except urllib.error.URLError as e:
#     print(f"Error en la solicitud: {e}")


# 2. Con dependencias (request)
import requests

print("\nGET:")
api_posts = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(api_posts)
json = response.json()
print(json[0])
