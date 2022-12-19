class animal:
    def speak(self):
        print("Animal Speaks.")
class dog(animal):
    def bark(self):
        print("Dog Bark.")
d=dog()
d.speak()
d.bark()