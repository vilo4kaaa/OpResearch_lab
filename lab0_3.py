m_field = 15
n_field = 15
field = [[0] * m_field for i in range(n_field)]

for i in range(n_field):
    for j in range(m_field):
        field[i][j] = 0

field[1][2] = 1
field[12][2] = 1
field[12][4] = 1
field[14][4] = 1
field[14][9] = 1
field[1][9] = 1

for row in field:
    print(row)

count = 0

for i in range(n_field):
    for j in range(m_field):
        if field[i][j] == 1:
            count += 1

# print(count)

m_points = count+1
n_points = 2

points = [[0] * m_points for i in range(n_points)]

k = 0

for i in range(n_field):
    for j in range(m_field):
        if field[i][j] == 1:
            points[0][k] = j
            points[1][k] = i
            k += 1

# for row in points:
#    print(row)

root = [[0] * m_points for i in range(n_points)]
for i in range(n_points):
    for j in range(m_points):
        root[i][j] = 0

root[0][0] = points[0][0]
root[1][0] = points[1][0]


start_x = root[0][0]
start_y = root[1][0]
k = 1

while k <= count:
    for j in range(m_field):
        if field[start_y][j] == 1 and j != start_x:
            root[0][k] = j
            root[1][k] = start_y
            start_x = j
            break
    k += 1

    for i in range(n_field):
        if field[i][start_x] == 1 and i != start_y:
            root[0][k] = start_x
            root[1][k] = i
            start_y = i
            break
    k += 1

for k in range(m_points):
    print("(", root[0][k], ";", root[1][k], ")")
