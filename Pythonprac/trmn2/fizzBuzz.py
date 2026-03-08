numb1=int(input("Enter thr number: "))
list1=[1]
for i in range((numb1)-1):
    list1.append(list1[i]+1)
print(list1)

for i in range(len(list1)):
    if list1[i]%3==0 and list1[i]%5==0:
        list1[i]="FizzBuzz"
    elif list1[i]%3==0:
        list1[i]="Fizz"
    elif list1[i]%5==0:
        list1[i]="Buzz"
print(list1)
