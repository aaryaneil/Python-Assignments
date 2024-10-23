def passwordRetype(password):
    x=3
    while(x>0):
        print(f"You have {x} attempts left to retype your password.")
        retypedPass = input("Retype your password :")
        if(password==retypedPass):
            break
        x-=1
    print("You are out of attempts.")

print("Enter you login details")
username = input("Username :")
password = input("Password :")
passwordRetype(password)