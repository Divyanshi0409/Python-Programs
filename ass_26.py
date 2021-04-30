string= input("Enter a string: ")
string=string.upper()

freq: dict={}
st: set={*string}

for c in string:
    if c in freq:
        freq[c]+=1
    else:
        freq[c]=1

for c in st:
    print(f'{c} {freq[c]}')
