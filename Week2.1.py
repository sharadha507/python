'''
5
4 4
3 3 3
2 2 2 2 2
1 1 1 1 1 1
'''
rows=5
for i in range(0, rows):
    for j in range(0, i+1):
        print(rows-i, end=' ')
    print("\r")
row=int(input("Enter number of row"))
i=0
while(i<row):
    j=0
    while(j<i+1):
        print(row-i, end=' ')
        j=j+1;
    i=i+1
    print("\r")