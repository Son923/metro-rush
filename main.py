from utils import handling_argument, handling_data, create_list_of_lines
from train import Train, generate_trains
from dummy import Dummy


def main():
    filename, algo = handling_argument()
    data, start_point, end_point, total_train = handling_data(filename)


    lines = create_list_of_lines(data)
    trains = generate_trains(total_train)
    graph = Dummy(lines, trains, start_point, end_point)

    print(data)

    # test structure
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
    #     print()

    # print(data)


if __name__ == "__main__":
    main()

