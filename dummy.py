from graph import Graph

class Dummy(Graph):
    def __init__(self, lines, trains, start_point, end_point):
        super().__init__(lines, trains, start_point, end_point)
    
    def find_smallest_turn(self):
        turns, trains_history = None, None
        return turns, trains_history