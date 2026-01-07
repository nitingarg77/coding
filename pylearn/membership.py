students = {"alice", "bob", "charlie", "david"}

def is_student(name):
    return name in students 
# Example usage:
print(is_student("alice"))  # True
print(is_student("eve"))    # False