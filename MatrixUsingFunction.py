def read_mat(A,r,c):
    for i in range(r):
        t=[]
        for j in range(c):
            val=int(input(f"Enter the A[{i}][{j}] value"))
            t.append(val)
        A.append(t)
def display_mat(A):
    for i in A:
        print(i)
mat_A=[]
read_mat(mat_A,2,2)
print("mat A")
display_mat(mat_A)
mat_B=[]
read_mat(mat_B,2,2)
print("mat B")
display_mat(mat_B)
c=[]
for i in range(2):
    t=[]
    for j in range(2):
        val=mat_A[i][j]+mat_B[i][j]
        t.append(val)
    c.append(t)
display_mat(c)