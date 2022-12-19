class animal:
    def sound(self):
        print("Animal makes sound.")
class dog(animal):
    def sound(self):
        print("Dog Barks")
o=dog()
o.sound()