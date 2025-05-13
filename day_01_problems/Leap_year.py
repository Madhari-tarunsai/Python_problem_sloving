num=int(input("enter a year:"))
if( num%400==0 and num%100!=0 or num%2==0):
    print("{} is leap year".format(num))
else:
    print("not")