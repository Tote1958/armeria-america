from dataclasses import dataclass

@dataclass
class ResponseMessage:
    message: str
    id: int
    data: dict = None
    
@dataclass
class ResponseBuilder:
    add_message: str
    add_status_code: int
    add_data: dict = None

    def add_message(self, message: str):
        self.add_message = message
    
    def add_status_code(self, status_code: int):
        self.add_status_code = status_code
    
    def add_data(self, data: dict):
        self.add_data = data

    def build(self):
        return ResponseMessage(
            message=self.add_message,
            status_code=self.add_status_code,
            data=self.add_data
        )