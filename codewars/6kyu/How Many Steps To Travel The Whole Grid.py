def minimum_steps(grid):
    return len(grid) - 1 + sum([len(grid[i]) - 1 for i in range(1, len(grid))])