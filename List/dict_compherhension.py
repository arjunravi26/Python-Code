text = input("Enter something")
dict_text = {key: len(key) for key in text.split()}
print(dict_text)
