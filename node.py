class Node:
    def __init__(self, node_info, line, is_Hub):
        node_info = node_info.split(':')
        self.__id = node_info[0]
        self.__name = node_info[1]
        self.__line = line
        self.__current_train = None
        self.is_Hub = is_Hub
        if is_Hub:
            self.__conn_line = node_info[3]

    
    def __str__(self):
        return self.get_id() + ' ' + self.get_name()

    # GET, SET PAIRS:
    # id
    def get_id(self):
        return self.__id

    # name
    def get_name(self):
        return self.__name
    
    # line
    def get_line(self):
        return self.__line
    
    # train
    def set_train(self, train):
        self.__current_train = train
    
    def get_train(self):
        return self.__current_train
    
    # METHOD FOR HUB:
    def switch_line(self):
        hub_name = self.get_name()
        conn_line = self.get_conn_line()
        hubs_in_conn_line = conn_line.get_hubs_in_line()

        if hub_name not in hubs_in_conn_line:
            print('This hub is not in {}'.format(conn_line.get_name()))

        for hub in hubs_in_conn_line:
            if hub_name == hub:
                return hub
        print('No switch')

    def get_conn_line(self):
        return self.__conn_line
    
    