list1=[1,2,3,4,5]
list2=[2,4,6,8,10]
a=len(list1)
b=len(list2)
if(a==b):
    print("both lists have same length ",a)
else:
    print("both have different lengths",a,b)
if(sum(list1)==sum(list2)):
    print("both the sum are same")
else:
    print("both the sums are not same")
print("common element are")
for i in list1:
    for j in list2:
        if(i==j):
            print(i)