from abc import ABC, abstractmethod


class Graph(ABC):
    # Store all data of metro graph.
    def __init__(self):
        self.ls_lines = []
        self.total_turns = 0
        self.all_train_histories = []
        self.trains = []

    # Set up value for attributes
    def __setattr__(self, attribute, value):
        super(Graph, self).__setattr__(attribute, value)

    @abstractmethod
    def find_smallest_turn(self):
        pass

