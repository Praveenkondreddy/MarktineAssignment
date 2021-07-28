a=input("Input :").split(",")
n=[]
for i in a:
    l=[]
    for j in a:
        if sorted(i)==sorted(j):
            l.append(j)
    n.append(sorted(l))
unique_list=[]    
for x in n:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
print(unique_list)
