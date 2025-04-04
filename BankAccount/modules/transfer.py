import ast

def Transfer(lines):
    with open("BankAccount/BankData/accounts.txt") as chck:
        realchck = chck.readlines()
        line = ast.literal_eval(realchck[lines])
        lines=lines
        bankAccountnum= line["Account Number"]
        BankName = line["Name"]
        BankAddress = line["Address"]
        BankPassword = line["Password"]
        BankBalance = line["Balance"]

    if(BankBalance==0):
        print("****YOU DO NOT HAVE ANY BALANCE TO TRANSFER****")
        return 
    while True:
        getter=input("Whom Do you want to transfer please enter his account number (or type N to exit): ")

        if not getter.isdigit():
            if (getter.lower()=="n"):
                print("Exited...")
                break
            else:
                print("Try again !! You Entered Something Wrong")
            continue
        elif(int(getter) == bankAccountnum):
            print("You can not transfer into your own account")

        else:    
            with open("BankAccount/BankData/accounts.txt","r") as read:
                read1= read.readlines()
                    # print(read1)
            getline=0
            for line1 in read1:
                    lines1 = ast.literal_eval(line1)
                    if (str(lines1["Account Number"])==getter):
                        bankAccountnum2= lines1["Account Number"]
                        BankName2 = lines1["Name"]
                        BankAddress2 = lines1["Address"]
                        BankPassword2 = lines1["Password"]
                        BankBalance2 = lines1["Balance"]
                        while True:
                            amount = input("Enter The Amount You Want TO Transfer : ")
                            if not amount.isdigit() or int(amount)<=0:
                                print(f"{BankName} Enter a Valid Amount")
                                continue
                            amount = int(amount)    
                            if(BankBalance<=amount):
                                print(f"{BankName} You cannot transfer more than what you have")
                                continue
                            elif(BankBalance>=amount):     
                                realchck[lines]=f"{str({ "Account Number" : bankAccountnum,"Name" : BankName,"Address" : BankAddress,'Password' : BankPassword,"Balance" : BankBalance - amount })}\n"            
                                finalupdate = ""
                                for all in realchck:
                                    finalupdate += all

                                with open("BankAccount/BankData/accounts.txt","w") as withdrawedit:
                                    withdrawedit.write(f"{str(finalupdate)}")
                                    print(f'''{BankName} You Have Transfered {amount}$ to {BankName2} whose Account Number is {bankAccountnum2}
SUCCESFULLY UPDATED THE BALANCE''')
                                realchck[getline]=f"{str({ "Account Number" : bankAccountnum2,"Name" : BankName2,"Address" : BankAddress2,'Password' : BankPassword2,"Balance" : BankBalance2 + amount })}\n"            
                                finalupdate = ""
                                for all in realchck:
                                    finalupdate += all

                                with open("BankAccount/BankData/accounts.txt","w") as depositeedit:
                                        depositeedit.write(f"{str(finalupdate)}")
                                return                                          
                                                           
                    else:
                        getline+=1
                        continue
            else:
                    print("There is no Bank Account with these Account number PLEASE TRY AGAIN !!")
                    continue
