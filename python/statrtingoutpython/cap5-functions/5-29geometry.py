import circle
import rectangle

AREA_CIRCLE_CHOICE = 1
CIRCUNFERENCE_CHOICE = 2
AREA_RETANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

def main():
    choice = 0

    while choice != QUIT_CHOICE:
        display_menu()

        choice = int(input("Enter you choice: "))
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print('The area is ', circle.area(radius))
        elif choice == CIRCUNFERENCE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print("The circunference is ", circle.circunference(radius))
        elif choice == AREA_RETANGLE_CHOICE:
            width = float(input("Enter the retangule width: "))
            length = float(input("Enter the retangule length: "))
            print("The area is ", rectangle.area(width, length))
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input("Enter the retangule width: "))
            length = float(input("Enter the retangule length: "))
            print("The perimeter is ", rectangle.perimeter(width, length))
        elif choice == QUIT_CHOICE:
            print("Exiting the program...")
        else:
            print("Error: Invalid selection")

def display_menu():
    print("MENU")
    print("1) Area of a circle")
    print("2) Circunference of a circle")
    print("3) Area of a retangule")
    print("4) Perimeter of a retangule")
    print("5) Quit")

main()