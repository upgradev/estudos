
def main():
    num_emps = int(input("How many employee records do you want to create? "))

    emp_file = open("employees.txt", "w")

    for count in range(1, num_emps + 1):
        print(f"Enter data for emplyee #{count}")
        name = input('Name: ')
        id_num = input("ID Number: ")
        dept = input("Department: ")

        emp_file.write(f"{name}\n")
        emp_file.write(f"{id_num}\n")
        emp_file.write(f"{dept}\n")

        print()
    emp_file.close()


if __name__ == "__main__":
    main()
