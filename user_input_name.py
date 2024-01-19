 print kankarla ramya
name=input("enter any name:")
m=0
for x in range (len(name)):
    print(f"{name[m]}: {name.count(name[m])}")
    m=m+1
