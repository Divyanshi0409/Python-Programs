import camelcase


w=[]

words=input("Enter your name: ")

w1=camelcase.CamelCase()
upper = w1.hump(words)

upper=list(upper)

length=len(upper)
i=0

for word in upper:
    if(word!=" " ):
        w.append(word)
    else:
        print(w)
        w=[]
        continue

