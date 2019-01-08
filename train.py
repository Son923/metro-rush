class Train:
    def __init__(self):
        self.__name = 'T'
        self.__current_node = None
        self.__history = []
        self.__path = []
        self.__graph = None
    
    def __str__(self):
        return self.get_name()

    # GET, SET PAIRS:
    # graph
    def set_graph(self, graph_obj):
        self.__graph = graph_obj
    
    def get_graph(self):
        return self.__graph
    
    # name
    def set_name(self, index):
        self.__name += index
        
    def get_name(self):
        return self.__name
    
    # current_node
    def set_current_node(self, node):
        self.__current_node = node
        self.__history.append(node)
    
    def get_current_node(self):
        return self.__current_node
    
    # path
    def set_path(self, path):
        self.__path = path
    
    def get_path(self):
        return self.__path
    
    # history
    def add_history(self, next_node):
        self.__history.append(next_node)

    def get_history(self):
        return self.__history
    
    # METHODS:
    def move_next_node(self, next_node):
        path = self.get_path()
        next_node = path[path.index(self.get_current_node()) + 1]
        
        if self.is_available_node(next_node):
            self.set_current_node(next_node)
        self.add_history(self.get_current_node())
    
    def switch_line(self, line):
        pass
    
    def is_available_node(self, node):
        if node.get_current() is not None:
            return False
        return True
    
    def update_path(self):
        graph = self.get_graph()
        new_path = graph.find_path(self.get_current_node())
        self.set_path(new_path)
