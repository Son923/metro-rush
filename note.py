dict_instance = {l1: [{s1:[{l2: [p2, p22, p222]}, {l3: [p3]}, {}, {}]}, s2, s3], l2: [], l3: []}
    dict_instance = {l1: [(1, abc, redline), s2, s3],
                     l2: [],
                     l3: []}

A = last_train
total_turn = turns_A_wait + turns_A_reach_end

turns_A_reach_end?? (min path for A)
turns_A_wait?? (number of branch,...)

ratio = turns_A_reach_end?? / turns_A_wait??

Conclusion:
Find path for 1st train so that last_train's turn is smallest (minimum of line changes)
total_turn = turns_last_train_wait + turns_that_last_train_reach_end


def parse_file(filename):
    return data 

def create_nodes(data):
    return nodes

def create_lines(nodes):
    return lines 

def create_graph(lines):
    return graph

def main():
    nodes = create_nodes(data)
    lines = create_lines(nodes)
    graph = create_graph(line)
    result = execute_algo(graph)
    return result