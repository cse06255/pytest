import pytest
import json
import requests
import allure

def test_getUserinfo():
    resp = requests.get("https://reqres.in/api/users?page=2")
    print(resp)
    code = resp.status_code
    assert code == 200, "code does not match"
    json_response=resp.json()
    print(json_response['data'][0]['email'])
    token=json.loads(resp.text)
    print(token)
#@pytest.mark.skip
@allure.description("add user")
@allure.severity("Normal")
def test_addUser():
    mydata = open("C://Users//dell//AppData//Roaming//JetBrains//PyCharmCE2021.1//scratches//scratch_1.json",
                  "r").read()
    resp = requests.post("https://reqres.in/api/users", json.loads(mydata))
    print(resp.json())
    print(resp.status_code)
