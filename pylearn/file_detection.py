# python file detection

import os

file_path = "/home/nitin/Desktop/test.txt"

if os.path.exists(file_path):
    print(f"the location '{file_path}' exits.")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That's a folder")
else:
    print(f"the location '{file_path}' does not exists. ")


#print(os.path)
