num=int(input("enter a number:"))
number=num
digits_sum=0
n = len(str(num))
while(number >0):
    digit=number%10
    digits_sum+=digits_sum**n
    number=number//10
if(number==num):
    print("yes")
else:
    print("no")
