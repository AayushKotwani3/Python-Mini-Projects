import Secretlanguage as sl

# master_password=input("What is Your Master Password")

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user,encrypted_password=data.split('|')
            decrypted_password=sl.decode(encrypted_password)
            print('username :',user,'| password :',decrypted_password)    

def add():
    Account_name=input("Enter name of Your Account: ")
    Password=input("Enter Password: ")
    
    encrypted_password=sl.encode(Password)

    with open('password.txt','a') as f:
        f.write(Account_name+'|'+encrypted_password+"\n")

while True:
    mode=input("Do you want to add a new password or view an older one (view/add) or presss q to quit").lower()

    if mode=='q':
        break

    if mode=='add':
        add()
    elif mode=='view':
        view()
    else:
        print('Invalid mode')