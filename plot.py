# Description: Plotting functions for the A* algorithm
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

def ax_init_map(ax: plt.Axes, grid: np.ndarray, start: Tuple[int, int], end: Tuple[int, int]):
    n_rows, m_cols = grid.shape
    ax.set_xticks(np.arange(-0.5, n_rows, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, m_cols, 1), minor=True)
    # ax.grid(which='minor', color='black', linestyle='-', linewidth=1)
    ax.imshow(grid, cmap='Greys', origin='upper')
    ax.plot(start[1], start[0], 'gs', markersize=10, label='start')
    ax.plot(end[1], end[0], 'rp', markersize=10, label='end')
    ax.legend(loc="best")

    
def ax_draw_path(ax: plt.Axes, path: list):
    path_np = np.array(path, dtype=np.float32)
    # for i in range(len(path_np) - 1):
    #     ax.arrow(
    #         path_np[i, 1], path_np[i, 0],
    #         path_np[i+1, 1] - path_np[i, 1], 
    #         path_np[i+1, 0] - path_np[i, 0],
    #         head_width=0.33, 
    #         length_includes_head=True, 
    #         color='r'
    #     )
    #     plt.pause(0.01)
    ax.plot(path_np[:, 1], path_np[:, 0], 'r-', linewidth=2)
    