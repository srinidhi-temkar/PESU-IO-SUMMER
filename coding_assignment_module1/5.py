ip=input("Enter a string : ")
if(ip.replace('.','',1).isdigit()):
    print("Numeric string")
else:
    print("Non-numeric string")