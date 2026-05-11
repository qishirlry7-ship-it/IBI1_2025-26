import numpy as np
import matplotlib.pyplot as plt

susceptible = 10000 - 1 # people who have the possibility to get infected
infected = 1 # initial infected people
recovered = 0 #initial recovered people
N = 10000 # the total number of the population
beta = 0.3
gamma = 0.05

time_list = [0]
susceptible_list = [susceptible]
infected_list = [infected]
recovered_list = [recovered]

# run the loop for 1000 times:
#    randomly pick susceptible people -> become new infected
#        p: beta * (infected / N)
#    randomly pick infected people -> recovered
#        p: gamma
#    infected people = initial infected + new infected - recovered 

# I presume the infection and recovery happen at the same time.

for time in range(1, 1001):

    infection_probability = beta * infected / N

    new_infected_array = np.random.choice(
        range(2),
        susceptible,
        p=[1 - infection_probability, infection_probability]
    )

    recovered_array = np.random.choice(
        range(2),
        infected,
        p=[1 - gamma, gamma]
    )

    new_infected_total = np.sum(new_infected_array)
    new_recovered_total = np.sum(recovered_array)

    susceptible = susceptible - new_infected_total
    infected = infected + new_infected_total - new_recovered_total
    recovered = recovered + new_recovered_total

    time_list.append(time)
    susceptible_list.append(susceptible)
    infected_list.append(infected)
    recovered_list.append(recovered)

plt.figure(figsize=(6, 4), dpi=150)

plt.plot(time_list, susceptible_list, label='susceptible')
plt.plot(time_list, infected_list, label='infected')
plt.plot(time_list, recovered_list, label='recovered')

plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()

plt.savefig('SIR_model.png', format='png')
plt.show()
