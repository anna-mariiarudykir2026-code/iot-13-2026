from enum import Enum

class Kind(Enum):
    DOG = "dog"
    CAT = "cat"
    BIRD = "bird"


class Pet():
    def __init__(self, name, breed, age, greeting, mass, kind):
        self.name = name
        self.breed = breed
        self.age = age
        self.greeting = greeting
        self.mass = mass
        self.kind = kind

    def is_polite(self):
        if "Hello" in self.greeting:
            return True
        else:
            return False


class Home():
    def __init__(self):
        self.pet = []

    def add(self, pet):
        self.pet.append(pet)

def are_friends(pets_array):
    friends = []

    for i in range(len(pets_array)):
        for j in range(i + 1, len(pets_array)):
            if abs(pets_array[i].age - pets_array[j].age) < 2:
                friends.append((pets_array[i].name, pets_array[j].name))
                return friends

def sort_by_age(pets_list):
    return sorted(pets_list, key=lambda pet:pet.age)
  

if __name__ == "__main__":
    p1 = Pet("Франциск", "Німецька вівчарка", 3, "Woof! Hello!", 15.0, "DOG")
    p2 = Pet("Мурка", "Британка", 4, "Meow", 4.0, "CAT")
    p3 = Pet("Пірат", "Папуга", 1, "Hello!Where is my food?", 0.2, "BIRD")

    my_home = Home()
    my_home.pet.append(p1)
    my_home.pet.append(p2)
    my_home.pet.append(p3)

    print("Франциск ввічливий пес?:", p1.is_polite())
    print("Мурка ввічлива киця?:", p2.is_polite())
    print("Пари друзів:")
    print(are_friends(my_home.pet)) 

    print("Тварини від наймолодшої до найстаршої:")
    sorted_pets = sort_by_age(my_home.pet)
    for pet in sorted_pets:
        print(pet.name, "-", pet.age, "роки")
