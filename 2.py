st1,st2=input().split(",")
count=0
for i in st1:
    if st2[-1]==i:
        count+=1
print(count)