ch=input("enter the number of character")
if(ch .islower()):
    print(ch," is lower case alphabets")
elif(ch.isupper()):
    print(ch," is upper case alphabets")
elif(ord(ch)>=48 and ord(ch)<=58):
    print(ch," is digit")
else:
    print(ch," is special character")