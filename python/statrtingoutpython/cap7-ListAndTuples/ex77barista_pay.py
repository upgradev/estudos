
NUM_EMPLOYEES = 6


def main():

    hours = [0] * NUM_EMPLOYEES

    for index in range(NUM_EMPLOYEES):
        hours[index] = float(input(f"Hours worked by employye {index + 1}: "))

    pay_rate = float(input("Hourly pay rate: "))
    for index in range(NUM_EMPLOYEES):
        gross_pay = hours[index] * pay_rate
        print(f"Gross pay for employye {index + 1}: ${gross_pay:,.2f}")


if __name__ == "__main__":
    main()
