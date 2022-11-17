str1=input("enter a string")
dict={}
for n in str1:
    if n in dict:
        dict[n]+=1
        print(dict)
    else:
        dict[n]=1
        print(dict)
print("charecter frequency")
for k,v in dict.items():
    print(k,v)