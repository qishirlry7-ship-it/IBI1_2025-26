import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N = 10000
beta = 0.3
gamma = 0.05

vaccination_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5,
                     0.6, 0.7, 0.8, 0.9, 1.0]

plt.figure(figsize=(7, 5), dpi=150)

for index in range(len(vaccination_rates)):

    vaccination_rate = vaccination_rates[index]

    infected = 1
    vaccinated = int((N - infected) * vaccination_rate)
    susceptible = N - infected - vaccinated
    recovered = 0

    time_list = [0]
    infected_list = [infected]

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
        infected_list.append(infected)

    label_text = str(int(vaccination_rate * 100)) + '%'

    plt.plot(
        time_list,
        infected_list,
        label=label_text,
        color=cm.viridis(index / len(vaccination_rates))
    )

plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.legend(title='vaccination rate')

plt.savefig('SIR_vaccination.png', format='png')
plt.show()