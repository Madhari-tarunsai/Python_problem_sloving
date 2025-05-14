num=int(input("enter a number:"))
temp=num
reverse=""
while(temp > 0):
    digit=temp%10
    reverse+=str(digit)
    temp = temp // 10
print(reverse)