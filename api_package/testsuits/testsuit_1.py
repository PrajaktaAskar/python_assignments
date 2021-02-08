import json
import requests
import jsonpath


def test_get():
    url = "https://reqres.in/api/users?page=2"
    v_response = requests.get(url)
    v_statuscode = v_response.status_code
    print("Total Time of completion: " + str(v_response.elapsed.total_seconds()))
    json_data = json.loads(v_response.text)
    v_per_page = jsonpath.jsonpath(json_data, "per_page")
    assert v_statuscode == 200
    assert v_per_page[0] == 6


def test_delete():
    url = "https://reqres.in/api/users/2"
    response = requests.delete(url)
    v_reponse_data = response.text
    v_statuscode = response.status_code
    print("Status Code is: " + str(v_statuscode))
    assert len(v_reponse_data) == 0
    assert v_statuscode == 204


def test_post():
    try:
        url = "https://reqres.in/api/users"
        f_pointer = open("D:\\workspace_python\\Python_Assignments\\api_package\\files\\sample_data.json", mode='r')
        v_input_data = f_pointer.read()
        v_input_data_json = json.loads(v_input_data)
        v_response = requests.post(url, v_input_data_json)
        print("Total Time of completion: " + str(v_response.elapsed.total_seconds()))

        v_statuscode = v_response.status_code
        print("StatusCode is: " + str(v_statuscode))
        v_response_json = json.loads(v_response.text)
        v_id = jsonpath.jsonpath(v_response_json, "id")
        print("First ID from response: " + str(v_id[0]))
    except:
        print("Exception occurred in POST URL test")
    finally:
        assert v_statuscode == 201
        print("Testcase passed successfully")
