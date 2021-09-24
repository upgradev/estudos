
def main():
    outfile = open("philosophers.txt", "w")

    outfile.write("John locker\n")
    outfile.write("David hume\n")
    outfile.write("Edmund burker\n")

    outfile.close()


if __name__ == "__main__":
    main()
