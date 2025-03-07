import time
def vendingmachine():
    products = [
        {'code': 'D1', 'name': 'Water', 'price': 1.50, 'stock': 5},         #Provides the list of drinks and snacks along with its code using a dictionary
        {'code': 'D2', 'name': 'Cola', 'price': 3, 'stock': 6},
        {'code': 'D3', 'name': 'Iced Vanilla Latte', 'price': 9.50, 'stock': 4},
        {'code': 'D4', 'name': 'Iced Coffee', 'price':8.25, 'stock': 7},
        {'code': 'D5', 'name': 'Pineapple Juice', 'price': 5.75, 'stock': 3},
        {'code': 'S1', 'name': 'Orange Juice', 'price': 6, 'stock': 2},
        {'code': 'S2', 'name': 'Cheetos', 'price': 4.50, 'stock': 8},
        {'code': 'S3', 'name': 'Lays', 'price': 3, 'stock': 5},
        {'code': 'S4', 'name': 'Oreo', 'price': 2.25, 'stock': 3},
        {'code': 'S5', 'name': 'Ferrero', 'price': 7, 'stock': 2},
    ]
    balance = 0
    quit = False

    while quit == False:                                                     #Using while loop to make sure that the program is running until the user quits
        print("Welcome to Ian's Vending Machine")
        time.sleep(1)
        print("------------------------------------------------------------------")
        print("MENU")                                                           #Using a for loop to display the available products including their prices, codes and stocks
        for product in products:                                               
            time.sleep(0.1)                                                    
            print(f"Product Name: {product['name']} - Price: {product['price']} - Code: {product['code']} - Stock: {product['stock']}")
        print("------------------------------------------------------------------")

        order = (input("Enter the code name of the item that you want to buy: "))
        for product in products:
            if order == product['code']:                                         #Using a for loop to check if the entered code by the user is correct
                order = product
                order['stock'] -= 1                                              #Stocks will also decrease as long as the program is running
                if order['stock'] == 0:
                    products.remove(product)

        else:
            print(f"Amazing, {order['name']} will cost you {order['price']} AED")  #If code in products are the same, else statement will be shown

            cash = float(input(f"Enter {order['price']} AED to buy: "))

            if cash < order['price']:                           #If the price of item is higher than cash then it will ask the user to input the remaining cash to get the item
                balance = float(input("Insert exact amount: "))
                balance = balance + cash
                if balance == order['price']:
                    balance -= order['price']
                    print(str(order['name']) + " being dispensed...")
                    time.sleep(2)                                  #Using time.sleep() function to stimulate delays in dispensing an item
                    print("Here's your " + str(order['name']))
                elif balance > order['price']:
                    balance -= order['price']
                    print(str(order['name']) + " being dispensed...")
                    time.sleep(2)
                    print("Here's your " + str(order['name']) + " and a balance of " + str(balance))
                else:
                    print("Current balance:" + str(balance) + "AED")
                    print("Insert exact amount")

            elif cash == order['price']:                                         #If the user inputs the right amount of cash, item will be dispensed once program has ended
                print(str(order['name']) + " being dispensed...")
                time.sleep(2)
                print(f"Thank you for buying here is your {order['name']}")

            elif cash > order['price']:                                          #If user inputs a higher amount of cash,user will be given the correct change
                balance = cash - order['price']
                print(str(order['name']) + " being dispensed...") 
                time.sleep(2)
                print("Here's your " + str(order['name'] + " and remaining " + str(balance) + "AED"))

        print("Note: If you have remaining balance quit the program first, so you can get your change")
        answer = input("To continue buying type I and to quit the program type S: ")
        if answer == 'i'.upper():                                                #If the keyword I or any keyword is entered, then it will allow you to continue buying
            quit = False
        elif answer == 's'.upper():                                              #If the keyword S is entered, then it will quit the program
            quit = True
            if balance != 0:                                                     #If the user have remaining balance in the machine then it will return the balance to the customer
                print("Thank you, come again and here's your change " + str(balance))
            else:                                                                #If balance is equal to zero then this will be executed
                print("Thank you, come again!")



vendingmachine()