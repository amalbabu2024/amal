n=int(input("Enter the number of elements"))
print("Enter the elements")
list=[]
for i in range(0,n):
    n=int(input())
    if (n>100):
     list.append("Over")
    else:
     list.append(n)
print(list)
