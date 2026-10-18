# TASK 2: Learner Report Functions
# Topics: def, function calls, parameters, arguments, return, conditions

def get_result(mark):
    if mark >= 50:
        return "PASS"
    else:
        return "FAIL"
    # TODO 1: If mark is 50 or more, return "PASS"
    # TODO 2: Otherwise, return "FAIL"


def calculate_percentage(mark, total_marks):
    percentage = mark/total_marks * 100
    return percentage
    # TODO 3: Calculate the percentage
    # Formula: mark / total_marks * 100
    # TODO 4: Return the percentage


print("=== Learner Report ===")

learner_name = input("Enter learner name: ")
mark = float(input("Enter mark obtained: "))
total_marks = float(input("Enter total possible marks: "))

percentage = calculate_percentage(mark, total_marks)
results = get_result(percentage)

print(f'{learner_name}, Percentage: {percentage}, Results: {results}')
# TODO 5: Call calculate_percentage() and save the returned value

# TODO 6: Call get_result() and save the returned value

# TODO 7: Display learner_name, percentage, and result
