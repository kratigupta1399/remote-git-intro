"####this is bank application###"
import json
bank ={
    'user':['krati','nikhil','chinki','gaurav'],
    'acc':['AC1','AC2','AC3','AC4'],
    'password':['python','oops','linux','redhat'],
    'balance':[15000,25000,35000,45000],
}

f = open("bank_db", "w") 
json.dump(bank, f)
f.close()
print("file created suceesfully")

from getpass import getpass
import json
f=open('bank_db')
data=json.load(f)
f.close()

while True:
    print("-----!!!WELCOME TO THE SBI BANK!!!-----")
    print("\n 1.LOGIN\n 2.SIGNUP\n 3.EXIT")
    choice=int(input("Enter Your Choice:  "))
    
    
    if choice==1:
        uacc=input("Enter Your Account Number:   ")
        if uacc in bank['acc']:
            upass=getpass("Password:  ")
            index=bank['acc'].index(uacc)
            if bank['password'][index]==upass:
                print("\nWelcome User ")
                
                while True:
                    print("\n 1.DEBIT\n 2.CREDIT\n 3.LOGOUT")
                    ch=int(input("Enter Your Choice:  "))
                    if ch==1:
                        bal=int(input("\nEnter amount to debit:  "))
                        if bal > bank['balance'][index] :
                            print("Insufficient account balance to withdrawn.")
                        else:
                            bank['balance'][3]-=bal
                            print("Cash withdrawn from your account",bal)
                            print()
                            f.close()
                            f=open('bank_db','w')
                            json.dump(bank,f)
                            f.close()
                    elif ch==2:
                        bal=float(input("\nEnter balance to Deposite: "))
                        bank['balance'][3]+=bal
                        f=open('bank.txt','w')
                        json.dump(bank,f)
                        f.close()
                        print("Your account sucessfully updated")
                        print()
                    elif ch==3:
                        print("\nLogging out.....")
                        break
        else:
            print("Invalid password try again!!")
    elif choice==2:
            bank['acc'].append('AC'+str(int(bank['acc'][-1][-1])+1))
            name=input("\nEnter Name:  ")
            password=getpass("set password: ")
            bal=int(input("Enter Initial Balance:  "))
            #acc='AC'+str(int(max(bank.keys())[4:]) + 1).zfill(5)
            bank['user'].append(name)
            #bank['acc'].append(acc)
            bank['password'].append(password)
            bank['balance'].append(bal)
            f=open('bank_db','w')
            json.dump(bank,f)
            f.close()
            print("!!!Account created sucessfully!!!")
            print("!!Now you can login.")
            
    elif choice==3:
           # print("do you really exit? (y/n): ")
            ch=input("do you really exit?? (yes/no): ")
            if ch=='yes'or ch=='no':
                print("!!!!\n Thanks for using our service!!!!")
                break
    else:
        print("!!Invalid Choice Try Again!!")


bank_db={
    'user':['krati','nikhil','chinki','gaurav'],
    'acc':['AC1','AC2','AC3','AC4'],
    'password':['python','oops','linux','redhat'],
    'balance':[15000,25000,35000,45000],
    
}
