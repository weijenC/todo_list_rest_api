import pytest
import logging
from uuid import uuid4

import sys
sys.path.append("/opt/program/cognixus-app/app/")
from database.operation import DatabaseAction


######################
# Initialization
######################
user = "exception_db_user"
item = "exception_db_item"

logger = logging.getLogger()
operation_id = str(uuid4())


# insert_item()
def test_exception_additem_internal_server_error():
    conn_object = DatabaseAction(logger, operation_id, unittest="internal_server_error")
    with pytest.raises(Exception) as exc_info:
        conn_object.insert_item(user, item)

    assert exc_info.value.args[0] == "400"
    assert exc_info.value.args[1] == "Internal server error"

def test_exception_additem_tbd():
    conn_object = DatabaseAction(logger, operation_id, unittest="operational_error")
    with pytest.raises(Exception) as exc_info:
        conn_object.insert_item(user, item)

    assert f"{exc_info.value.args[0]}" == "1054"

def test_exception_additem_tbd():
    conn_object = DatabaseAction(logger, operation_id, unittest="programming_error")
    with pytest.raises(Exception) as exc_info:
        conn_object.insert_item(user, item)

    assert f"{exc_info.value.args[0]}" == "1064"

def test_exception_additem_tbd():
    conn_object = DatabaseAction(logger, operation_id, unittest="data_error")
    with pytest.raises(Exception) as exc_info:
        conn_object.insert_item(user, item)

    assert f"{exc_info.value.args[0]}" == "1366"


# select_item()
def test_exception_listitem_internal_server_error():
    conn_object = DatabaseAction(logger, operation_id, unittest="internal_server_error")
    with pytest.raises(Exception) as exc_info:
        conn_object.select_item(user)

    assert exc_info.value.args[0] == "400"
    assert exc_info.value.args[1] == "Internal server error"

def test_exception_listitem_data_not_found():
    conn_object = DatabaseAction(logger, operation_id, unittest="data_not_found")
    with pytest.raises(Exception) as exc_info:
        conn_object.select_item(user)

    assert exc_info.value.args[0] == "404"
    assert exc_info.value.args[1] == "Data not found"

def test_exception_listitem_operational_error():
    conn_object = DatabaseAction(logger, operation_id, unittest="operational_error")
    with pytest.raises(Exception) as exc_info:
        conn_object.select_item(user)

    assert f"{exc_info.value.args[0]}" == "1054"

def test_exception_listitem_programming_error():
    conn_object = DatabaseAction(logger, operation_id, unittest="programming_error")
    with pytest.raises(Exception) as exc_info:
        conn_object.select_item(user)

    assert f"{exc_info.value.args[0]}" == "1064"


# update_item()
def test_exception_markitem_internal_server_error():
    conn_object = DatabaseAction(logger, operation_id, unittest="internal_server_error")
    with pytest.raises(Exception) as exc_info:
        conn_object.update_item(user, item)

    assert exc_info.value.args[0] == "400"
    assert exc_info.value.args[1] == "Internal server error"

def test_exception_markitem_data_not_found():
    conn_object = DatabaseAction(logger, operation_id, unittest="data_not_found")
    with pytest.raises(Exception) as exc_info:
        conn_object.update_item(user, item)

    assert exc_info.value.args[0] == "404"
    assert exc_info.value.args[1] == "Data not found"

def test_exception_markitem_operational_error():
    conn_object = DatabaseAction(logger, operation_id, unittest="operational_error")
    with pytest.raises(Exception) as exc_info:
        conn_object.update_item(user, item)

    assert f"{exc_info.value.args[0]}" == "1054"

def test_exception_markitem_programming_error():
    conn_object = DatabaseAction(logger, operation_id, unittest="programming_error")
    with pytest.raises(Exception) as exc_info:
        conn_object.update_item(user, item)

    assert f"{exc_info.value.args[0]}" == "1064"


# delete_item()
def test_exception_deleteitem_internal_server_error():
    conn_object = DatabaseAction(logger, operation_id, unittest="internal_server_error")
    with pytest.raises(Exception) as exc_info:
        conn_object.delete_item(user, item)

    assert exc_info.value.args[0] == "400"
    assert exc_info.value.args[1] == "Internal server error"

def test_exception_deleteitem_data_not_found():
    conn_object = DatabaseAction(logger, operation_id, unittest="data_not_found")
    with pytest.raises(Exception) as exc_info:
        conn_object.delete_item(user, item)

    assert exc_info.value.args[0] == "404"
    assert exc_info.value.args[1] == "Data not found"

def test_exception_deleteitem_operational_error():
    conn_object = DatabaseAction(logger, operation_id, unittest="operational_error")
    with pytest.raises(Exception) as exc_info:
        conn_object.delete_item(user, item)

    assert f"{exc_info.value.args[0]}" == "1054"

def test_exception_deleteitem_programming_error():
    conn_object = DatabaseAction(logger, operation_id, unittest="programming_error")
    with pytest.raises(Exception) as exc_info:
        conn_object.delete_item(user, item)

    assert f"{exc_info.value.args[0]}" == "1064"
