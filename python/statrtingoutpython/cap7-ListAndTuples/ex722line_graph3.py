import matplotlib.pyplot as plt


def main():
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    plt.plot(x_coords, y_coords)

    plt.title("Sample Data")

    plt.xlabel("label X  axis")
    plt.ylabel("label Y axis")

    # set the axis limits
    plt.xlim(xmin=-1, xmax=10)
    plt.ylim(ymin=-1, ymax=6)

    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    main()
