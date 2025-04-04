import ast

def Withdraw(lines):        
    while True:    
        with open("BankAccount/BankData/accounts.txt") as chck:
            realchck = chck.readlines()
        line = ast.literal_eval(realchck[lines])
        lines=lines
        bankAccountnum= line["Account Number"]
        BankName = line["Name"]
        BankAddress = line["Address"]
        BankPassword = line["Password"]
        BankBalance = line["Balance"]

        amount= (input("Enter the amount you want to withdraw : "))
        if not amount.isdigit() or int(amount)<=0:
            print(f"{BankName} Enter a Valid Amount")
            continue
            

        amount = int(amount)
        if(BankBalance>=amount):
            realchck[lines]=f"{str({ "Account Number" : bankAccountnum,"Name" : BankName,"Address" : BankAddress,'Password' : BankPassword,"Balance" : BankBalance - amount })}\n"            
            finalupdate = ""
            for all in realchck:
                finalupdate += all

            with open("BankAccount/BankData/accounts.txt","w") as withdrawedit:
                withdrawedit.write(f"{str(finalupdate)}")
                print(f'''WITHDRAWN **{amount}**
SUCCESFULLY UPDATED THE BALANCE''')
                break


        elif(BankBalance==0):
            print("YOU HAVE NO BALANCE TO WITHDRAW")
            continue

        elif(BankBalance<amount):
            print("You can not withdraw more than what you have")
            continue

        break