
def main():
    emp_file = open("./employees.txt", "r")

    name = emp_file.readline()

    while name != "":
        id_num = emp_file.readline()

        dept = emp_file.readline()

        # strip the newlines from the field
        name = name.strip("\n")
        id_num = id_num.strip("\n")
        dept = dept.strip("\n")

        # dispplay records
        print(f"Name: {name}")
        print(f"Id: {id_num}")
        print(f"Dept: {dept}")
        print()

        name = emp_file.readline()
    emp_file.close()


if __name__ == "__main__":
    main()
