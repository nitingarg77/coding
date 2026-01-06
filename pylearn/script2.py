from script1 import *

def fav_drink(drink):
    print(f"My favorite drink is {drink}!")

def main():
    print("This is script2")
    fav_drink("coffee")
    fav_food("pizza")
    print("End of script2")

if __name__ == "__main__":
    main()