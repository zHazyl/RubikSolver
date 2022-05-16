import sys

class Node():
    """A node class for A* search"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = sys.maxsize # PATH-COST to the node
        self.h = sys.maxsize # heuristic to the goal: straight-line distance hueristic
        self.f = sys.maxsize # evaluation function f(n) = g(n) + h(n)

    def __eq__(self, other):
        return self.position == other.position
    

    
    ''' DEBUG THE FOLLOWING FUNCTION '''
def astar(maze, start, end):
    """Returns a list of tuples as a solution from "start" to "end" state in "maze" map using A* search.
    See lecture slide for the A* algorithm."""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    # end_node.g = end_node.h = end_node.f = sys.maxsize

    # Initialize both open and closed list
    open_list = []    # frontier queue
    closed_list = []  # explored set
    
    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Check if we found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Expansion: Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            
            def isChildOnClosed():
            # Child is on the closed list
                for closed_child in closed_list:
                    if child == closed_child:
                        return True
                return False

            if isChildOnClosed():
                continue
            
            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            def isChildOnOpen():
            # Child is already in the open list
                for open_node in open_list:
                    if child == open_node:
                        if child.g < open_node.g:
                            open_node.g = child.g
                            open_node.parent = child.parent
                            open_node.f = child.f
                        return True
                return False
                    
            if isChildOnOpen():
                continue

            # Add the child to the open list
            open_list.append(child)   