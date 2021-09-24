rows = int(input("How many rows? "))
cols = int(input("How many cols? "))

for r in range(rows):
    for c in range(cols):
        print("*", end="")
    print()
