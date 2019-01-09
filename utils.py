import sys


# ===========================================================================
def handling_argument():
    """
    Take user input, parse the argument and return a filename if it's exists.
    """
    import os
    import argparse

    ls_algorithm = ['dfs', 'cluster', 'super_cluster',
                    'two_opt', 'nearest']

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', help='name of file')
    parser.add_argument('--algo', dest='algorithm', help='name of algorithm')
    args = parser.parse_args()

    if args.filename is None or not os.path.exists(args.filename):
        raise FileNotFoundError()

    if args.algorithm is not None and args.algorithm not in ls_algorithm:
        print("SyntaxError: Algorithm not found!")
        exit(0)

    return args.filename, args.algorithm


# ===========================================================================
def handle_certain_data(alist):
    """
    Handling all start point, end point and the number of train.
    """
    for i, each in enumerate(alist):
        if i == len(alist):
            alist[i] = int(each.split('=')[1:][0])
        else:
            alist[i] = each.split('=')[1:][0].split(':')
    return alist


# ===========================================================================
def find_data(data, point):
    """
    Find name of start station and end station with its id and line name.
    """
    for item in data:
        if item[0] == point[0]:
            for each in item:
                alist = each.split(':')
                if alist[0] == point[1]:
                    return [alist[1]] + point


# ===========================================================================
def handling_data(file):
    """
    Open a target file, take data and return a list of data.
    """
    try:
        start_point, end_point, total_train = '', '', 0
        with open(file) as myfile:
            all_content = myfile.read().split('#')
            data = [each[:-1].split('\n') for each in all_content[1:-1]]

            ls_inform = handle_certain_data(all_content[-1].split('\n')[-3:-1])

            start_point = find_data(data, ls_inform[0])
            # print(start_point)
            start_info = ('{}:{}'.format(start_point[2], start_point[0]), start_point[1])
            end_point = find_data(data, ls_inform[1])
            end_info = ('{}:{}'.format(end_point[2], end_point[0]), end_point[1])
            total_train = 100

            all_content[-1] = '\n'.join(ls_inform[:-4])

        return data, start_info, end_info, total_train
    except IOError:
        print("Could not open file! Please close Excel!")


# ===========================================================================
def setup_value(line_name, alist, conn=False):
    """
    Set value in instance type for all stations and all transfer points.
    """
    from station import Station
    from hub import Hub

    ls_instance = []
    for item in alist:
        ls_inform = item.split(':')
        flag_set = False
        if conn and len(ls_inform) == 4:
            new_instance = Hub()
            new_instance.conn = ls_inform[-1]
            flag_set = True

        if not conn:
            new_instance = Station()
            flag_set = True

        if flag_set:
            new_instance.name = ls_inform[1]
            new_instance.line = line_name
            new_instance.id = ls_inform[0]

        if not conn or conn and len(ls_inform) == 4:
            ls_instance.append(new_instance)

    return ls_instance


# ===========================================================================
def setup_all_lines(list_data):
    """
    Make a list of instance store all line's instance.
    """
    from line import Line

    ls_instance = []
    for each in list_data:
        new_line = Line()
        new_line.name = each[0]
        new_line.stations = setup_value(each[0], each[1:])
        new_line.conns = setup_value(each[0], each[1:], conn=True)
        ls_instance.append(new_line)

    return ls_instance


# ===========================================================================
def setup_state(alist, amount, start_p):
    """
    Set up first state for all of trains.
    """
    [alist.append(['T' + str(item), start_p]) for item in range(1, amount + 1)]


# ===========================================================================
def find_total_turns(total_data, start_point, end_point, total_train):
    """
    Take total data and proceeding find the smallest turn.
    """

    from routing import Routing

    ls_instance = setup_all_lines(total_data)
    path = Routing()
    path.ls_lines = ls_instance
    setup_state(path.all_train_history, total_train, start_point)

    return path.find_smallest_turn()

# Son's part
# ===========================================================================
from node import Node
from line import Line
from train import Train

def generate_lines(data):
    lines = []

    for line in data:
        line_obj = Line(line[0])
        for node_info in line[1:]:
            is_Hub = False
            if 'Conn' in node_info:
                is_Hub = True
            node_obj = Node(node_info, line_obj.get_name(), is_Hub)
            line_obj.add_nodes_in_line(node_obj)

            if is_Hub:
                line_obj.add_hubs_in_line(node_obj)

        lines.append(line_obj)

    return lines

def generate_trains(total_train):
    trains = [Train() for _ in range(total_train)]
    for index, train in enumerate(trains):
        train.set_name(str(index))
    return trains

