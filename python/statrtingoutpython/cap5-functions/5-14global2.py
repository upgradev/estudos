number = 0


def main():
    global number
    number = int(input("enter a number: "))
    show_number()


def show_number():
    print(f"the number you entered is {number}")


main()
