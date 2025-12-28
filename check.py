import json
import requests

# API_URL = "https://restcountries.com/v3.1/independent?status=true"

# response = requests.get(API_URL,timeout=6)

# if response.status_code == 200:
#     data = response.json()
#     print(json.dumps(data, indent=2)) 
    
# else:
#     print(f" Error : {response.status_code}")
#     exit()



API_URL = "https://restcountries.com/v3.1/name/{}"

country = "nepal"   

response = requests.get(API_URL.format(country), timeout=6)

if response.status_code == 200:
    data = response.json()
    # print(json.dumps(data, indent=2))
    print(type(data))
    print(type(data[0]))
    print(type(data[0]["name"]))

else:
    print(f"Error : {response.status_code}")