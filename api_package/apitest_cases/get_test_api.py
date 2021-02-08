from selenium import webdriver
import requests
import json
import jsonpath

# get api
url = "https://reqres.in/api/users?page=2"
v_response = requests.get(url)
print("------------API response--------------")
print(v_response.text)

# api response status code
v_statuscode = v_response.status_code
print("-------Response code----------")
print(v_statuscode)

#convert data into json
json_data = json.loads(v_response.text)
print("------Json Data---------")
print(json_data)

#get per page value
v_per_page = jsonpath.jsonpath(json_data,"per_page")
print("----Per page value------")
print(v_per_page)

assert v_statuscode == 200
assert v_per_page[0] == 6