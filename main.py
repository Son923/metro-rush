from utils import handling_argument, handling_data
from train import Train, generate_trains
from prep import create_list_of_lines

def main():
    filename, algo = handling_argument()
    data, start_point, end_point, total_train = handling_data(filename)
    
    lines = create_list_of_lines(data)
    for line in lines:
        print(line)
        nodes = line.get_nodes_in_line()
        hubs = line.get_hubs_in_line()
        print('Nodes')
        for node in nodes:
            print(node)
        print()
        print('Hubs')
        for hub in hubs:
            print(hub)
        print()
    
    # Create lst of trains
    # trains = generate_trains(total_train)
    

if __name__ == "__main__":
    main()