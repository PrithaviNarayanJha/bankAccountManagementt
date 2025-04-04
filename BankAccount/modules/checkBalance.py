import ast

def CheckBalance(lines):
    with open("BankAccount/BankData/accounts.txt") as chck:
        realchck = chck.readlines()
        line = ast.literal_eval(realchck[lines])
        lines=lines
        bankAccountnum= line["Account Number"]
        BankName = line["Name"]
        BankBalance = line["Balance"]

    print(f"{BankName} You Have {BankBalance}$ in your Bank Account : {bankAccountnum}")