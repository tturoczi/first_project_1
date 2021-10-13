menu=("valassz 1, 2 ,3")
names= []
i=0

while(i!=3):
    i=int(input(menu))
    if (i==1):
        names.append(input("add meg a nevet"))
        print("köszi")
    elif(i==2):
        print(names)
    elif(i==3):
        print("kilepes")
    else:
        print("gyoker vagy")



