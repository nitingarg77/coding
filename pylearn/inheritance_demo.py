

class Animal:
    def __init__(self, name, is_alive):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} does woof woof")



class Cat(Animal):
    def speak(self):
        print(f"{self.name} does Meow")

class Mouse(Animal):
    def speak(self):
        print(f"{self.name} does Squeek")




dog = Dog("leo", True)
cat = Cat("Kiki", True)
mouse = Mouse("Jimi", True)

print(dog.name)

dog.eat()
cat.sleep()
dog.speak()
cat.speak()
mouse.speak()