# calculate the precentage change
# unit: million
UK_change = 69.2 - 66.7
UK = UK_change / 66.7 * 100
China_change = 1410-1426
China = China_change / 1426 * 100
Italy_change = 58.9 - 59.4
Italy = Italy_change / 59.4 * 100
Brazil_change = 212 - 208.6
Brazil = Brazil_change / 208.6 * 100
USA_change = 340.1 - 331.6
USA = USA_change / 331.6 * 100
population_changes = {'UK': UK, 'China': China, 'Italy': Italy, 'Brazil': Brazil, 'USA': USA}
sorted_data = sorted(population_changes.items(), key=lambda x: x[1], reverse=True)
print('the precentage population change: ', population_changes)
print('the sorted outcome: ', sorted_data)
print('the largest increase: ', sorted_data[0][0])
print('the largest decrease: ', sorted_data[4][0])

import matplotlib.pyplot as plt
plt.bar(population_changes.keys(), population_changes.values()) # x&y should be written separately
# add the number on the bar chart
for i, value in enumerate(population_changes.values()):
    plt.text(i, value, f'{value:.2f}', ha='center', va='bottom') # only keeps two decimal places
plt.title('Population Change')
plt.ylabel('population change (%)')
plt.show()