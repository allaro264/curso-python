# Comó hacer peticiones a APIS con Python 
# con y sin dependincias 

# 1. Sin dependencias (díficil y sin dependencias)

import urllib.request
import json

# DEEPSEEK_API_KEY = "xxx"

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
response_json = response.json()
print(json[0])


# 3. Un Post
print("\nPOST:")
try:
    response = requests.post("https://jsonplaceholder.typicode.com/posts/", 
    json={
        "title": "midu",
        "body": "dev",
        "userId": 5
    })
    print(response.status_code)

except requests.excetions.RequestException as e:
    print(f"Error en la solicitud: {e}")


# 4. Un PUT 
print("\nPUT:")
try:
    response = requests.put("https://jsonplaceholder.typicode.com/posts/1", 
    json={
        "title": "midu",
        "body": "dev",
        "userId": 5
    })
    print(response.status_code)

except requests.excetions.RequestException as e:
    print(f"Error en la solicitud: {e}")

    # User la API de GPT-4o de OpenAI

#     OPENAI_KE="sk-XXXXXXXX"

#     import json

# def call_openai_gpt(api_key, prompt):
#     url = "https://api.openai.com/v1/chat/completions"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"bearer {api_key}"
#     }
#     data = {
#         "model": "gpt-4o-mini",
#         "messages": [{"role": "user", "content": prompt}]
#     }

#     response = requests.post(url, json=data, headers=headers)
#     return response.json()

# api_response = call_openai_gpt(OPENAI_KEY, "Esctibe un breve poema sobre la programación")

# print(json.dumps(api_response, indent=2))

# print(api_response["choises"][0]["message"]["content"])

# Llamar a la api de deep sheek

# import json

# def call_deepseek(api_key, prompt):
#     url = "https://api.deepseek.com/chat/completions"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"bearer {api_key}"
#     }
#     data = {
#         "model": "deepseek-chat",
#         "messages": [{"role": "user", "content": prompt}]
#     }

#     response = requests.post(url, json=data, headers=headers)
#     return response.json()

# api_response = call_deepseek(DEEPSEEK_API_KEY, "Esctibe un breve poema sobre la programación")

# print(json.dumps(api_response, indent=2))

# print(api_response["choises"][0]["message"]["content"])