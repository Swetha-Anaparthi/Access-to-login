def cred():
    splchar= "!@#$%^&*()_+={}\[]|/;'"",.<>?"
    locase='abcdefghijklmnopqrstuvwxyz'
    upcase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num="0123456789"
    k=l=0
    #id format
    if id[0] in splchar or id[0] in num:
            exit("id should not start with special character or a number")
    if '@' in id:
        id1 = id.split('@')
        if id1[1] != 'gmail.com' and id1[1] != 'yahoo.in':
            exit(" id not in required format")
    else:
        exit("Id not in required format.")
            #password format
    print("REGISTER TO LOGIN:")
    pword = input("Enter the password : ")
    print("Minimum and Maximum length of password is 5 ,16\n "
          "Password must have 1 upper case,1 lowercas,1 digit ,1 splecial character ")
    if len(pword)< 5 : exit("Password too small")
    elif len(pword)>16:exit("Password too long")
    def forconditions(a,b,c):
            k=0
            for i in a:
                if i in b:
                    k+=1
            if k == 0:
                    exit(f" no {c} found")
    forconditions(pword,splchar,'special_character')
    forconditions(pword,num,'number')
    forconditions(pword,locase,'lower_case letter')
    forconditions(pword,upcase,'uppercase letter')
    user=id+" "+pword+"\n"
    file1=open("logins_database.txt","a")
    file1.write(user)
    file1.close()
    print("Run again for access")
print("email format: user_name@gmail.com or user_name@yahoo.in ")
id=input("Enter the email id/user name:\n ")
file2=open("logins_database.txt","r")
readfile=file2.read()
if id in readfile:
    print("Enter the password or Enter 2 to access forget password")
    psword=input()
    with open("logins_database.txt","r") as f:
        for line in f:
            userArray=line.strip().split()
            if (userArray[0]==id):
                if psword== userArray[1]:
                    print("Access granted")
                elif psword=="2":
                    print("Password :",userArray[1])
                else:
                    print("Incorrect password")
                    print("Enter 2 to access forget password")
                    forget=int(input())
                    if forget==2:
                        print("password: ",userArray[1])
                        file2.close()
else:
    cred()

