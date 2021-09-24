import math

def main():
    a = float(input("Enter the lenght A: "))
    b = float(input("Enter the lenght B: "))

    c = math.hypot(a, b)

    print(f"The lenght of the hypotenuse is {c}")

main()