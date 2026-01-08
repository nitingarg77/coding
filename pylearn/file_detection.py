# python file detection

import os

file_path = "~/tech/coding/pylearn/2D_list.py"

if os.path.exists(file_path):
    print(f"the location '{file_path}' exits.")
else:
    print(f"the location '{file_path}' does not exists. ")
