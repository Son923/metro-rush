class Node:
    def __init__(self, node_info):
        self.__id = node_info[0]
        self.__name = node_info[1]
        self.__line = node_info[2]
        self.__current_train = ''

    def get_id(self):
        return self.__id
        
    def get_name(self):
        return self.__name
    
    def get_line(self):
        return self.__line
    
    def set_train(self, train):
        self.__current_train = train
    
    def get_train(self):
        return self.__current_train
    
    