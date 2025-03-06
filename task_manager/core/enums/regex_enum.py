from enum import Enum


class TaskRegEx(Enum):
    TITLE = (
        r'^[A-Z][\w]{1,30}',
        'Start from uppercase, from 2 to 20 letters'
    )
    
    def __init__(self, pattern:str, msg:str):
        self.pattern = pattern
        self.msg = msg