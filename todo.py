from datetime import date
from enum import Enum
from uuid import uuid4


class Status(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    COMPLETED = 2


class Priority(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2


class Item():
    __creation_date = date.today()
    __title = "empty"
    __status = Status.NOT_STARTED
    __priority = Priority.LOW
    __flag = False
    __url = ""
    __due_date = date
    __state = False
    __notes = ""
    __incon = ""
    

    def __init__(self, title:str=None):
        if title is not None:
            self.__title = title
        self.__id = str(uuid4)


    @property
    def title(self)->str:
        """Returns the title of the item"""
        return self.__title
    @property
    def creation_date(self)->date:
        """Returns the creation date of the item"""
        return self.__creation_date
    @property
    def status(self)->Status:
        """Returns the status of the item"""
        return self.__status
    @property
    def priority(self)->Priority:
        """Returns the priority of the item"""
        return self.__priority
    @property
    def notes(self)->str:
        """Returns the notes of the item"""
        return self.__notes


    @title.setter
    def title(self, value):
        self.__title = value
    @creation_date.setter
    def creation_date(self, value):
        self.__creation_date = value
    @status.setter
    def status(self, value):
        self.__status = value
    @priority.setter
    def priority(self, value):
        self.__priority = value
    @notes.setter
    def notes(self, value):
        self.__notes = value

    