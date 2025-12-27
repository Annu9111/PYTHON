x=int(input("enter a number:  "))
#x is variable to match
match x:
    # if x matches
    case 0:
        print("you typed 0")
    case 2:
        print("you typed 2")
    # if x does not matches
    case _:
        print("i dont know what you typed")        