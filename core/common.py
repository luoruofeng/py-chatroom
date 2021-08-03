
import json
from enum import Enum


class MessageType(Enum):
    TXT = 1
    IMAGE = 2
    VOICE =3

def create_message(name: str,content: str,type: int,mt: MessageType = 1) -> str:
    dict = {'name':name,'content':content,'mt':mt}
    return json.dumps(dict)