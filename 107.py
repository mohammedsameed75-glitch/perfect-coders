n = 4

matrix = [[0 for _ in range(n)] for _ in range(n)]

num = 1
top = 0
bottom = n - 1
left = 0
right = n - 1

while top <= bottom and left <= right:

    # Left to right
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1

    # Top to bottom
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1

    # Right to left
    for i in range(right, left - 1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1

    # Bottom to top
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        num += 1
    left += 1

for row in matrix:
    for value in row:
        print(value, end="\t")
    print()
