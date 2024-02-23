whether_c = eval(input())
print(f"Whether in cellulitis: {whether_c}")
whether_f = {key: c * 9 / 5 + 32 for (key, c) in whether_c.items()}
print(f"Whether in fahrenheit: {whether_f}")
