from os import sep


def main():
    video_file = open("./video_times.txt", "r")
    total = 0.0
    count = 0
    print("Here are the running times for each video: ")
    for line in video_file:
        # convert a line  to a float
        run_time = float(line)
        count += 1

        print("Video #", count, ": ", run_time, sep="")

        total += run_time
    video_file.close()
    print(f"Total running time is {total:.2f} seconds")


if __name__ == "__main__":
    main()
