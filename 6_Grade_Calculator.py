# Q6 - Grade Calculator
# This program calculates total, percentage, grade and pass/fail result.

try:
    marks_list = []

    # Taking marks for 5 subjects
    for i in range(1, 6):
        marks = float(input(f"Enter marks for subject {i}: "))
        marks_list.append(marks)

    # Calculating total and percentage
    total_marks = sum(marks_list)
    percentage = total_marks / 5

    # Determining grade
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    # Checking pass condition (each subject must be >= 40)
    if all(mark >= 40 for mark in marks_list):
        result = "Pass"
    else:
        result = "Fail"

    # Output
    print("\nTotal Marks:", total_marks)
    print("Percentage:", percentage)
    print("Grade:", grade)
    print("Result:", result)

except ValueError:
    print("Please enter valid marks.")