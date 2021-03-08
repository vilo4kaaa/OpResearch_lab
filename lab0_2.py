import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm

n_towers = 10
m_towers = 3
towers = [[0] * m_towers for i in range(n_towers)]

for i in range(n_towers):
    for j in range(m_towers-1):
        towers[i][j] = random.randint(0, 100)

for i in range(5):
    towers[i][2] = 100

for i in range(5, 8):
    towers[i][2] = 300

for i in range(8, 10):
    towers[i][2] = 500

for row in towers:
    print(row)

n_density = 100
m_density = 100
density = [[0] * m_density for i in range(n_density)]

for i in range(n_density):
    for j in range(m_density):
        density[i][j] = random.randint(20, 100)

n_power = 100
m_power = 100
power = [[0] * m_power for i in range(n_power)]

tower_power = []
n_tower_power = n_towers

tower_power = [0 for i in range(n_tower_power)]

for i in range(n_power):
    for j in range(m_power):
        for k in range(n_tower_power):
            if i == towers[k][0] and j == towers[k][1]:
                tower_power[k] = towers[k][2]
            else:
                tower_power[k] = towers[k][2]/(pow(i-towers[k][0], 2) + pow(j-towers[k][1], 2))
        power[i][j] = max(tower_power)

for row in power:
    print(row)

plt.imshow(power, cmap=cm.viridis, origin='lower', vmin=0, vmax=5)
plt.show()

amount = 0

for i in range(n_power):
    for j in range(m_power):
        if power[i][j] > 1:
            amount += density[i][j]

print("Users with ok connection: ", amount)
