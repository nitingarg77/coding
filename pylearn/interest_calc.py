#python compound interest calculatotor

principle = 0
roi = 0
time = 0

while True: #principle <0:
    principle = float(input("Enter the principle amount: "))
    if principle <0:
        print("Principle amount must be greater than 0.")
    else:
        break
while True: #roi <0:
    roi = float(input("Enter the rate of interest: "))
    if roi <0:
        print("Rate of interest must be greater than 0.")
    else:
        break

while True: #time <0:
    time = float(input("Enter the time period: "))
    if time <0:
        print("Time period must be greater than 0.")
    else:
        break
total = principle * ( (1 + roi/100) ** time)

print(f"The total amount after {time} years is: {total:.2f}")


#print(principle)
#print(roi)
#print(time)