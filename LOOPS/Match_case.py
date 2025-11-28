#Match case

a = int(input("Entera a number between 1 to 10:"))
match a:
    case 1:
        print("You won a charger.")
    case 6:
        print("You won a bluetooth.")
    case 8:
        print("You won a camera.")
    case _:
        print("Better luck next time.")