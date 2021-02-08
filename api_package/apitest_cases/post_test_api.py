import requests
import json
import jsonpath

#post url
url = "https://reqres.in/api/users"

#input data for posting
f_pointer = open("D:\\workspace_python\\Python_Assignments\\api_package\\files\\sample_data.json", mode ='r')
v_input_data = f_pointer.read()
print("input data:" + str(v_input_data))

#convert data to json
v_input_data_json = json.loads(v_input_data)
print("input data with json:" + str(v_input_data_json))

v_response = requests.post(url,v_input_data_json)
print(v_response.text)

#status code
v_statuscode = v_response.status_code
print("StatusCode is: "+ str(v_statuscode))

#load data into json
v_response_json = json.loads(v_response.text)

#jsonpath to check
v_id = jsonpath.jsonpath(v_response_json,"id")
print(v_id[0])

assert v_statuscode == 201

