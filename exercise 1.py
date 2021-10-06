#%% WILLIAM JONATHAN MULYADI -L1CC
#%% EXERCISE 1
#%% Slope of line
import math

x1 = eval(input("Enter the x-coordinate for point1:"))
y1 = eval(input("Enter the y-coordinate for point2:"))
x2 = eval(input("Enter the x-coordinate for point1:"))
y2 = eval(input("Enter the y-coordinate for point2:"))

f = (y2-y1)/(x2-x1)
print("The slope for the line that connects two points", ( x1 , y1 ), "and", ( x2 , y2), "is", format(f,".5"))

#%% Runway Length
s = eval(input("Enter the plane's take off speed in m/s :"))
a = eval(input("Enter the plane's acceleration in m/s**2:"))
q = (s**2)/(2*a)
print("The minimum runway length needed for this airplane is",format(q,".4f"), "meters")

#%% Tip Calculator
s1 = eval(input("Enter the subtotal: $"))
t1 = eval(input("Enter tip amount (as a %):"))
tp = s1 * (t1/100)
ttl = s1 + tp
print("Subtotal: $","${:,.2f}".format(s1))
print("Tip: $","${:,.2f}".format(tp))
print("Total: $","${:,.2f}".format(ttl))

#%% Area of Hexagon
import math
ss = eval(input("Enter the side length of the hexagon:"))
area = ((3*math.sqrt(3))/2)*(ss**2)
print("Enter the side length of the hexagon:",ss)
print("The area of a hexagon with side length",ss,"is", format(area,".3f"))