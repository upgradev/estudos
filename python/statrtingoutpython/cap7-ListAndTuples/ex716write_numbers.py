def main():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    outifile = open("numberlist.txt", "w")

    for item in numbers:
        outifile.write(str(item)+"\n")

    outifile.close()


if __name__ == "__main__":
    main()
