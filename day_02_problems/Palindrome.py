num=input("enter a str:")
low_num=0
high_num=len(num) -1
while(low_num < high_num):
    if num[low_num]!=num[high_num]:
        print("not")
        break
    low_num+=1
    high_num-=1
else:
    print("yes")

