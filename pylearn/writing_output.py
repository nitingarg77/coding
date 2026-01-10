#python output
#txt_data = "I dont like pizza"
import json
import csv
employees = [["Name", "Age", "job"],
             ["Nitin", 40, "Business"],
             ["Sachin", 37, "Profession"],
             ["Kapil", 35, "OT"]]

file_path = "/home/nitin/Desktop/output.csv"

try:
    with open(file_path,"w") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"json file '{file_path}' has been created")


except FileExistsError:
    print("That file already exyst")
