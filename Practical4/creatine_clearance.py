#store the value of age, weight, gander, and creatine concentration, Cr, in	height
#I am not sure the format of some input, so I use float() to have a wider cover.

age = int(input('age: (in years)')) #unit: year
print('weight: (in kg)')
weight = float(input()) #unit: kg
#We need to add an factor when calculating the CrCl of female.
print('What is your gender, male or female?')    # improved
gender = int(input()) 
print('Cr(creatine concentration): (in µmol/l)')
Cr = float(input()) #unit: µmol/l
#judge whether the variables are correct and calculate the CrCl if they are correct in the different gender circumstance
if age >= 100:
    print('Age needs corrected.') 
elif 20 >= weight or weight >= 80:
    print('Weight needs corrected.')
elif 0 >= Cr or Cr >= 100:
    print('Cr needs corrected.')
elif gender == 'female':    # improved
    CrCl = (140 - age) * weight * 0.85 / (72 * Cr)
    print(CrCl)
elif gender == 1:
    CrCl = (140 - age) * weight / (72 * Cr)
    print(CrCl)
else:
    print('Gender needs corrected.')

