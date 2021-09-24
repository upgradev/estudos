keep_going = "y"

while keep_going == "y":
    sales = float(input("enter the amount of sales: "))
    comm_rate = float(input("enter the commission rate: "))

    commission = sales * comm_rate

    print(f"The commison is ${commission:,.2f}")

    keep_going = input("D you want to calculate another commission? (enter y for yes): ")
    