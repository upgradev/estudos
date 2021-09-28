def main():
    food = ["Pizza", "Burgers", "Chips"]
    print("Here are the items in the food list: ")
    print(food)

    item = input("Which item should I remove? ")

    try:
        food.remove(item)
        print("here is the revised list: ")
        print(food)
    except ValueError:
        print('That item was not found in the list.')


if __name__ == "__main__":
    main()
