grid_size = 20
dict =  {}

def traverse (i , j):
    if (i == grid_size or j == grid_size):
        return 1;
    x = 0
    y = 0
    if (dict.has_key((i + 1, j))):
        x = dict[(i + 1, j)]
    elif (dict.has_key((i , j + 1))):
        y = dict[(i, j + 1)]

    if (x == 0):
        x = traverse(i + 1, j)
    if (y == 0):
        y = traverse (i, j + 1)
    
    count = x + y
    dict[(i ,j)] = count
    
    return count

print traverse(0, 0)
