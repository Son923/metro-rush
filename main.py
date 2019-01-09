from utils import handling_argument, handling_data
from utils import generate_lines, generate_trains
from node import Node
from graph import Graph
from dfs import DFS

def set_up(data, start_info, end_info, total_train):
    start_node = Node(start_info[0], start_info[1], is_Hub = False)
    end_node = Node(end_info[0], end_info[1], is_Hub = False)
    lines = generate_lines(data)
    trains = generate_trains(total_train)
    return lines, trains, start_node, end_node

def main():
    filename, algo = handling_argument()
    data, start_info, end_info, total_train = handling_data(filename)
    
    lines, trains, start_node, end_node = set_up(data, start_info, end_info, total_train)

    train = trains[0]
    graph = Graph(lines, start_node, end_node)

    visited = DFS.apply(train, graph)
    print(list(visited))
    
    





    # # test structure
    # for line in lines:
    #     print(line)
    #     nodes = line.get_nodes_in_line()
    #     hubs = line.get_hubs_in_line()
    #     print('Nodes')
    #     for node in nodes:
    #         print(node)
    #     print()
    #     print('Hubs')
    #     for hub in hubs:
    #         print(hub)
    #         print(hub, '|conn:' + hub.get_conn_line())


if __name__ == "__main__":
    main()

