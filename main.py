import numpy as np
import matplotlib.pyplot as plt
from astar import astar
from plot import ax_init_map, ax_draw_path
import config

# Define the grid, 0 means passable, 1 means obstacle
# Generate random grid
np.random.seed(1337)
MAP_SIZE = 100
grid = np.random.choice([0, 1], size=(MAP_SIZE, MAP_SIZE), p=[0.75, 0.25])

start = (0, 0)
end = (MAP_SIZE-1, MAP_SIZE-1)

# path = astar(grid, start, end)
# print("Path finded" if path else "Path not found")

alphas = np.linspace(0, 1, 21)
for alpha in alphas:
    config.alpha = alpha
    fig, ax = plt.subplots(figsize=(8, 8))
    ax_init_map(ax, grid, start, end)
    print(f"alpha: {alpha:0.2f}", end=" ")
    path = astar(grid, start, end, ax)
    print("path length:", len(path))
    ax_draw_path(ax, path)
    plt.savefig(f"images/astar_{alpha:0.2f}.png")
    plt.close()
