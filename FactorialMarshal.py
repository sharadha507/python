import marshal
src='''
n=5
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
'''
code=compile(src,"src","exec")
fp=open("marshal1.txt","wb")
marshal.dump(code,fp)
fp.close()