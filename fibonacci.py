def fibonacci(x):
    if x==0:
        return 0
    elif x==1 or x==2:
        return 1
    else:
        return(fibonacci(x-1)+ fibonacci((x-2)))

num=int(input("Enter the total numbers you want in fibonacci series: "))
for i in range(0,num):
    fib=fibonacci(i)
    print(fib)