# Messy Python Code Improvement
# Example of organizing code into clear functions and readable variables.

def calculate_average(marks):
    """Return the average of a list of marks, or 0 for an empty list."""
    if not marks:
        return 0
    return sum(marks) / len(marks)


def get_result(average):
    """Return Pass or Needs Improvement based on the average."""
    return "Pass" if average >= 40 else "Needs Improvement"


def main():
    student_name = "Student"
    marks = [78, 85, 69, 90, 76]

    average = calculate_average(marks)
    result = get_result(average)

    print("Student:", student_name)
    print("Marks:", marks)
    print("Average:", round(average, 2))
    print("Result:", result)


if __name__ == "__main__":
    main()
