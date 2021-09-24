
def main():
    num_videos = int(input("How many videos are in the project? "))
    video_file = open("video_times.txt", "w")
    print("Enter the running times for each video")
    for count in range(1, num_videos + 1):
        run_time = float(input(f"Video #{count}: "))
        video_file.write(f"{run_time}\n")
    video_file.close()
    print("The times have been saved to video_times.txt")


if __name__ == "__main__":
    main()
