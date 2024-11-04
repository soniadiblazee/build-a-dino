# the base class !
class jurDino:
    def __init__ (self,name,species,age,diet):
        self.name = name
        self.species = species
        self.age = age
        self.diet = diet

    def roar(self):
        print(f"{self.name} roars")

    def eat(self,food):
        if food == self.diet:
            print(f"{self.name} eats food.... yummers......")
        else:
            print(f"{self.name} does not eat {food}")

    def dinoInfo(self):
        return (f"{self.name} is a {self.species} and is {self.age} years old. She eats {self.diet}.")


#! subclasses for different types of dinosaurs
class flyingDino(jurDino):
    def __init__(self,name,species,age,diet,wingspan):
        super().__init__(name,species,age,diet)
        self.wingspan = wingspan

    def roar(self):
        print(f"{self.name} schreeches in the sky")

class waterDino(jurDino):
    def __init__(self,name,species,age,diet,swimSpeed):
        super().__init__(name,species,age,diet)
        self.swimSpeed = swimSpeed

    def roar(self):
        print(f"{self.name} roars while underwater")

#! getter method for dinosaur's age (the underscore makes it so the 
#! age attribute is private)
def getAge(self):
    return self._age


dino1 = flyingDino("Perry","Pterodactyl",136,"meat",3)
dino2 = jurDino("Blue","Velociraptor",9,"meat")


dino1.roar()
dino2.roar()