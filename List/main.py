# # Increment number by one
# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
# print(numbers)
# print(new_numbers)
#
# # print letters in names
# name = "Arjun"
# new_name = [n for n in name]
# print(new_name)
#
# # Double number
# double_range = [n * 2 for n in range(1, 5)]
# print(double_range)
#
# # Name uppercase
# names = ["Arjun", "Althaf", "Sijo", "Jishnu", "Anandakrishnan", "alice", "Bob", "Charlie", "Dave"]
# print([name for name in names if len(name) <= 5])
# cap_name = [name.upper() for name in names]
# print(cap_name)
#
# # squared number
# numbers = input().split(',')
# squared_numbers = [int(num) * int(num) for num in numbers]
# print(squared_numbers)


with open('file1.txt') as f1:
    line_1 = f1.readlines()
with open('file2.txt') as f2:
    line_2 = f2.readlines()

new_file = [int(n1) for n1 in line_1 if n1 in line_2]
print(new_file)
