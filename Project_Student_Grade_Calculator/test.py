student_a = [82,85,98,72,75]

total_score = sum(student_a)
print(total_score)

num_tests = len(student_a)
print(num_tests)

average_score = total_score // num_tests
print(average_score)

#Grade comaprison

if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

# Update the grade using assignment operator

if average_score % 10 >= 5:
    grade += "+"

#check if specific score exits in the list using membership operators

check_score = 90
if check_score in student_a:
    print(f"The score {check_score} exists in the list")
else:
    print(f"The score {check_score} does not exits in the list")

#Comapre objects using identity operators
scores_copy = student_a

if student_a is scores_copy:
    print("The student_a scores_copy are the same object.")
else:
    print("The student_a and scores_copy are different object")

#Perform bitwise operations on the scores

bitwise_result = student_a[0] & student_a[1]
print(f"Bitwise AND of the first two scores:{bitwise_result}")

#display student's grade 

print(f"The Student's average score is {average_score} and their grade is {grade}")