def calculate_gpa(grade):
    if grade == "A":
        return 5
    elif grade == "B":
        return 4
    elif grade == "C":
        return 3
    elif grade == "D":
        return 2
    elif grade == "E":
        return 1
    elif grade == "F":
        return 0
    else:
        print("Invalid grade")
        return None

def main():
    number_of_courses = int(input("Enter total number of courses: "))
    total_score = 0
    total_unit_load = 0

    for _ in range(number_of_courses):
        grade = input("Enter grade: ").upper()  # Convert input to uppercase for case-insensitivity
        unit_load = int(input("Enter the unit load: "))

        grade_value = calculate_gpa(grade)
        
        if grade_value is not None:
            # calculating grades
            gpa = grade_value * unit_load
            total_score += gpa
            total_unit_load += unit_load
        else:
            # Skip invalid grades
            continue

    if total_unit_load == 0:
        print("No valid courses entered. Cannot calculate CGPA.")
    else:
        total_gpa = round(total_score / total_unit_load, 2)
        print(f"Your CGPA is {total_gpa}")

if __name__ == "__main__":
    main()
