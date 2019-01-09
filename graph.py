
class Graph():
    def __init__(self, lines, start_node, end_node):
        self.__lines = lines
        self.__start_node = start_node
        self.__end_node = end_node
    
    def get_line(self):
        return self.__lines
    
    def get_start_node(self):
        return self.__start_node.get_name() + '-' + self.__start_node.get_line()
    
    def get_end_node(self):
        return self.__end_node.get_name() + '-' + self.__end_node.get_line()
    
    def create_graph(self):
        lines = self.get_line()
        graph = {}
        for line in lines:
            nodes = line.get_nodes_in_line()
            for node in nodes:
                node_name = node.get_name()
                index = nodes.index(node)

                if node_name not in graph:
                    graph[node_name] = set()

                if index == 0:
                    graph[node_name].add(nodes[index + 1].get_name()+'-'+nodes[index + 1].get_line())
                elif index == len(nodes) - 1:
                    graph[node_name].add(nodes[index - 1].get_name()+'-'+nodes[index - 1].get_line())
                else:
                    graph[node_name].add(nodes[index - 1].get_name()+'-'+nodes[index - 1].get_line())
                    graph[node_name].add(nodes[index + 1].get_name()+'-'+nodes[index + 1].get_line())
    
        return graph

