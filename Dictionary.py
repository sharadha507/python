def invert_content(dic):
    invert_dic = {}
    invert_dic = {v:k for k,v in dic.items()}
    return invert_dic
n=int(input("enter no of values"))
dic={}
for i in range(n):
    key=input("enter keys")
    value=input("enter values")
    dic[key]=value
    print(dic)
    print("after invertion")
    print("invert_content(dic")