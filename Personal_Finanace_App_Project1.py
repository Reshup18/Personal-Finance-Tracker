#Expence Tracker Project

expensesList=[] #List of all expenses in form of dictionary
print ("*****Welcome to Expense Tracker App*****")

while True:
    print("=====MENU====")
    print("1. Add Expenses")
    print("2.View all Expenses")
    print("3.View total Spending")
    print("4.Exit")

#Add Expenses   
    choice=int(input("Enter your choice: "))

    if (choice==1):
        date=input("Enter the Date of Expenses: ") #Date of Expense
        category=input("Enter the category of the Expenses like(dress, food, travel, etc): ") #Category of Expense
        description=input("Enter the description of category of the Expenses : ") #Description of Expense
        amount=float(input("Enter the amount of Expenses: ")) #Amount of Expense

        expenses={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }
        expensesList.append(expenses) #Adding expense to the list
        print(" \n Expense added successfully!")
#2.View all Expenses
    elif(choice==2):
        if(len(expensesList)==0):
            print("No Expense Added")
        else:
            print("Following are your all Expenses") 
            count =1
            for eachexpense in expensesList:
             print(f"Expense Number {count}. Date: {eachexpense['date']}, Category: {eachexpense['category']}, Description: {eachexpense['description']}, Amount:  {eachexpense['amount']} ") #Display all expenses
             count+=1

#3.View total Spending
    elif(choice==3):
        total=0
        for eachexpense in expensesList:
            total += eachexpense['amount']

        print(" \n TOTAL SPENDINDG = ", total)

#4.Exit
             
    elif(choice==4):
        print("Thank you for using Expense Tracker App. Have a nice day!")
        break
    else:
        print("Invalid Choice. Please try again.")


