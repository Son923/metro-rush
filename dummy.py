from graph import Graph

class Dummy(Graph):
    def __init__(self, lines, trains, start_point, end_point):
        super().__init__(lines, trains, start_point, end_point)
        for train in trains:
            train.set_graph(self)
    
    def find_smallest_turn(self):
        turns, trains_history = None, None
        return turns, trains_history
    
    def find_path(self):
        return path
    