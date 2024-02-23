def add(*args):
    sum_of_numbers = 0
    for n in args:
        sum_of_numbers += n
    return sum_of_numbers


print(add(1, 7, 8, 9, 10, 23, 5))
