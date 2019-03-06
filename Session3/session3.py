ls=["T-shirt","Sweater"]
while True:
    print("Welcom to our shop, what do you want")
    print("R: See all Item")
    print("C: Add new Item")
    print("U: Update Item")
    print("D: Delete Item")
    button=input("")
    if button == "R":
        print("Our Item: ",(ls))
    if button == "C":
        new=input("Enter new item: ")
        ls.append(new)
        print("Our Item: ",(ls))
    if button == "U":
        pos=int(input("Update position ?"))
        new=input("Enter new item: ")
        if pos<=len(ls):
            ls[pos-1]=new
        else:
            print("Your Position not exist !")
        print("Our Item: ",(ls))
    if button =="D":
        pos=int(input("Delete Position? "))
        if pos <=len(ls):
            ls.remove(ls[pos-1])
        else:
            print("Your Position not exist !")
        print("Our Item: ",(ls))
    
