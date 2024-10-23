def runMatch():
    num = int(input("Enter a number between 1 and 3: "))
    match num:
        case 1:
            print("One")
        case 2:
            print("Two")
        case 3:
            print("Three")
        case _:
            print("Number not between 1 and 3")  
runMatch()