num_students = int(input("How many students do you have? "))

num_test_scores = int(input("How many test score per student? "))

for student in range(num_students):
    total = 0.0

    print(f"Student number {student + 1}")
    print("----------")

    for test_num in range(num_test_scores):
        print(f"Test number {test_num + 1}", end="")
        score = float(input(": "))

        total += score

    average = total / num_test_scores

    print(f"The average for student number {student + 1} is {average:.1f}")
    print()
