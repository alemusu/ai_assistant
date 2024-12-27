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
    __title = "empty"
    __id = ""
    __creation_date = date.today()
    __status = Status.NOT_STARTED
    __priority = Priority.LOW
    __flag = False
    __url = ""
    __due_date = date
    __state = False
    __notes = ""
    __icon = ""

    def __init__(self, title:str=None):
        if title is not None:
            self.__title = title
        self.__id = str(uuid4)

    @property
    def title(self)->str:
        """Returns the title of the item"""
        return self.__title
    @property
    def id(self)->str:
        """Returns the id of the item"""
        return self.__id
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
    def flag(self)->bool:
        """Returns the flag of the item"""
        return self.__flag
    @property
    def url(self)->str:
        """Returns the url of the item"""
        return self.__url
    @property
    def due_date(self)->date:
        """Returns the due date of the item"""
        return self.__due_date
    @property
    def state(self)->bool:
        """Returns the state of the item"""
        return self.__state
    @property
    def notes(self)->str:
        """Returns the notes of the item"""
        return self.__notes
    @property
    def icon(self)->str:
        """Returns the icon of the item"""
        return self.__icon
    @property
    def age(self)->date:
        """Returns the age of the item"""
        return self.creation_date - date.today()

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
    @flag.setter
    def flag(self, value):
        self.__flag = value
    @url.setter
    def url(self, value):
        self.__url = value
    @due_date.setter
    def due_date(self, value):
        self.__due_date= value
    @state.setter
    def state(self, value):
        self.__state = value
    @notes.setter
    def notes(self, value):
        self.__notes = value
    @icon.setter
    def icon(self, value):
        self.__icon = value
    
class Todo():
    __todos = []

    def __init__(self):
        print("new todo list created")
        self._current = -1

    @property
    def items(self)->list:
        return self.__todos

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._current < self.__length__() -1:
            self._current += 1
            print(self.__todos[self._current].title)
            return self.__todos[self._current]
        else:
            self._current = -1
        raise StopIteration

    def __length__(self):
        return len(self.__todos)

    def new_item(self, item:Item):
        self.__todos.append(item)

    def show(self):
        print("*"*80)
        for item in self.__todos:
            print(item.title, item.status, item.priority, item.age)
        print("*"*80)

    def remove_item(self, uuid:str=None, title:str=None):
        if title is None and uuid is None:
            print("You need to provide some details for me to remove the item")
        elif uuid is None and title:
            for item in self.__todos:
                if item.title() == title:
                    self.__todos.remove(item)
                    return True
            pritn("Item with the title", title, "not found")
        else: #case uuid!=None
            self.__todos.remove(uuid)
            return True