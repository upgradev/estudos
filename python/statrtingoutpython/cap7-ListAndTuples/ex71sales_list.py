NUM_DAY = 5


def main():
    sales = [0] * NUM_DAY
    print("enter the sales for each day: ")
    for index in range(len(sales)):
        sales[index] = float(input(f"Day #{index + 1}: "))
    print("here are the values you entered: ")
    for value in sales:
        print(value)
    

if __name__ == "__main__":
    main()
