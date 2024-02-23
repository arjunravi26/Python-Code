import random

names = ["alice", "Bob", "Charlie", "Dave"]
student_score = {student: random.randint(1, 100) for student in names}
print(student_score)
passed_student = {key for (key, mark) in student_score if mark > 35}
print(passed_student)
