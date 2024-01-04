class Fish:

    def __init__(self, x, y):
        self.x = x
        self.y = y


# méthode qui affiche "1" pour indiquer le type de mon instance de poisson
    def type_code(self):
        return "1"
    pass

fish_1 = Fish(1, 1)

print(fish_1)

# print(isinstance(fish_1, Fish))

# print(dir(fish_1))

# print(fish_1.x)

#permet de lister les attributs de mon instance de Fish, ici fish_1
print(fish_1.__dict__)

print(fish_1)

# affiche la méthode
print(fish_1.type_code())
