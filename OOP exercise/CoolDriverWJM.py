from CoolClassShoppingWJM import SL_WJM
#function that causes items to become list
def mylist():
    orderlist = []
    n = eval(input("How many items will you order today?"))
#this will cause looping if the item is less than 1
    while n < 1:
        print("Number of items must be at least 1.")
        n = eval(input("How many items will you order today?"))
    else:
            pass
#creating numbers of items based on n
    for data in range(1,n+1,+1):
        print("Items #",data)
        print("please write the food names in lowercase, thank you")
        food_type = input("Enter Food: ")
        pounds_Ord =  eval(input("Enter amount of pounds:"))
        while pounds_Ord <= 0:
            pounds_Ord = float(input("Enter amount of pounds:"))
            
        item =SL_WJM(food_type,pounds_Ord)  
 #adding the item into the list
        orderlist.append(item)
    return orderlist
#function displaying the list content
def display (orderlist):
    print("Here's a summary of the items purchased:" +"\n--------------------------")
    for data in range (len(orderlist)):
        orderlist[data].totalWJM()
        print("Item #", orderlist[data].food)
        print("Amount ordered :", orderlist[data].pounds ,"pounds")
        print("Price per pound : $", "{:.2f}".format(orderlist[data].get_priceWJM()))
        print("Price of order : $","{:.2f}".format(orderlist[data].totalWJM())+"\n")
#function calculating total cost        
def calc_amount(orderlist):
    total = 0
    for data in range(len(orderlist)):
        total += orderlist[data].totalWJM()
    return total
#function calling function
def main():
    all_list= mylist()
    display(all_list)
    print("Total cost: $","{:.2f}".format(calc_amount(all_list)))
main()
