import numpy as np
import matplotlib.pyplot as plt

# Each cell in the grid represents one person:
# 0 = susceptible, 1 = infected, 2 = recovered
population = np.zeros((100, 100))

# Start the outbreak with one randomly chosen infected person
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# Infection and recovery probabilities
beta = 0.3
gamma = 0.05

# Save the population at these time points for plotting
saved_times = [0, 10, 50, 100]
saved_populations = []
saved_populations.append(population.copy())

# Main simulation loop:
# At each time point, infected people can infect their 8 neighbours,
# and they also have a chance to recover.
for time in range(1, 101):

    # Store updates in a copy so that all changes happen after checking
    # the current time point
    new_population = population.copy()

    # Find all infected cells in the current population
    infected_positions = np.where(population == 1)

    for n in range(len(infected_positions[0])):

        row = infected_positions[0][n]
        col = infected_positions[1][n]

        # Check the 8 neighbouring cells around each infected person
        for row_change in [-1, 0, 1]:
            for col_change in [-1, 0, 1]:

                # Skip the infected cell itself
                if row_change == 0 and col_change == 0:
                    continue

                neighbour_row = row + row_change
                neighbour_col = col + col_change

                # Only check neighbours that are inside the grid
                if neighbour_row >= 0 and neighbour_row < 100 and neighbour_col >= 0 and neighbour_col < 100:

                    # Susceptible neighbours may become infected
                    if population[neighbour_row, neighbour_col] == 0:

                        infection = np.random.choice(
                            range(2),
                            p=[1 - beta, beta]
                        )

                        if infection == 1:
                            new_population[neighbour_row, neighbour_col] = 1

        # Each infected person may recover after spreading infection
        recovery = np.random.choice(
            range(2),
            p=[1 - gamma, gamma]
        )

        if recovery == 1:
            new_population[row, col] = 2

    # Update the population for the next time point
    population = new_population.copy()

    # Save selected time points for comparison
    if time in saved_times:
        saved_populations.append(population.copy())


# Plot the saved populations as heat maps
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