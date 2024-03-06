#!/usr/bin/env python3
"""
fileName: iceKarim.py
author: Hezha
dateAndTime: 3/5/24-18:58
description: Select from a variety of ice-cream flavors, toppings, and sizes, with each choice affecting the total price. 
"""
flavors = {                         # Ice Cream flavors
    "Vanilla": 1,
    "Chocolate": 1,
    "Strawberry": 1,
    "Cotton Candy": 1.1,
    "Saffron": 1.2
}
toppings = {                        # Ice cream toppings
    "Sprinkes": .25,
    "Chocolate Chips": .25,
    "Mixed Nuts": .5,
    "Pistachio": .75
}
sizes = {                           # Ice cream sizes
    "Small": 4,
    "Medium": 8,
    "Large": 10,
}

def display(dic,dicName):           # Display each item in the dictionaries
    count = 0
    print(f"\n\n{dicName} options")
    print("********")
    for item in dic:
        count+=1
        print(f"{count}- {item}\t${dic[item]}")
    print("********")

    flag=True                       # error handling
    while flag:
        try:
            usrChoice = int(input("Select an option: "))
            if usrChoice > len(dic):
                print("Invalid input (Options doen't exit)")
            else:
                flag=False
        except:
            print("Invalid input (Number expected)")

    return list(dic.keys())[usrChoice-1], list(dic.values())[usrChoice-1]

def menu():                         # Display the menue choices
    print("****\tMENU\t****")
    print("1- Start the order")
    print("2- Display Cart")
    print("Press Enter to exit.")

def cart(items,price):
    print("\n\n****\tYOUR CART\t****")

    if len(items) == 0 and len(price) ==0:
        print("Your Cart is empty!\n\n")
    else:
        for i in range(len(items)):
            print(f"{i+1}- {items[i][0],items[i][1],items[i][2]}\t${price[i]}")
        print(f"You Total is: ${sum(price)}\n\n")

def main():                         # asks for input and call other functions accordingly
    items=[]
    price=[]
    while 75!=85:
        menu()
        inpOpt = input("Select offered options: ")
        if inpOpt=="1":
            item1,price1=display(sizes,"Size")
            item2,price2=display(flavors,"Flavor")
            item3,price3=display(toppings,"Topping")
            items.append([item1,item2,item3])
            price.append(price1+price2+price3)
        elif inpOpt=="2":           # shows the items and the prices already added to the cart
            cart(items,price)
        elif inpOpt=="":
            break
        else:
            print("Invalid input\n")

if __name__=="__main__":
    main()