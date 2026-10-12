balance=2000
while True:
    print("1. check bank balance")
    print("2. deposit money")
    print("3. withdraw money ")
    print("4. exit")

    atm=int(input("enter the one options:"))
    if atm==1:
        print("your current balance is: ",balance)
    elif atm==2:
        deposit=int(input("enter your deposit amount: "))
        if deposit>0:
            balance=balance+deposit
            print("money deposited sucessfully and current balance is: ",balance)
        else:
            print("enter a valid amount")
    elif atm==3:
        withdraw=int(input("enter your withdraw amount: "))
        if withdraw>0 and withdraw<=balance:
            balance=balance-withdraw
            print("withdraw amount is : ",withdraw)
            print(" current balance is: ",balance)
        else:
            print("insufficent balance ")
    elif atm==4:
        print("exit sucessfully")
        break
    else:
        print("invalid option,enter a valid number")
