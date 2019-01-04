
def generate_trains(total_train):
    trains = [Train() for _ in range(total_train)]
    for index, train in enumerate(trains):
        train.set_name(str(index))
    return trains

class Train:
    def __init__(self):
        self.__name = 'T'
        self.__current = None
        self.__history = []
    
    def __str__(self):
        return self.get_name()
    
    def set_name(self, index):
        self.__name += index
        
    def get_name(self):
        return self.__name
    
    def set_current(self, node):
        self.__current = node
        self.__history.append(node)
    
    def get_current(self):
        return self.__current

    def get_history(self):
        return self.__history
    
    def move_next_node(self, next_node):
        pass
    
    def switch_line(self, line):
        pass