from ATM_1 import ATM
acc = ATM("Ersi",1234,1500) 

while True:
    try:
        usrn=input("Enter username: ")
        passw=int(input("Enter password: "))
        acc1=acc.login(usrn,passw)
        if acc1 == False:
            break
        if acc1 == True:
            while True:
                print("""
                Please write in the same format of the question!""")
                ask3= int(input("""What would you like to do?
                Display(1); Deposit(2); Withdraw(3) or Exit(4)? 
                """))
                if ask3 == 1:
                    acc.display()
                elif ask3 == 2:
                    acc.deposit()
                elif ask3 == 3:
                    acc.withdraw()
                elif ask3 ==4:
                    break
                else:
                    print("Not supported answer!")
    except:
        print("Re-run the program")


    

