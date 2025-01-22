class Pet:
    def __init__(self, name, species, breed, age, weight):
        self.name = name
        self.spices = species
        self.breed = breed
        self.age = age
        self.weight = weight

    def retrieve_pet(self):
        print(f"Name: {self.name}")
        print(f"spices: {self.spices}")
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight}")


my_pet = Pet("Max", "Dog", "Boston Terrier", 3, 10)

print(my_pet.retrieve_pet())

