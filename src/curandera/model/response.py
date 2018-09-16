from typing import Text, List, TypeVar

Version = TypeVar('Version')

class Reply: pass

class Error:
    message: Text

class Progress:
    message: Text # Current action
    minimum: int
    maximum: int
    current: int

class Message:
    message: Text
    title: Text

class Hello:
    supported: List[Version]