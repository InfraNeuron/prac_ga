list1=[17,22,32,34,75,26,47,68,39]
flag=1

number1=int(input("Enter the number to be searched: "))

for i in range(len(list1)):
    if list1[i]==number1:
        print("Number is found at index '" +str(i)+"' of list")
        flag=2
        break
if(flag==1):
    print("Number does not exist in list")
