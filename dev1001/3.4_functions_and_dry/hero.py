class Flyer:
    def __init__(self, *args, **kwargs):
        print("Flyer init")
        super().__init__(*args, **kwargs)

class Shooter:
    def __init__(self, gun_type, *args, **kwargs):
        print(f"Shooter init with gun_type: {gun_type}")
        super().__init__(*args, **kwargs)

class Hero(Flyer, Shooter):
    def __init__(self, name, gun_type):
        print(f"Hero init with name: {name}")
        super().__init__(gun_type)
        self.name = name
    
h = Hero("Nova", "Plasma Blaster")

class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's Name: {self.name}")

class Labrador(Dog):  # Single Inheritance
    def sound(self):
        print("Labrador woofs")

# Multilevel Inheritance
class GuideDog(Labrador):  # Multilevel Inheritance
    def guide(self):
        print(f"{self.name}Guides the way!")

barry = GuideDog("Barry")
barry.display_name()