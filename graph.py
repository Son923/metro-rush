from abc import ABC, abstractmethod


class Graph(ABC):
    # Store all data of metro graph.
    def __init__(self, lines, trains, start_point, end_point):
        self.lines = lines
        self.trains = trains
        self.start_node = start_point
        self.end_node = end_point

        self.__total_turns = 0
        self.__all_train_histories = []

    def get_start_end(self):
        return (self.start_node, self.end_node)

    @abstractmethod
    def find_smallest_turn(self):
        pass
    
    @abstractmethod
    def find_path(self, start):
        end = self.end_node
        pass path