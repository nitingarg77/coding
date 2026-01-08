# python file detection

import os

file_path = "/home/nitin/tech/coding/pylearn/1test.txt"

if os.path.exists(file_path):
    print(f"the location '{file_path}' exits.")
else:
    print(f"the location '{file_path}' does not exists. ")


print(os.path)
