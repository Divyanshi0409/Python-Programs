def prime(x):
    if x==1 or x==2 or x==3:
        print("Prime Number")
    else:
        number=int(x/2 +1)
        p=0
        for i in range(2,number):
            if x%i==0:
                p=1
                print("Not Prime Number")
                break
            else:
                continue
        if p==0:
            print("Prime number")

number=int(input("Enter a number to check if it is prime or not "))
prime(number)