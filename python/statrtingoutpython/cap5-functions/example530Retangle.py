def area(width, length):
    return width * length

def perimeter(width, length):
    return 2 * (width + length)

def main():
    width = float(input("Enter the rectangle width: "))
    length = float(input("Enter the rectangle length: "))
    print("The area is ", area(width, length))
    print("The perimeter is ", perimeter(width, length))

if __name__ == '__main__':
    main()