'''
Required restart after making changes, as the script call it one time only upon starting service.
'''
import pymysql

import config


# Custom exception
class DataNotFound(Exception):
    """Couldn't find any related data from the database
    """
    def __init__(self):
        # equivalent to Exception("404", "Data not found")
        # use together with parent try-catch block Exception().args to format return code & message
        super().__init__("404", "Data not found")

class InternalServerError(Exception):
    """Couldn't find any related data from the database
    """
    def __init__(self):
        # equivalent to Exception("404", "Data not found")
        # use together with parent try-catch block Exception().args to format return code & message
        super().__init__("400", "Internal server error")


# Database operation
class DatabaseAction:
    def __init__(self, logger, operation_id, unittest=None):
        self.logger = logger
        self.operation_id = operation_id
        self.unittest = unittest
        self.conn = self.open_connection()   # Establish connection


    def open_connection(self):
        # unit test
        conn = pymysql.connect(host=config.host_db,
                            port=config.port_db,
                            user=config.username_db,
                            password=config.password_db,
                            db=config.database_db,
                            connect_timeout=10,
                            read_timeout=60,
                            write_timeout=60)
        return conn


    def close_connection(self):
        self.conn.close()


    def insert_item(self, user, item):
        insert_query = """INSERT INTO todolist (item, owner) VALUES (%(item)s, %(user)s)"""

        # unit test
        if(self.unittest == "internal_server_error"):
            # Expect code 400
            raise InternalServerError
        if(self.unittest == "operational_error"):
            # Expect code 1054
            insert_query = """INSERT INTO todolist (item, ownersss) VALUES (%(item)s, %(user)s)"""
        if(self.unittest == "programming_error"):
            # Expect code 1064
            insert_query = """INSERT INTOOOO todolist (item, owner) VALUES (%(item)s, %(user)s)"""
        if(self.unittest == "data_error"):
            # Expect code 1366
            insert_query = """INSERT INTO todolist (status, owner) VALUES (%(item)s, %(user)s)"""

        cursor = self.conn.cursor()
        cursor.execute(insert_query, {"user": user, "item": item})    # SQL Injection safe
        self.conn.commit()
        cursor.close()


    def delete_item(self, user, item):
        select_query = """SELECT * FROM todolist WHERE owner=%(user)s AND item=%(item)s"""
        delete_query = """DELETE FROM todolist WHERE owner=%(user)s AND item=%(item)s"""

        # unit test
        if(self.unittest == "internal_server_error"):
            # Expect code 400
            raise InternalServerError
        if(self.unittest == "data_not_found"):
            # Expect code 404
            select_query = """SELECT * FROM todolist WHERE owner='data_not_found' AND item='data_not_found'"""
        if(self.unittest == "operational_error"):
            # Expect code 1054
            select_query = """SELECT * FROM todolist WHERE ownersss=%(user)s"""
        if(self.unittest == "programming_error"):
            # Expect code 1064
            select_query = """SELECTTTT * FROM todolist WHERE owner=%(user)s"""

        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(select_query, {"user": user, "item": item})
        results = cursor.fetchall()
        self.logger.info(results)
        if(len(results) < 1):
            raise DataNotFound
        elif(len(results) >= 1):
            cursor.execute(delete_query, {"user": user, "item": item})    # SQL Injection safe
            self.conn.commit()
        cursor.close()


    def select_item(self, user):
        select_query = """SELECT * FROM todolist WHERE owner=%(user)s"""

        # unit test
        if(self.unittest == "internal_server_error"):
            # Expect code 400
            raise InternalServerError
        if(self.unittest == "data_not_found"):
            # Expect code 404
            select_query = """SELECT * FROM todolist WHERE owner='data_not_found' AND item='data_not_found'"""
        if(self.unittest == "operational_error"):
            # Expect code 1054
            select_query = """SELECT * FROM todolist WHERE ownersss=%(user)s"""
        if(self.unittest == "programming_error"):
            # Expect code 1064
            select_query = """SELECTTTT * FROM todolist WHERE owner=%(user)s"""

        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(select_query, {"user": user})  # SQL Injection safe
        results = cursor.fetchall()
        self.logger.info(f"select_item() results: {results}")
            
        if(len(results) < 1):
            raise DataNotFound
        cursor.close()
        print(results)
        return results


    def update_item(self, user, item):
        select_query = """SELECT * FROM todolist WHERE owner=%(user)s AND item=%(item)s"""
        update_query = """UPDATE todolist SET status = %(status)s WHERE owner=%(user)s AND item=%(item)s"""

        # unit test
        if(self.unittest == "internal_server_error"):
            # Expect code 400
            raise InternalServerError
        if(self.unittest == "data_not_found"):
            # Expect code 404
            select_query = """SELECT * FROM todolist WHERE owner='data_not_found' AND item='data_not_found'"""
        if(self.unittest == "operational_error"):
            # Expect code 1054
            select_query = """SELECT * FROM todolist WHERE ownersss=%(user)s"""
        if(self.unittest == "programming_error"):
            # Expect code 1064
            select_query = """SELECTTTT * FROM todolist WHERE owner=%(user)s"""

        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(select_query, {"user": user, "item": item})
        results = cursor.fetchall()
        self.logger.info(results)
        if(len(results) < 1):
            raise DataNotFound
        elif(len(results) >= 1):
            update_status=0
            self.logger.info(update_status)
            if(results[0]["status"] == 0):
                update_status=1
            self.logger.info(update_status)
            cursor.execute(update_query, {"user": user, "item": item, "status": update_status})
            self.conn.commit()
        cursor.close()
