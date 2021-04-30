str1=input("Enter a string: ")
str2=input("Enter another string: ")

string=""
for i in range(len(str1)):
    if(str1[i].isupper()):
        string+=str1[i]

for i in range(len(str2)):
    if(str2[i].isupper()):
        string+=str2[i]

print("Concatenated string is:",string)