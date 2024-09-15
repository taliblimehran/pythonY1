def main():
    student_name = input("Enter name of the student:\n")
    course_code = input("Enter code of the course:\n")
    exercise_points = int(input("Enter exercise points:\n"))
    project_points = int(input("Enter project points:\n"))

    total_course_points = exercise_points + project_points
    while total_course_points > 60:
        print(f"Total course points are {total_course_points}")
        print("The maximum number of points should be 60.")
        exercise_points = int(input("Enter exercise points:\n"))
        project_points = int(input("Enter project points:\n"))
        total_course_points = exercise_points + project_points

    grade = 0
    if total_course_points >= 0 and total_course_points <= 10:
        grade = 0
    elif total_course_points >= 11 and total_course_points <= 20:
        grade = 1
    elif total_course_points >= 21 and total_course_points <= 30:
        grade = 2
    elif total_course_points >= 31 and total_course_points <= 40:
        grade = 3
    elif total_course_points >= 41 and total_course_points <= 50:
        grade = 4
    elif total_course_points >= 51 and total_course_points <= 60:
        grade = 5

    print(f"Total course points are {total_course_points}")
    if grade == 0:
        print(f"{student_name} did not pass the course {course_code} with the total points being {total_course_points}")
    else:
        print(f"{student_name} received the grade {grade} from the course {course_code} with the total points of {total_course_points}")

main()