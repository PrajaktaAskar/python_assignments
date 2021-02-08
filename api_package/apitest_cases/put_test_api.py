import requests
import json
import jsonpath

#put url
url= "https://reqres.in/api/users/2"

#read input data
f_pointer = open("/api_package/files/sample_data_put.json", mode ='r')
v_input_data = f_pointer.read()

#conver data to json/dic
v_input_json_data = json.loads(v_input_data)

#get response
v_response= requests.put(url,v_input_json_data)
print(v_response.text)

#statuscode
v_statuscode= v_response.status_code
print(v_statuscode)

#load response in json
json_data= json.loads(v_response.text)
print(json_data)

#test with jsonpath
v_name = jsonpath.jsonpath(json_data,"name")
print(v_name)
v_job = jsonpath.jsonpath(json_data,"job")

assert v_name[0] == "morpheus"
assert v_statuscode == 200


