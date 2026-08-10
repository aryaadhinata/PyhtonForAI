class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return f"{self.name} says : woof!"
    
    def introduce(self):
        return f"hello i'm {self.name}, {self.bark()}"

a = Dog("burhan")
b = Dog("dohan")

print(a.introduce())
print(b.introduce())