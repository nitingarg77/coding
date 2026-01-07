my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for key in my_dict:
    print(f"Key: {key}")

for key, value in my_dict.items():
    print(f"{key}:{value}")
for value in my_dict.values():
    print(f"Value: {value}")
for index, key in enumerate(my_dict):
    print(f"Index: {index}, Key: {key}")
          