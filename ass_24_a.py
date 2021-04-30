count=0
str=input("Enter a string: ")
for i in str:
    if i.isupper():
        count+=1

print("Number of  Upper case leters: ",count)
