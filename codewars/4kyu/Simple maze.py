def has_exit(maze):
    def find_kate():
        count_k = 0
        position = None
        for r in range(len(maze)):
            for c in range(len(maze[r])):
                if maze[r][c] == 'k':
                    count_k += 1
                    position = (r, c)
        if count_k != 1:
            raise ValueError("There must be exactly one Kate in the maze.")
        return position

    def is_escape_possible(maze, start_row, start_col):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = [(start_row, start_col)]
        visited = set(queue)

        while queue:
            current_row, current_col = queue.pop(0)
            for dr, dc in directions:
                new_row, new_col = current_row + dr, current_col + dc
                if new_row < 0 or new_row >= len(maze) or new_col < 0 or new_col >= len(maze[new_row]):
                    return True
                if (new_row, new_col) not in visited and maze[new_row][new_col] == ' ':
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))
        return False

    kate_position = find_kate()
    if kate_position is None:
        return False
    return is_escape_possible(maze, kate_position[0], kate_position[1])


if __name__ == "__main__":
    print(has_exit([
        "########",
        "# # ####",
        "# #k#   ",
        "# # # ##",
        "# # # ##",
        "#      #",
        "########"
    ]))  # True