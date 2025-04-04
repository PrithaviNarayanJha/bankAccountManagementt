import ast


def login():
    ask = "y"
    while(True):
        if ask.lower() =="y":
            print("Enter Your Details")
            Accountnum = input("Enter your account number : ")
            Password = input("Enter your Password : ")

            with open("BankAccount/BankData/accounts.txt") as accounts:
                content = accounts.readlines()

            lines = -1
            for line in content:
                lines +=1
                a = ast.literal_eval(line)
                bankAccountnum= a["Account Number"]
                BankPassword = a["Password"]
                # BankName = a["Name"]

                if (Accountnum == str(bankAccountnum) and Password==BankPassword):
                    print("Succesfully signed in...")
                    return lines
                elif(Accountnum == str(bankAccountnum) and Password!=BankPassword):
                    print(f"You Entered Wrong Password for the Bank Account {bankAccountnum}")
                    while(Password!=BankPassword):
                        re=input("Do you want to retry the password (Y/N) : ")
                        if (re.lower()=="y"):
                            Password=input("Enter the Password : ")
                            if(Password!=BankPassword):
                                continue
                            else:
                                print(f"You entered correct password for the bank account {Accountnum}")
                                print("Succesfully signed in...")
                                return lines
                        elif(re.lower()=="n"):
                            print("Exiting......")   
                            break
                        else:
                            continue
                    else:
                        continue
                    ask = input("Do You Want to login(Y/N) : ")
                    break
            else:
                print("Enter a valid account number and password")
                ask = input("Do you want to try again?(Y/N) : ")
                continue 

        elif (ask.lower() =="n"):
            return "exit"
        else:
            print("ENTER AGAIN!!!(Y/N)")
            ask = input("Do you want to try again?(Y/N) : ")
