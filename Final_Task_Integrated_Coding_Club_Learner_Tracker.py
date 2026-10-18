# FINAL TASK: Coding Club Learner Tracker
# Combines Day 1 loops + Day 2 functions + Day 3 lists

names = []
marks = []
grades = []
statuses = []


def calculate_grade(mark):
    if mark  >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"
    # TODO 1: Return A, B, C, D, or F using the grade rules
    # A: 80+, B: 70+, C: 60+, D: 50+, F: below 50
    


def check_status(mark):
    if mark >= 50:
        return "PASS"
    else:
        return "FAIL"
    # TODO 2: Return "PASS" if mark >= 50, otherwise return "FAIL"
    


def calculate_average(mark_list):
    if not mark_list:
        print("Mark list is empty")
        return 0
    else:
        average = sum(mark_list)/len(mark_list)
        return average
    # TODO 3: Return the average of the marks in mark_list
    # Hint: use sum() and len(), but check for an empty list first
    


print("=== Coding Club Learner Tracker ===")

while True:
    learner_name = input("Enter learner name (or done to finish): ").strip()
    if learner_name.lower() == "done":
        break
    elif learner_name.lower == "":
        print("Name cannot be empty")
        continue

    # TODO 4: Use strip() to remove extra spaces

    # TODO 5: If learner_name.lower() == "done", break out of the loop

    # TODO 6: If learner_name is blank, display a message and continue

    mark = float(input("Enter mark (0-100): "))
    if not (0 <= mark <= mark):
        print("Invalid mark")

    grade = calculate_grade(mark)
    status = check_status(mark)

    names.append(learner_name)
    marks.append(mark)
    grades.append(grade)
    statuses.append(status)  

    # TODO 7: Validate that mark is between 0 and 100.
    # If invalid, display a message and continue

    # TODO 8: Call calculate_grade(mark) and save the grade

    # TODO 9: Call check_status(mark) and save the status

    # TODO 10: Append name, mark, grade, and status to the matching lists


print("\n=== LEARNER REPORT ===")

for name,mark,grade,status in zip(names,marks,grades,statuses):
    print(f'{name} - Mark:{mark}, Grade:{grades}, Status:{status}')
print(f'\nTotal learners: {len(names)}')

class_average = calculate_average(marks)
print(f'Class average: {class_average}')
# TODO 11: Use a for loop over the indexes or use zip() to display:
# learner name, mark, grade, and status

# TODO 12: Display total learners using len(names)

# TODO 13: Call calculate_average(marks) and display the class average
