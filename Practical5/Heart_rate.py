heart_rate = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64] #resting heart rates
n = len(heart_rate)
mean = (sum(heart_rate) / n)
print('There are ', n, ' patients in the dataset, and the mean rate is ', mean)

low = 0
normal = 0
high = 0
# calculate the number in each type
for i in heart_rate:
    if i < 60:  # unit: bpm
        low += 1
    elif i <= 120:
        normal += 1
    else: 
        high += 1
print('heart rate of the patients:Low: ', low, ', Mormal: ', normal, ', High: ', high)

# compare and find the largest category
if low < high:
    if high < normal:
        print('The largest number of patients are in normal heart rate.')
    else:
        print('The largest number of patients are in high heart rate.')
elif low < normal:
    if high < normal:
        print('The largest number of patients are in normal heart rate.')
    else:
        print('The largest number of patients are in high heart rate.')
else:
    print('The largest number of patients are in low heart rate.')

#create pie chart
import matplotlib.pyplot as plt
labels = 'Low', 'Normal', 'High'
sizes = [low, normal, high]
# report the number of patients in each heart rate category with reporting the precentage
def make_autopct(values):
    def my_autopct(pct):
        count = values[my_autopct.counter]
        my_autopct.counter += 1
        return f'{count} ({pct:.1f}%)'  
    my_autopct.counter = 0
    return my_autopct
plt.pie(sizes, labels = labels, autopct = make_autopct(sizes))
plt.axis('equal')
plt.title("Distribution of Heart Rate Categories")
plt.show()

    
    