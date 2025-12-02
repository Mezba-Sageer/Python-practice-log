from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    def walk(self):
        pass
class Dog(Animal):
    def speak(self):
        return "woof!"
    def walk(self):
        return "dog is walking"
class cat(Animal):
    def speak(self):
        return "meow"
    def walk(self):
        return "cat is strolling"
dog=Dog()
print(dog.speak())
print(dog.walk())

cat=cat()
print(cat.speak())
print(dog.walk())