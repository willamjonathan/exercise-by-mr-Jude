#%% PROGRAMMMING EXERCISE 25-10-21
#%% WILLIAM JONATHAN L1CC
#%% submission due 27-10-21
#%% number 1
def hms():
    hours = int(input("Enter number of hours:"))
    minutes = int(input("Enter number of hours:"))
    seconds = int(input("Enter number of hours:"))
    return hours, minutes, seconds
def convert_to_days(h,m,s):
    return  (h/24) + (m/(60*24)) + (s/(3600*24))
h,m,s = hms()
d = convert_to_days(h,m,s)
print ("The number of days is :", "{:.4f}".format(d))

#%% number 2
def calc_weight_on_planet():
    weight = 120
    return weight
def calc_weight_on_planet1(w):
    return w/9.8 * 23.1
w = calc_weight_on_planet()
z = calc_weight_on_planet1(w)
def main():
    print("calc_weight_on_planet","(",int(w),",",9.8,")")
    print(float(w))
    print("calc_weight_on_planet","(",int(w),")")
    print(z)
    print("calc_weight_on_planet","(",int(w),",",23.1,")")
    print(z)
main()
#%% number 3
def numb_atoms1():
    a = 10
    return a
def calculation_element(a,b=196.97): #optional parameter
    return a/b *(6.022*(10**23))
def calculation_carbon(a):
    return a/12.001 *(6.022*(10**23))
def calculation_hyd(a):
    return a/1.008 *(6.022*(10**23))
a = numb_atoms1()
c = calculation_carbon(a)
h = calculation_hyd(a)
g = calculation_element(a,b=196.07)
def numb_of_atoms():
    print ("num_atoms","(",a,")")
    print (g)
    print ("num_atoms","(",a,",",12.001,")")
    print (c)
    print ("num_atoms","(",a,",",1.008,")")
    print (h)
numb_of_atoms()
#%% number 4
def current():
    cw = eval(input("Enter the current width:"))
    ch = eval(input("Enter the current height:"))
    dw = eval(input("Enter the desired width:"))
    return cw,ch,dw
def calc_new_height1(cw,ch,dw):
    return ch * (dw/cw)
cw,ch,dw = current()
x = calc_new_height1(cw,ch,dw)
def calc_new_height():
    print("The corresponding height is:",x)
    print(x)
calc_new_height()
#%% number 5
def farenheit():
    frh = eval(input("Enter a temperature in Farenheit:"))
    return frh
def celcius(f):
    return 5/9 *(f-32)
def kelvin(c):
    return c+273.15

f = farenheit()
c = celcius(f)
k = kelvin(c)
def convert_temp():
    print("The temperature in Farenheit is : ",f)
    print("The temperature in Celcius is : ",c)
    print("The temperature in Kelvin is : ",k)
convert_temp()
