

def main():
    try:
        hours = int(input("How many hours did you work? "))
        pay_rate = float(input("Enter your hourly pay rate: "))

        gross_pay = hours * pay_rate

        print(f"Gross pay: ${gross_pay:,.2f}")
    except ValueError:
        print("Error: Hours worked and hourky pay rate must be valid numbers")


if __name__ == "__main__":
    main()
