class ResponseBody:
    def __init__(self, logger, request_id, operation_id):
        self.logger = logger
        self.request_id = request_id
        self.operation_id = operation_id

    def success(self, data=None):
        if(data is None):
            return {"request_id": self.request_id, "return-code": "200", "message": "Success", "data": [], "operation_id": self.operation_id}
        else:
            return {"request_id": self.request_id, "return-code": "200", "message": "Success", "data": data, "operation_id": self.operation_id}
    
    def error(self, message):
        self.logger.error(message)
        if(len(message.args) == 1):
            code = "400"
            detail_message = "Internal Server Error"
        else:
            code, detail_message = message.args
        return {"request_id": self.request_id, "return-code": f"{code}", "message": detail_message, "data": [], "operation_id": self.operation_id}
