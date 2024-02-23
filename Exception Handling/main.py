try:
    data = [1, 2, 3]
    print(data[3])
except IndexError as error_message:
    print(f" {error_message} ")
