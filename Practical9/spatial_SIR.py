import numpy as np
import matplotlib.pyplot as plt

# 0 = susceptible
# 1 = infected
# 2 = recovered

population = np.zeros((100, 100))

outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

beta = 0.3
gamma = 0.05

saved_times = [0, 10, 50, 100]
saved_populations = []

saved_populations.append(population.copy())

# For each time step:
#   1. Find all currently infected cells.
#   2. For each infected cell, check its 8 neighbours.
#   3. If a neighbour is susceptible, infect it with probability beta.
#   4. The infected cell recovers with probability gamma.
#   5. Save the population at selected time points for plotting.

for time in range(1, 101):

    new_population = population.copy()

    infected_positions = np.where(population == 1)

    for n in range(len(infected_positions[0])):

        row = infected_positions[0][n]
        col = infected_positions[1][n]

        for row_change in [-1, 0, 1]:
            for col_change in [-1, 0, 1]:

                if row_change == 0 and col_change == 0:
                    continue

                neighbour_row = row + row_change
                neighbour_col = col + col_change

                if neighbour_row >= 0 and neighbour_row < 100 and neighbour_col >= 0 and neighbour_col < 100:

                    if population[neighbour_row, neighbour_col] == 0:

                        infection = np.random.choice(
                            range(2),
                            p=[1 - beta, beta]
                        )

                        if infection == 1:
                            new_population[neighbour_row, neighbour_col] = 1

        recovery = np.random.choice(
            range(2),
            p=[1 - gamma, gamma]
        )

        if recovery == 1:
            new_population[row, col] = 2

    population = new_population.copy()

    if time in saved_times:
        saved_populations.append(population.copy())


plt.figure(figsize=(8, 8), dpi=150)

for i in range(len(saved_populations)):

    plt.subplot(2, 2, i + 1)

    plt.imshow(
        saved_populations[i],
        cmap='viridis',
        interpolation='nearest',
        vmin=0,
        vmax=2
    )

    plt.title('time = ' + str(saved_times[i]))

plt.tight_layout()
plt.show()