name = "Nitin Garg"
age = 25
gpa = 8.5
is_student = True
type(name)

print(type(name))         # Output: <class 'str'>
print(type(age))          # Output: <class 'int'>
print(type(gpa))          # Output: <class 'float'>
print(type(is_student))   # Output: <class 'bool'>

gpa = int(gpa)
print(gpa)                # Output: 8
print(type(gpa))         # Output: <class 'int'>
age = float(age)
print(age)                # Output: 25.0
print(type(age))         # Output: <class 'float'>
is_student = str(is_student)
print(is_student)        # Output: 'True'
print(type(is_student))  # Output: <class 'str'>
name = bool(name)
print(name)              # Output: True
print(type(name))       # Output: <class 'bool'>
