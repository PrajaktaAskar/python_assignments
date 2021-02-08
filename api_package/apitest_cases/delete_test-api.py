import requests
import json
import jsonpath

#delete url
url= "https://reqres.in/api/users/2"

response= requests.delete(url)
v_reponse_data = response.text
v_statuscode= response.status_code
print(v_statuscode)

assert len(v_reponse_data) == 0
assert v_statuscode == 206