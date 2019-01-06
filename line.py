
class Line:
    def __init__(self, name):
        self.__name = name
        self.__nodes_in_line = []
        self.__hubs_in_line = []
    
    def __str__(self):
        return self.get_name()

    def get_name(self):
        return self.__name

    def add_hubs_in_line(self, hub_obj):
        self.__hubs_in_line.append(hub_obj)
    
    def get_nodes_in_line(self):
        return self.__nodes_in_line

    def add_nodes_in_line(self, node_obj):
        self.__nodes_in_line.append(node_obj)
    
    def get_hubs_in_line(self):
        return self.__hubs_in_line
