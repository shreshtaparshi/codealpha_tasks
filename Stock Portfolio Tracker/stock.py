print("welcome to stock portfolio tracker!")

prices={"AAPL":180, "TSLA":250, "GOOGL":140}

portfolio={}
total=0

while(True):
    print("Available Stocks:")

    for key,value in prices.items():
        print(key," : ",value)

    stock=input("\nenter the stock name: ")
    quantity=int(input("enter the quantity:"))
    print("\n")

    investment=prices[stock]*quantity

    portfolio[stock]=investment

    print(f"investment in {stock} = {investment}")
    
    choice=input("\nDo you want to enter the another stock?(YES/NO) ")
    print("\n")

    if(choice=="NO"):
        print("-"*20)
        print("Portfolio Summary")
        print("-"*20)

        for key,value in portfolio.items():
            print(key,":",value)
            total+=value

        print(f"\nTotal Portfolio Value= {total} ")

        break



    
    