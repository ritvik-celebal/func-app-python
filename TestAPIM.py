import requests

# === Required Config ===
apim_base_url = "https://testami.azure-api.net"
api_path = "/python/pythonfunction"
subscription_key = "<>"

# === POST Body (JSON)
json_data = {
    "name": "test2"
}

# === Headers (include subscription key and content type)
headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-Type": "application/json"
}

# === Make the POST request
response = requests.post(f"{apim_base_url}{api_path}", headers=headers, json=json_data)

# === Print the response
print("Status code:", response.status_code)
print("Response body:", response.text)
