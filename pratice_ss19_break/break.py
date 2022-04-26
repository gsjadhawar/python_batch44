n_str=input("enter the size of list")
n=int(n_str)

i=0
L=[]
while i<n:
    element_str=input("enter the element in L list:")
    element=int(element_str)
    L.append(element)
    i=i+1
print("printing entered List L:",L)

m=0
for x in L:
    if x % 7 == 0:
        break
    m=m+1

if m == n:
    print("all iteration completed")
else:
    print("not all iteration completed")
