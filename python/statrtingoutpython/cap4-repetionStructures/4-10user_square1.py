end = int(input("How high should i go? "))

print()
print("number\tsquare")
print("----------------")

for number in range(1, end + 1):
    square = number**2
    print(f"{number}\t{square}")