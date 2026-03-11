a = 5.08 #million 2004
b = 5.33 #2014
c = 5.55 #2024
d = b - a #d = 0.25
e = c - b #e = 0.22
print(d)
print(e)
if d < e:
    print("population growth is accelerating")
else:
    print("population growth is decelerting")

#population growth is decelerting


X = True
Y = False
W = X or Y
print(W)

X = True
Y = True
W = X or Y
print(W)

X = False
Y = True
W = X or Y
print(W)

X = False
Y = False
W = X or Y
print(W)

#W (X or Y) truth table：
#X     | Y      | W (X or Y)
#---------------------------
#True   | True   | True
#True   | False  | True  
#False  | True   | True
#False  | False  | False