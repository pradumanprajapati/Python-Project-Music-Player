#Write a Python program to sum all the items in a list
l1=[5,6,8,9,7,8]
l2=[8,9,8,9,7,8]
v=sum(l1+l2)
print("sum of the list:\n",l1,l2,"\nTotal sum\:n",v)
# secound method
for i in range(len(l1)):
    p=sum(l1)
    print("sum of the l1 elemant\n",p)
    break
