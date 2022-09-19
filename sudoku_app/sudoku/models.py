LEVEL1 = [[1, 0, 0, 0, 0, 0, 0, 0, 3], [0, 0, 7, 2, 6, 0, 4, 8, 0], [4, 0, 0, 9, 3, 5, 0, 0, 6],
          [0, 3, 0, 4, 8, 0, 2, 0, 0], [0, 4, 1, 6, 0, 9, 3, 0, 0], [0, 0, 6, 0, 0, 0, 8, 9, 0],
          [5, 7, 8, 0, 4, 0, 0, 0, 2], [0, 0, 0, 3, 0, 0, 0, 7, 0], [2, 0, 0, 0, 0, 0, 0, 0, 5]]


def verify(arr):
    for i in arr:
        if len(i) != len(set(i)):
            return False

    cols = [[0 for i in range(9)] for i in range(9)]
    for i in range(9):
        for j in range(9):
            cols[j][i] = arr[i][j]
    for i in cols:
        if len(i) != len(set(i)):
            return False

    cubes = [[x for r in arr[i:i + 3] for x in r[j:j + 3]] for j in range(0, 9, 3) for i in range(0, 9, 3)]
    for i in cubes:
        if len(i) != len(set(i)):
            return False

    return True


