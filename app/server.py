#!/usr/bin/python3
"""
First created on 2023-09-17

@author: Wei Jen
"""
import traceback
from uuid import uuid4
from datetime import datetime
from fastapi import FastAPI


import config
from utils.event_log import file_logging

from io_body.request import (
    RequestBodyAdd,
    RequestBodyDelete,
    RequestBodyList,
    RequestBodyMark
)
from io_body.response import ResponseBody
from database.operation import DatabaseAction


app = FastAPI()


################################
# Endpoints
################################
@app.post('/add-item')
async def add_item(inputbody: RequestBodyAdd):
    """
    inputbody: {
        request_id: str
        user: str
        item: str
        trigger_error: Optional[str]
    }
    """
    # Define Log
    operation_id = str(uuid4())
    logger = file_logging(operation_id, "/add-item", config.log_path+"todolist-"+datetime.now().strftime("%Y%m%d")+".log")
    logger.openfile()

    # Instantiate Response object
    response_object = ResponseBody(logger, inputbody.request_id, operation_id)

    try:
        logger.info("Executing endpoint /add-item")

        # Establish Database Connection
        conn_object = DatabaseAction(logger, operation_id, inputbody.trigger_error)

        # Run SQL
        conn_object.insert_item(inputbody.user, inputbody.item)

        # Close Database Connection
        conn_object.close_connection()

        # Close log file
        logger.closefile()

        # Return
        return response_object.success()
    except Exception as e:
        logger.error(traceback.format_exc().replace("\n", "/n"))
        logger.closefile()
        return response_object.error(e)


@app.post('/list-all-item')
async def list_all_item(inputbody: RequestBodyList):
    """
    inputbody: {
        request_id: str
        user: str
        trigger_error: Optional[str]
    }
    """
    # Define Log
    operation_id = str(uuid4())
    logger = file_logging(operation_id, "/list-all-item", config.log_path+"todolist-"+datetime.now().strftime("%Y%m%d")+".log")
    logger.openfile()

    # Instantiate Response object
    response_object = ResponseBody(logger, inputbody.request_id, operation_id)

    try:
        logger.info("Executing endpoint /list-all-item")

        # Establish Database Connection
        conn_object = DatabaseAction(logger, operation_id, inputbody.trigger_error)

        # Run SQL
        results = conn_object.select_item(inputbody.user)

        # Close Database Connection
        conn_object.close_connection()

        # Close log file
        logger.closefile()

        # Return
        return response_object.success(results)
    except Exception as e:
        logger.error(traceback.format_exc().replace("\n", "/n"))
        logger.closefile()
        return response_object.error(e)


@app.post('/mark-item')
async def mark_item(inputbody: RequestBodyMark):
    """
    inputbody: {
        request_id: str
        user: str
        item: str
        trigger_error: Optional[str]
    }
    """
    # Define Log
    operation_id = str(uuid4())
    logger = file_logging(operation_id, "/mark-item", config.log_path+"todolist-"+datetime.now().strftime("%Y%m%d")+".log")
    logger.openfile()

    # Instantiate Response object
    response_object = ResponseBody(logger, inputbody.request_id, operation_id)

    try:
        logger.info("Executing endpoint /mark-item")

        # Establish Database Connection
        conn_object = DatabaseAction(logger, operation_id, inputbody.trigger_error)

        # Run SQL
        conn_object.update_item(inputbody.user, inputbody.item)

        # Close Database Connection
        conn_object.close_connection()

        # Close log file
        logger.closefile()

        # Return
        return response_object.success()
    except Exception as e:
        logger.error(traceback.format_exc().replace("\n", "/n"))
        logger.closefile()
        return response_object.error(e)


@app.post('/delete-item')
async def delete_item(inputbody: RequestBodyDelete):
    """
    inputbody: {
        request_id: str
        user: str
        item: str
        trigger_error: Optional[str]
    }
    """
    # Define Log
    operation_id = str(uuid4())
    logger = file_logging(operation_id, "/delete-item", config.log_path+"todolist-"+datetime.now().strftime("%Y%m%d")+".log")
    logger.openfile()

    # Instantiate Response object
    response_object = ResponseBody(logger, inputbody.request_id, operation_id)

    try:
        logger.info("Executing endpoint /delete-item")

        # Establish Database Connection
        conn_object = DatabaseAction(logger, operation_id, inputbody.trigger_error)

        # Run SQL
        conn_object.delete_item(inputbody.user, inputbody.item)

        # Close Database Connection
        conn_object.close_connection()

        # Close log file
        logger.closefile()

        # Return
        return response_object.success()
    except Exception as e:
        logger.error(traceback.format_exc().replace("\n", "/n"))
        logger.closefile()
        return response_object.error(e)


################################
# Main
################################
if __name__ == '__main__':
    print("Please run command: '/opt/program/python-venv/ap_backend/bin/python3 /opt/program/python-venv/ap_backend/bin/gunicorn apws_main:app --bind 172.17.160.216:3000 --workers=16 --thread=8 --timeout 180 -k uvicorn.workers.UvicornWorker --daemon'")
    raise Exception("Please run command: '/opt/program/python-venv/ap_backend/bin/python3 /opt/program/python-venv/ap_backend/bin/gunicorn apws_main:app --bind 172.17.160.216:3000 --workers=16 --thread=8 --timeout 180 -k uvicorn.workers.UvicornWorker --daemon'")
