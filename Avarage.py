students = []

with open("marks.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")

        name = data[0]
        marks = list(map(int, data[1:]))

        avg = sum(marks) / len(marks)

        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        else:
            grade = "C"

        students.append(f"{name} - Average: {avg:.2f} - Grade: {grade}")

with open("report.txt", "w") as report:
    for student in students:
        report.write(student + "\n")

print("Report Generated Successfully!")