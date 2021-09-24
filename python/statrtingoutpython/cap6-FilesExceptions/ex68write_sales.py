def main():
    num_days = int(input("For how many days do you have sales? "))
    sales_file = open("sales.txt", "w")

    for count in range(1, num_days + 1):
        sales = float(input(f"Enter tha sales for day #{count}: "))

        sales_file.write(f"{sales}\n")
    sales_file.close()
    print("Data written to sales.txt")


if __name__ == "__main__":
    main()
