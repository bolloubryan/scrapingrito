fileopener = open("matpart.txt", "r")
allsummoners = fileopener.read()

for list in allsummoners:
    print(len(list))
    if (len(list) == 11):
        print(list[len(list)-1])