import pymysql
import sys
sys.path.append("/opt/program/cognixus-app/app/")

import config


######################
# Initialization
######################
conn = pymysql.connect(host = config.host_db, port = config.port_db, user = config.username_db, password = config.password_db, db = config.database_db)
user = "service_db_user"
item = "service_db_item"

################################
# Test Cases: Database Functions
################################
def test_connection():
    print("\n========================================== Test Cases: Database Functions ==========================================")
    print("Testing Database: connection()")
    conn = pymysql.connect(host = config.host_db, port = config.port_db, user = config.username_db, password = config.password_db, db = config.database_db)
    
    assert type(conn) is pymysql.connections.Connection


def test_insert_item():
    print("\nTesting Database: insert_item()")

    insert_query = """INSERT INTO todolist (owner, item) VALUES (%(user)s, %(item)s)"""

    cursor = conn.cursor(pymysql.cursors.DictCursor)
    affected_rows = cursor.execute(insert_query, {"user": user, "item": item})
    conn.commit()

    assert affected_rows == 1
    print(affected_rows)


def test_select_item():
    print("\nTesting Database: select_item()")

    select_query = """SELECT * FROM todolist WHERE owner=%(user)s AND item=%(item)s"""

    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(select_query, {"user": user, "item": item})
    results = cursor.fetchall()
    print(results)

    assert type(results) is list
    assert len(results) == 1

    assert type(results[0]) is dict

    assert "owner" in results[0]
    assert type(results[0]["owner"]) is str
    assert results[0]["owner"] != ""
    assert results[0]["owner"] == user

    assert "item" in results[0]
    assert type(results[0]["item"]) is str
    assert results[0]["item"] != ""
    assert results[0]["item"] == item

    assert "status" in results[0]
    assert type(results[0]["status"]) is int
    assert results[0]["status"] == 0 or results[0]["status"] == 1


def test_update_item():
    print("\nTesting Database: update_item()")

    update_query = """UPDATE todolist SET status=1 WHERE owner=%(user)s AND item=%(item)s"""

    cursor = conn.cursor()
    affected_rows = cursor.execute(update_query, {"user": user, "item": item})
    conn.commit()

    assert affected_rows == 1
    print(affected_rows)


def test_delete_item():
    print("\nTesting Database: delete_item()")

    delete_query = """DELETE FROM todolist WHERE owner=%(user)s AND item=%(item)s"""

    cursor = conn.cursor()
    affected_rows = cursor.execute(delete_query, {"user": user, "item": item})
    conn.commit()
    print(affected_rows)

    assert affected_rows >= 1
