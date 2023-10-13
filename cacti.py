def count_adjacent_empty_cells(plot):
    rows, cols = len(plot), len(plot[0])
    count = 0
    
    def is_valid_cell(i, j):
        return 0 <= i < rows and 0 <= j < cols

    def is_adjacent_cell_empty(i, j):
        return is_valid_cell(i, j) and plot[i][j] == 1

    def is_empty_cell(i, j):
        return is_valid_cell(i, j) and plot[i][j] == 0

    for i in range(rows):
        for j in range(cols):
            if is_empty_cell(i, j):
                adjacent_empty = all(
                    not is_adjacent_cell_empty(x, y)
                    for x in range(i-1, i+2)
                    for y in range(j-1, j+2)
                )
                
                if adjacent_empty:
                    count += 1

    return count
