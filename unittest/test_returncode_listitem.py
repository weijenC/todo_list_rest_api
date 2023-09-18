import requests


endpoint_url="http://localhost:3000/list-all-item"
basic_header={'Content-Type': 'application/json'}
request_timeout=10
todo_user="unittest_returncode"
todo_item="buy apple"

def test_listitem_200():
    print("\n========================================== Test Cases: list-item ==========================================")
    print("\nTesting API Return Code 200: Success")
    request_json = {"request_id": todo_user, "user": todo_user, "item": todo_item}
    response = requests.post(url=endpoint_url, json=request_json, headers=basic_header, timeout=request_timeout).json()
    print(response)
    assert response["return-code"]=="200"
    assert response["message"]=="Success"
    assert "data" in response.keys()
    assert type(response["data"]) is list
    assert len(response["data"]) > 0


def test_listitem_400():
    print("\nTesting API Return Code 400: internal_server error")
    request_json = {"request_id": todo_user, "user": todo_user, "item": todo_item, "trigger_error": "internal_server_error"}
    response = requests.post(url=endpoint_url, json=request_json, headers=basic_header, timeout=request_timeout).json()
    print(response)
    assert response["return-code"]=="400"


def test_listitem_404():
    print("\nTesting API Return Code 404: data_not_found")
    request_json = {"request_id": todo_user, "user": todo_user, "item": todo_item, "trigger_error": "data_not_found"}
    response = requests.post(url=endpoint_url, json=request_json, headers=basic_header, timeout=request_timeout).json()
    print(response)
    assert response["return-code"]=="404"


def test_listitem_1054():
    print("\nTesting API Return Code 1054: operational_error")
    request_json = {"request_id": todo_user, "user": todo_user, "item": todo_item, "trigger_error": "operational_error"}
    response = requests.post(url=endpoint_url, json=request_json, headers=basic_header, timeout=request_timeout).json()
    print(response)
    assert response["return-code"]=="1054"


def test_listitem_1064():
    print("\nTesting API Return Code 1064: programming_error")
    request_json = {"request_id": todo_user, "user": todo_user, "item": todo_item, "trigger_error": "programming_error"}
    response = requests.post(url=endpoint_url, json=request_json, headers=basic_header, timeout=request_timeout).json()
    print(response)
    assert response["return-code"]=="1064"
