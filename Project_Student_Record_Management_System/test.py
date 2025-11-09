#Tuple for student record

student_1 = ("Harish",28,"Grade 12")
student_2 = ("Ravi",45,"Grade 18")
student_3 = ("Vinay",29,"Grade 15")

#combind the tuple

students = (student_1,student_2,student_3)

print(f"Numbers of students: {len(students)}")
print(f"Index of Ravi: {students.index(student_2)}")

#Create student Id and Courses
student_ids = {1001,1002,1003,1004}
courses = {"English","Maths","Science","Geography"}

#Set operation

print(f"Student Ids: {student_ids}")
print(f"Courses: {courses}")

#Add new student ids 

new_students = {1005,1006}
student_ids.update(new_students)
print(f"Updated Student Ids: {student_ids}")

#Remove the courses are completed 
completed_courses = {"Maths","English"}
remaining_courses = courses - completed_courses
print(f"Remaining Courses: {remaining_courses}")

#Frozen sets use

frozen_courses = frozenset({"Maths","English","Science","History","Social"})
print(f"Frozen Courses: {frozen_courses}")
#if you add below line it will show error
#frozen_courses.add("Art")

#Create a frozen set of  student data

frozen_student_data = frozenset(students)
print(f"Frozen Student Data: {frozen_student_data}")