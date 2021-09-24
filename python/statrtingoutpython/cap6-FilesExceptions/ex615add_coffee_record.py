
from os import write


def main():
    another = "y"

    coffee_file = open("coffee.txt", 'a')

    while another == "y" or another == "Y":
        print("Enter the following coffee data: ")
        descr = input("Description: ")
        qty = int(input("Quantity (in pounds): "))

        coffee_file.write(descr + "\n")
        coffee_file.write(f"{qty}\n")

        print("Do you want to add another records? ")
        another = input("Y = yes, anything else = no ")

    coffee_file.close()
    print("Data appended to coffee.txt")


if __name__ == "__main__":
    main()
