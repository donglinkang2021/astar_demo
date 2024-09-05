# Description: A* algorithm implementation

import heapq
import numpy as np
from typing import Tuple
import matplotlib.pyplot as plt
from utils import calc_time
import config

class Node:
    def __init__(self, x:int, y:int, parent=None, target=None):
        self.x = x
        self.y = y
        # the cost of the path from the start node to the current node
        steps_done = parent.steps_done + 1 if parent else 0  
        # the heuristic cost from the current node to the target node
        steps_rest = abs(x - target.x) + abs(y - target.y) if target else 0 # manhattan distance
        self.steps_done = steps_done
        alpha = config.alpha
        self.f = steps_done * alpha + steps_rest * (1 - alpha)
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

def backtrace(node:Node):
    return backtrace(node.parent) + [(node.x, node.y)] if node else []

@calc_time
def astar(
    grid:np.ndarray, 
    start:Tuple[int, int],
    end:Tuple[int, int],
    ax:plt.Axes = None
):
    n_rows, m_cols = grid.shape
    open_list = []
    closed_list = set()

    start_node = Node(start[0], start[1])
    end_node = Node(end[0], end[1])

    def is_end(node:Node) -> bool:
        return node.x == end_node.x and node.y == end_node.y
    
    def is_valid(x:int, y:int) -> bool:
        return 0 <= x < n_rows and 0 <= y < m_cols and grid[x][y] == 0 and (x, y) not in closed_list

    heapq.heappush(open_list, start_node)
    while open_list:
        current_node = heapq.heappop(open_list)
        if is_end(current_node): break
        closed_list.add((current_node.x, current_node.y))
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in neighbors:
            neighbor_x = current_node.x + dx
            neighbor_y = current_node.y + dy
            if is_valid(neighbor_x, neighbor_y):
                neighbor_node = Node(neighbor_x, neighbor_y, current_node, end_node)
                if (neighbor_x, neighbor_y) not in [(n.x, n.y) for n in open_list]:
                    heapq.heappush(open_list, neighbor_node)
                    if ax:
                        ax.plot(neighbor_y, neighbor_x, 'bo', alpha=0.5)
                        # plt.pause(0.01)
    return backtrace(current_node) if is_end(current_node) else None
