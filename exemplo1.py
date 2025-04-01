

class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fazer_som(self):
        print(f"{self.nome} faz um som.")
        
class Cachorro(Animal):
    def fazer_som(self):
        print(f"{self.nome} late.")
        
class Gato(Animal):
    def fazer_som(self):
        print(f"{self.nome} mia.")
        
class Pato(Animal):
    def fazer_som(self):
        print(f"{self.nome} grasna.")
        
def fazer_som_animal(animal):
    return animal.fazer_som()

rex = Cachorro('Rex', 'Cachorro')
felix = Gato('Felix','Gato')
donald = Pato('Donald','Pato')

animais = [rex, felix, donald]  

for animal in animais:
    print(f"{animal.nome} é um {animal.especie}.")
    fazer_som_animal(animal)


