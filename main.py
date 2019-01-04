from utils import handling_argument, handling_data
from train import Train, generate_trains


def main():
    # filename, algo = handling_argument()
    # data, start_point, end_point, total_train = handling_data(filename)

    # Create lst of trains
    total_train = 10
    trains = generate_trains(total_train)
    

if __name__ == "__main__":
    main()