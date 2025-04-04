import ast

def Deposit(lines):        
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

        amount= (input("Enter the amount you want to deposit : "))
        if not amount.isdigit() or int(amount)<=0:
            print("Enter a Valid Amount")
            continue
            

        amount = int(amount)
        realchck[lines]=f"{str({ "Account Number" : bankAccountnum,"Name" : BankName,"Address" : BankAddress,'Password' : BankPassword,"Balance" : BankBalance + amount })}\n"            
        finalupdate = ""
        for all in realchck:
            finalupdate += all

        with open("BankAccount/BankData/accounts.txt","w") as depositeedit:
                depositeedit.write(f"{str(finalupdate)}")
                print(f'''DEPOSITED **{amount}**
SUCCESFULLY UPDATED THE BALANCE''')
                break


        break