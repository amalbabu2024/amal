a=input("Enter a line of text: ")
dict1={}
b=a.split()
print(b)
for i in b:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
    print("word frequency is :")
    for k, v in dict1.items():
        print(k,v)