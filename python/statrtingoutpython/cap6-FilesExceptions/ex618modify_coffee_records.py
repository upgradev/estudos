import os


def main():
    found = False

    search = input("Enter a description to search for: ")
    new_qty = int(input("Enter the new quantity: "))

    coffee_file = open("./coffee.txt", "r")

    # file temp
    temp_file = open("temp.txt", "w")

    descr = coffee_file.readline()

    while descr != "":
        qty = float(coffee_file.readline())
        descr = descr.rstrip("\n")

        if descr == search:
            temp_file.write(f"{descr}\n")
            temp_file.write(f"{new_qty}\n")

            found = True
        else:
            temp_file.write(f"{descr}\n")
            temp_file.write(f"{qty}\n")
        descr = coffee_file.readline()
    coffee_file.close()
    temp_file.close()

    # delete the original coffee.txt
    os.remove("./coffee.txt")

    # rename the temporary file
    os.rename("temp.txt", "coffee.txt")

    if found:
        print("The file has been updated")
    else:
        print("That item was not found in the file")


if __name__ == "__main__":
    main()
