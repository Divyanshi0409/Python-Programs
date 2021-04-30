str = input("Enter a string: ")
str=str.lower()
vowels={'a','e','i','o','u'}

count=0
for i in vowels:
    if i in str:
        count+=1
    
    print("Occurence of",i,"in",str,"is",count)