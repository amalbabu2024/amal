n=int(input("Enter the number of strings"))
print("Enter the strings")
list=[]
for i in range(0,n):
    str=input()
    list.append(str)
print(list)
count=0
for i in list:
    for j in i:
        if j=='a':
            count=count+1
print(count)