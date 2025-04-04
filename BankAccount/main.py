from modules import createAccount
from modules import login
from modules import withdraw
from modules import deposit
from modules import transfer
from modules import checkBalance


while(True):
    ask = input('''Enter **1** To create a new account 
Enter **2** To Login in an account
Enter **3** To exit
: ''')
    if(ask=='1'):
        name = input("Enter Your Name : ")
        Address = input("Enter Your Address : ")
        Password = input("Enter a password : ")
        person=createAccount.CreateAcccount(name,Address,Password)
        person.Accountmake()

    elif(ask=='2'):
        linecheck=login.login()  
        if (type(linecheck) == int):
            # accountuse = AccountUse(linecheck)  
            
            while True:
                thing=input(''' Enter 1/2/3/4/5 respectively for :-
**1** for Withdraw
**2** for Deposit
**3** for Transfer
**4** for CheckBalance
**5** for exit 
: ''')
                
                if(thing=='1'):
                        withdrawn = withdraw.Withdraw(linecheck)
                        # return "Withdraw"
                elif(thing=='2'):
                        deposited = deposit.Deposit(linecheck)
                elif(thing=='3'):
                        Transfered=transfer.Transfer(linecheck)
                elif(thing=='4'):
                        checkBalanced = checkBalance.CheckBalance(linecheck)
                elif(thing=='5'):
                        print( "Exited........")
                        break
                else:
                      print("Try again !!! you entered something wrong")
                      continue
            
        else:
            print("Exited......")


    elif(ask=='3'):
        print("Exited")
        break
    else:
        print("Try again !!! you entered something wrong")
        continue