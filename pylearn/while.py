num = float(input("enter a number 1 - 10: "))

while num < 1 or num > 10:
    print("number not in range, try again")
    num = float(input("enter a number 1 - 10"))
print("thank you!") 
print(f"you entered: {num:.2f}")