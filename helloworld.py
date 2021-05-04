name=input("What is your name? \n")
allowedUser=["Seyi","Mike","Love"]
allowedPassword=["PasswordSeyi","PasswordSeyi","PasswordLove"]
balance=100000

if(name in allowedUser):
    password=input("What is your password? \n")
    userId=allowedUser.index(name)
    if(password == allowedPassword[userId]):
        print("Welcome %s" % name)
        import datetime
        x = datetime.datetime.now()
        print(x)
        print("Available balance is: %d" % balance)
        print("These are the available options")
        print("1. Withdrawal")
        print("2. Cash deposit")
        print("3. Complaint")

        selectedOption=int(input("Please select an option: "))
        
        if(selectedOption==1):
            print("you selected %s" % selectedOption)
            selectedValue=int(input("How much would you like to withdraw: "))
            if(selectedValue <= balance):
                print("Take your cash")
                balance=balance-selectedValue
                print("Your current balance is: %d" % balance)
            else:
                print("Insufficient funds")
        elif(selectedOption==2):
            print("you selected %s" % selectedOption)
            selectedValue=int((input("How much would you like to deposit?: ")))
            balance=balance+selectedValue
            print("Your current balance is: %d" % balance)
        elif(selectedOption==3):
            print("you selected %s" % selectedOption)
            print(input("What issue will you like to report?: "))
            print("Thank you for contacting us")
        else:
            print("Invalid option selected, please try again")
    else:
        print("Password incorrect please try again")
else:
    print("Name not found, please try again")
