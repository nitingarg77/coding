# exception = an event that intrupt the flow of a program ( ZeroDivisionError, TypeError,   
# ValueError)
# 1.try 2. except 3. finally

try:
    number = int(input("Enter a number"))
    print(1/number)

except ZeroDivisionError:
    print("You cant divide by zero")
    
except ValueError:
    print("You cant enter word")
   
except Exception:
    print("some thing is wrong")


finally:
    print("Do some clean up")