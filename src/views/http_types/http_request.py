from typing import Dict


class HttpRequest:
    def __init__(self, body: Dict = None, parameters: Dict = None) -> None:
        self.body = body
        self.parameters = parameters
