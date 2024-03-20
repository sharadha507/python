try:
    a = int(input("Enter the a value"))
    #b=int(input("enter the b value"))
    c=a/b
    print("value of c:",a/b)
except NameError:
    print("b value is not mentioned")
except ZeroDivisionError:
    print("Arithmatic exception")
except ValueError:
    print("Value exception")
except IndexError:
    print("Array index out of bounds")
except KeyError:
    print("key error")
except IOError:
    print("file input or output error")