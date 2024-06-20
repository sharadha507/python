array1=[3,5,7,9]
array2=[9,8,4,0]
common_array=[]
for i in array1:
    if i in array2:
        common_array.append(i)
print(common_array)