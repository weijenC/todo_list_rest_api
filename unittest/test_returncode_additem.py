import requests


endpoint_url="http://localhost:3000/add-item"
basic_header={'Content-Type': 'application/json'}
request_timeout=10
todo_user="unittest_returncode"
todo_item="buy apple"

def test_additem_200():
    print("\n========================================== Test Cases: add-item ==========================================")
    print("\nTesting API Return Code 200: Success")
    request_json = {"request_id": todo_user, "user": todo_user, "item": todo_item}
    response = requests.post(url=endpoint_url, json=request_json, headers=basic_header, timeout=request_timeout).json()
    assert response["return-code"]=="200"
    assert response["message"]=="Success"
    assert "data" in response.keys()
    assert type(response["data"]) is list
    assert len(response["data"]) == 0


def test_additem_400():
    print("\nTesting API Return Code 400: internal_server error")
    request_json = {"request_id": todo_user, "user": todo_user, "item": todo_item, "trigger_error": "internal_server_error"}
    response = requests.post(url=endpoint_url, json=request_json, headers=basic_header, timeout=request_timeout).json()
    assert response["return-code"]=="400"


def test_additem_1054():
    print("\nTesting API Return Code 1054: operational_error")
    request_json = {"request_id": todo_user, "user": todo_user, "item": todo_item, "trigger_error": "operational_error"}
    response = requests.post(url=endpoint_url, json=request_json, headers=basic_header, timeout=request_timeout).json()
    assert response["return-code"]=="1054"


def test_additem_1064():
    print("\nTesting API Return Code 1064: programming_error")
    request_json = {"request_id": todo_user, "user": todo_user, "item": todo_item, "trigger_error": "programming_error"}
    response = requests.post(url=endpoint_url, json=request_json, headers=basic_header, timeout=request_timeout).json()
    assert response["return-code"]=="1064"


def test_additem_1366():
    print("\nTesting API Return Code 1366: data_error")
    request_json = {"request_id": todo_user, "user": todo_user, "item": todo_item, "trigger_error": "data_error"}
    response = requests.post(url=endpoint_url, json=request_json, headers=basic_header, timeout=request_timeout).json()
    assert response["return-code"]=="1366"