# What does this piece of code do?
# Answer: run a loop 11 times (from 0 to 10) to add a random number between 1 to 10 to the variable 'total_rand', and output the final outcome

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

#let the both number be 0 in the beginning
total_rand = 0 
progress=0
#run 11 times this loop, every time add a random number between 1 to 10 to the variable 'total_rand'
while progress<=10:
	progress+=1
	n = randint(1,10)
	total_rand+=n

#output the final total_rand number
print(total_rand)

