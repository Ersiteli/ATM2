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
                ask3= input("""What would you like to do?
                Display; Deposit; Withdraw or Exit? 
                """)
                if ask3 == "Display":
                    acc.display()
                elif ask3 == "Deposit":
                    acc.deposit()
                elif ask3 == "Withdraw":
                    acc.withdraw()
                elif ask3 == "Exit":
                    break
                else:
                    print("Not supported answer!")
    except:
        print("Re-run the program")


    

