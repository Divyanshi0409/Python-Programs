string=input("Enter a string: ")
string=string.replace(" ","")

print("String without blank spaces is",string)

length = len(string)
str1=""

for i in range(length):
    if(i%2==0):
        str1 +=string[i]

print("String having characters at even place: ",str1)

print("Reversed string is: ",str1[::-1])