# This program uses the writelines method to save
# a list of strings to a file.

def main():
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']
    outfile = open("cities.txt", "w")
    outfile.writelines(cities)
    outfile.close()


if __name__ == '__main__':
    main()
