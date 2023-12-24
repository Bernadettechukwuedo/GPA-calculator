# A code used to calculate your cgpa
number = int(input("Enter total number of courses: "))
count = 0
count_score = 0
count_UnitLoad = 0
score = []

# using a while condition to loop through
while count != number:
    global grade
    grade = input("Enter grade: ").upper()
    if grade == "A":
        score = 5
    elif grade == "B":
        score = 4
    elif grade == "C":
        score = 3
    elif grade == "D":
        score = 2
    elif grade == "E":
        score = 1
    elif grade == "F":
        score = 0
    else:
        print("Opps! wrong grade. The grade ranges from A to F")

        continue
    unit_load = int(input("Enter the unit load: "))

    # calculating grades
    gpa = score * unit_load
    count_score += gpa
    count_UnitLoad += unit_load
    count += 1


total_gpa = round(count_score / count_UnitLoad, 2)

print(f"Your CGPA is {total_gpa}")
