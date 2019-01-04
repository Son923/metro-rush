from node import Node

class Hub(Node):
    def __init__(self, node_info, line):
        super().__init__(node_info, line)
        self.conn_line = node_info[3]

    def get_conn_line(self):
        return self.conn_line