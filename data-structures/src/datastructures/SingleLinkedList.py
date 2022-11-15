# This class will create a node
class node:
    def __init__(self):
        self.__info = 0
        self.__next = None
    
    def set_info(self, info):
        self.__info = info
    
    def get_info(self):
        return self.__info
    
    def set_next(self, info):
        self.__next = info
    
    def get_next(self):
        return self.__next

class SingleLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0
    
    def insert_at_beginning(self, info):
        n = node()
        n.set_info(info)
        if self.__head is not None:
            n.set_next(self.__head)
        self.__head = n

    def insert_at_end(self, info):
        pass

    def insert_at_position(self, info, position:int):
        pass

    def delete_at_beginning(self):
        pass
    
    def delete_at_position(self, position:int):
        pass

    def delete_by_element(self, element):
        pass

    def display(self):
        pass

    def search(self, element, start:int, end:int):
        pass
