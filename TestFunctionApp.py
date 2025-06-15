import requests
import json

# Azure Function URL (adjust the function name and app name as needed)
function_url = "https://testfunccloud.azurewebsites.net/api/pythonfunction"

# Function key for authorization (if required)
function_key = "<>"  # Omit if Function access level is "Anonymous"

# Construct headers and payload
headers = {
    "Content-Type": "application/json"
}
payload = {
    "name": "Rekhu"  # Replace with the actual value you want to send
}

# Send POST request with function key in query string
response = requests.post(
    url=function_url,
    headers=headers,
    json=payload,
    params={"code": function_key} if function_key else {}
)

# Output response
print("Status Code:", response.status_code)
print("Response Body:", response.text)
