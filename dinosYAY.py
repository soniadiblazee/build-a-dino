class jurDino:
    def __init__ (self,name,species,age,diet):
        self.name = name
        self.species = species
        self.age = age
        self.diet = diet

    def roar(self):
        print(f"{self.name} says GRRRRAAAGHHGGGGHGHHH")

    def eat(self,food):
        if food == self.diet:
            print(f"{self.name} eats food.... yummers......")
        else:
            print(f"{self.name} does not eat {food}")

    def dinoInfo(self):
        return (f"{self.name} is a {self.species} and is {self.age} years old. She eats {self.diet}.")


raptor1 = jurDino("Blue","Velociraptor",9,"meat")
raptor2 = jurDino("Charlie","Velociraptor",6,"meat")
raptor3 = jurDino("Delta","Velociraptor",8,"meat")
raptor4 = jurDino("Echo","Velociraptor",7,"meat")
rex = jurDino("Rexy","Tyrannosaurus Rex",5,"meat")

print(raptor1.dinoInfo())
raptor3.roar()
raptor4.eat("plant")
rex.eat("meat")