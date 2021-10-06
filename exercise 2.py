#%% WILLIAM JONATHAN MULYADI -L1CC
#%% EXERCISE 2
#%% Ramp Angle
import math
m = eval(input("Enter the mass of the cart (in kg):"))
F = eval(input("Enter the force to push the cart (in N):"))
g = 9.81
angle = math.degrees(math.asin(F/(m*g)))
print("The angle of the ramp is ",format(angle,".1f"),"degrees")

#%% Perimeter of triangle
a = eval(input("Enter length of edge1:"))
b = eval(input("Enter length of edge2:"))
c = eval(input("Enter length of edge3:"))

if a+b > c:
    if b+c > a:
        if c+a > b:
            perimeter = a+b+c
            print('The perimeter is:',perimeter)
else:
    print('Perimeter cannot be calculated: the input is invalid.')

#%% Wind-Chill Temperature
t1 =eval(input("Enter the temperature in Fahrenheit: "))
while not -58 < t1 < 41:
    print("Temprature must be between -58F and 41F")
    t1 =eval(input("Please re-enter the temperature in Fahrenheit:  "))

s1 =eval(input("Enter the wind speed miles per hour: "))
while s1 < 2:
    print("Speed must be greater than or equal to 2")
    s1 =eval(input("Please re-enter the wind speed miles per hour: "))

total = (35.74) + (0.6215*t1) - (35.75*(s1**0.16)) + (0.4275*t1*(s1**0.16))
print("The wind chill index is", format(total, '.3f'))

#%% Software Sales
n = eval(input("Enter the number of packages purchased:"))
d0 = n*99*0
d1 = n*99*(1/10)
d2 = n*99*(2/10)
d3 = n*99*(3/10)
d4 = n*99*(4/10)
tl = n*99
if 0<n<10:
    print("Discount Amount @",d0,"%",":","${:,.2f}".format(d0))
    print("Total Amount :","${:,.2f}".format(tl-d0))
if 11<n<19:
    print("Discount Amount @",10,"%",":","${:,.2f}".format(d1))
    print("Total Amount :","${:,.2f}".format(tl-d1))
if 20<n<49:
    print("Discount Amount @",20,"%",":","${:,.2f}".format(d2))
    print("Total Amount :","${:,.2f}".format(tl-d2))
if 50<n<99:
    print("Discount Amount @",30,"%",":","${:,.2f}".format(d3))
    print("Total Amount :","${:,.2f}".format(tl-d3))
if n>=100:
    print("Discount Amount @",40,"%", ":", "${:,.2f}".format(d4))
    print("Total Amount :","${:,.2f}".format(tl-d4))


