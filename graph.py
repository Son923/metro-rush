from abc import ABC, abstractmethod


class Graph(ABC):
    # Store all data of metro graph.
    def __init__(self, lines, trains, start_point, end_point):
        self.lines = lines
        self.trains = trains
        self.start_node = start_point
        self.end_node = end_point

        self.total_turns = 0
        self.all_train_histories = []

    # Set up value for attributes
    def __setattr__(self, attribute, value):
        super(Graph, self).__setattr__(attribute, value)
    
    def get_start_end(self):
        return (self.start_node, self.end_node)

    @abstractmethod
    def find_smallest_turn(self):
        pass