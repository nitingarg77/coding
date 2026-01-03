num = -5
a = 6
b = 7
user_role = 'guest'
max = a if a > b else b
print("max:", max)
min = a if a < b else b
print("min:", min)
abs_value = -num if num < 0 else num
print("abs_value:", abs_value)

access_level = 'full' if user_role == 'admin' else 'limited'
print("access_level:", access_level)    