from node import Node
from hub import Hub
from line import Line

def create_list_of_lines(data):
    lines = []

    for line in data:
        line_obj = Line(line[0])
        for node_info in line[1:]:
            if 'Conn' in node_info:
                line_obj.add_hubs_in_line(node_info)
            else:
                line_obj.add_nodes_in_line(node_info)
        lines.append(line_obj)

    return lines
