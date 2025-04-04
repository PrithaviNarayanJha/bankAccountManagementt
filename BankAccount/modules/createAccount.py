import random
import ast


class CreateAcccount:

    def __init__(self,name,address,password):
        self.name =name
        self.address = address
        self.password = password
        self.balance=0

    def Accountmake(self):
            with open("BankAccount/BankData/accounts.txt","r") as read:
                read1= read.readlines()
            # print(read1)

            Exclude = []
            for line in read1:
                line = line.strip()
                if not line:
                     continue
                lines = ast.literal_eval(line)
                num=(lines["Account Number"])
                Exclude.append(num)

            
            valid_number = [num for num in range(1000,10000) if num not in Exclude]

            Accountnum = random.choice(valid_number)


            with open("BankAccount/BankData/accounts.txt","a") as opening:
                details = { "Account Number" : Accountnum,"Name" : self.name,"Address" : self.address,'Password' : self.password,"Balance" : self.balance}
                opening.write(f"{str(details)}\n")
                print("Account Succesfully Created")
                print(f"{self.name} your account number is {Accountnum}")

    
                    
