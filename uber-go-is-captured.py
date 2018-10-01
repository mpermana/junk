# Enter your code here. Read input from STDIN. Print output to STDOUT

# _ X X _
# X 0 _ X
# X 0 0 X
# _ X X _
# is 2, 2 captured?
# XX
# OX
# XX
#
#  XX
# XOOX
#  XX

data1 = [
    '_XX_',
    'XOOX',
    '_XX_',
]

data2 = [
    '_X__',
    'XOOX',
    '_XX_',
]

data3 = [
    '_XOX',
    'XOOX',
    '_XX_',
]

def get_piece(row, col, data):
    if row < 0 or col < 0 or row >= len(data) or col >= len(data[0]):
        return None
    return data[row][col]
    
def dfs(row, col, visited, data):
    if row < 0 or col < 0 or row >= len(data) or col >= len(data[0]):
        return False
    if data[row][col] == '_':
        return False
    visited.add((row, col))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for delta_row, delta_col in directions:
        neighbor_row = row + delta_row
        neighbor_col = col + delta_col
        piece = get_piece(neighbor_row, neighbor_col, data)
        if piece in [None, '_']:
            return False
        if piece == 'O' and (neighbor_row, neighbor_col) not in visited:
            if not dfs(neighbor_row, neighbor_col, visited, data):
                return False
    print 'ok ', row, col
    return True
    

def is_captured(data, row=0, col=0):
    visited = set()
    return dfs(row, col, visited, data)

data = data3
print is_captured(data)

