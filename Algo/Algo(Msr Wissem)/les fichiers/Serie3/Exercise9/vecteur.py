def program():
    f1 = open("f1.txt", "r")
    f2 = open("f2.txt", "r")

    ptr1 = f1.readline()[:-1]
    ptr2 = f2.readline()[:-1]

    output = 0

    while( ptr1 != '' and ptr2 != ''):
        output += int(ptr1) * int(ptr2)
        ptr1 = f1.readline()
        ptr2 = f2.readline()

    print("output is: " + str(output))

program()