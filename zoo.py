
class Animal:
    def __init__(self, name, age, health=0, happiness=0) -> None:
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        print(f"Nombre del animal: {self.name}, edad {self.age}, La salud del animal es: {self.health} y la felicidad es: {self.happiness}")
        return self

    def alimentar(self, comida=True):
        self.health+=10
        self.happiness+=10

class Leon(Animal):
    def __init__(self, name, age=2, health=70, happiness=80, sexo=None):
        super().__init__(name, age, health, happiness)
        self.sexo_animal=sexo
        

    def alimentar(self,comida):
        if comida == 'carne':

            self.health += 5
            self.happiness += 6
        else:
            print("No es el alimento adecuado para este animal")

    def caceria(self, cazar):
        if self.happiness < 10 and cazar == False:
            print(f"La felicidad esta muy baja: {self.happiness}, debe introducir un animal para que el leon lo pueda cazar")
            if cazar == True:
                self.salud+=8
                self.happiness+=10
            else:
                print(f"El Leon puede morir por depresion, debe ejecutar la caceria")
        else:
            print(f"El nivel de felicidad del Leon esta en un minimo aceptable")

class Panda(Animal):
    def __init__(self, name, age=4, health=67, happiness=80, sexo=None):
        super().__init__(name, age, health, happiness)
        self.sexo_animal = sexo
        

    def alimentar(self,comida):
        if comida == 'bambu':
            self.happiness+=4
            self.health+=3
        else:
            print("La comida adecuada para el Panda, es el bambu")
        return self

    def descansar(self, dormir):
        if dormir == True:
            self.happiness+=7
            self.health+=3
        else:
            print("Debe proveer un buen lugar para que el oso pueda descansar")
        return self

class Bird(Animal):

    def __init__(self, name, age=5, health=79, happiness=90):
        super().__init__(name, age, health=health, happiness=happiness)
    
    def alimentar(self, comida):

        if comida=='frutas':
            self.health=15
            self.happiness=12
        else:
            self.health=10
            self.happiness=10
            
        return self

    def jugar(self):
        self.health+=10
        self.happiness+=10
        return self

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name):
        self.animals.append( Leon(name) )
    def add_panda(self, name):
        self.animals.append( Panda(name) )
    def add_bird(self,name):
        self.animals.append( Bird(name))
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("New York Zoo")
zoo1.add_lion("Alex")
zoo1.add_lion("Nala")
zoo1.add_panda("Po")
zoo1.add_panda("Baloo")
zoo1.add_bird("Pepillo")
zoo1.add_bird("Blue")
zoo1.print_all_info()

while True:
    print("Escoja una de las siguientes opciones")
    answer_user = input('1:Add Lion \n2: Add Panda \n3: Add Bird \n 4: Info Animal \n 5: Alimentar Animal \n 0: Exit \n')

    if answer_user == '0':
        break

    elif answer_user == '1':
        
        new_leon = zoo1.add_lion(input('Leon name:'))
        print(f"El  agregado se llama {new_leon}")
    elif answer_user == '2':
        
        new_panda = zoo1.add_panda(input('Panda name:'))
        print(f"El  agregado se llama {new_panda}")
    elif answer_user =='3':
    
        new_bird=zoo1.add_bird(input('Bird name:'))
        print(f"El  agregado se llama {new_bird}")
    elif answer_user=='4':
        for i in range(len(zoo1.animals)):
            print(f"{i+1}: {zoo1.animals[i].name}")
        print("¿De cual animal necesita informacion \n 1: Alex \n 2: Nala \n 3: Po \n 4: Baloo \n 5: PePillo \n 6: Blue \n")
        elegir_animal = input('¿Cual animal?')
        if elegir_animal == '1':
            zoo1.animals[0].display_info()
        elif elegir_animal=='2':
            zoo1.animals[1].display_info()
        elif elegir_animal=='3':
            zoo1.animals[2].display_info()
        elif elegir_animal=='4':
            zoo1.animals[3].display_info()
        elif elegir_animal=='5':
            zoo1.animals[4].display_info()
        elif elegir_animal=='6':
            zoo1.animals[5].display_info()
    elif answer_user == '5':
        print("¿Cual animal desea alimentar?")
        resp_user = input('1:Alimentar Lion \n2: Alimentar Panda \n3: Alimentar Bird \n 0: Exit \n')        
        
        if resp_user =='1':
            zoo1.animals[0].alimentar('carne')
            zoo1.animals[1].alimentar('carne')
            print("Ha alimentado a los leones")
        elif resp_user == '2':
            zoo1.animals[2].alimentar('bambu')
            zoo1.animals[3].alimentar('bambu')
            print("ha alimentado alos panda")
        elif resp_user == '3':
            zoo1.animals[4].alimentar('frutas')
            zoo1.animals[5].alimentar('frutas')
        elif resp_user == '0':
            break
