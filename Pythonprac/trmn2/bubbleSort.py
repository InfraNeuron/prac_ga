# important 1
list1=[3,8,4,7,2,9,1]
for i in range(len(list1)):
    for j in range(len(list1)-1):
        if (list1[j]>list1[j+1]):
            temp=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=temp

print("Sorted list is \n",list1)
