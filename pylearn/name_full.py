#from functions import hbd
import functions as fn

def create_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    full_name = f"{first_name} {last_name}"
    return full_name
print(create_name("john", "doe"))
print(create_name("jane", "smith"))
print(create_name("alice", "johnson"))
print(create_name("bob", "brown"))     
#name = create_name("john", "doe")
fn.hbd(create_name("john", "doe"), 25)