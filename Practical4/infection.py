n = 91 #the number of total individuals
r = 0.4 #the growth rate over 24 hrs
#let the initial infected individuals number be 'a'
#indivuals will be infected on day two: a * r
#a + a * r = 7, a = 5
a = 5
i = 1  #the number of day the infection happens, let 1 be the initial
#use loop to achieve this goal: 
#start: 5 individuals infected
#   every day infection will happen, the number of people everyday is (a * r + a)
# when the number of infected people is higher than 91 or equal to 91, the loop ends
print("the number of infected students in day ", i, " is ", a) #show the the number	of infected	students in day 1
while a <= n:
    a = a + a * r
    i += 1
    print("the number of infected students in day ", i, " is ", a) #show the the number	of infected	students each day	

print(i, "days were taken to infect all")

#the final output:
# the number of infected students in day  1  is  5
# the number of infected students in day  2  is  7.0
# the number of infected students in day  3  is  9.8
# the number of infected students in day  4  is  13.72
# the number of infected students in day  5  is  19.208000000000002
# the number of infected students in day  6  is  26.891200000000005
# the number of infected students in day  7  is  37.64768000000001
# the number of infected students in day  8  is  52.70675200000001
# the number of infected students in day  9  is  73.78945280000002
# the number of infected students in day  10  is  103.30523392000003
# 10 days were taken to infect all