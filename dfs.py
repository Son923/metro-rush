from shortest_path_al import ShortestPathAlgorithm

class DFS(ShortestPathAlgorithm):
    @staticmethod
    def apply(trains, graph):
        dictio = graph.create_graph()
        start_node_name = graph.get_start_node()
        end_node_name = graph.get_end_node()
        return DFS.dfs_paths(dictio, start_node_name, end_node_name)
    
    @staticmethod
    def dfs(graph, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        for next in graph[start] - visited:
            DFS.dfs(graph, next, visited)
        return visited
    
    @staticmethod
    def dfs_paths(graph, start, goal):
        stack = [(start.split('-')[0], [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next in graph[vertex.split('-')[0]] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    # if len(graph[path[-1].split('-')[0]])>2 and path[-1].split('-')[-1] != next.split('-')[-1]:
                    stack.append((next, path + [next]))