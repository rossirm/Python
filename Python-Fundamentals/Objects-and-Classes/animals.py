class Dog:
    def __init__(self, name, age, number_of_legs):
        self.name = name
        self.age = age
        self.number_of_legs = number_of_legs
        self.sound = 'I\'m a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.'
        self.info = f'Dog: {self.name}, Age: {self.age}, Number Of Legs: {self.number_of_legs}'

    def produce_sound(self):
        return self.sound

    def get_info(self):
        return self.info


class Cat:
    def __init__(self, name, age, intelligence_quotient):
        self.name = name
        self.age = age
        self.intelligence_quotient = intelligence_quotient
        self.sound = 'I\'m an Aristocat, and I will now produce an aristocratic sound! Myau Myau.'
        self.info = f'Cat: {self.name}, Age: {self.age}, IQ: {self.intelligence_quotient}'

    def produce_sound(self):
        return self.sound

    def get_info(self):
        return self.info


class Snake:
    def __init__(self, name, age, cruelty_coefficient):
        self.name = name
        self.age = age
        self.cruelty_coefficient = cruelty_coefficient
        self.sound = 'I\'m a Sophistisnake, and I will now produce a sophisticated sound! Honey, I\'m home.'
        self.info = f'Snake: {self.name}, Age: {self.age}, Cruelty: {self.cruelty_coefficient}'

    def produce_sound(self):
        return self.sound

    def get_info(self):
        return self.info


animals = {'dogs': {}, 'cats': {}, 'snakes': {}}
line = input()
while line != 'I\'m your Huckleberry':
    first_command, other = line.split(' ', 1)
    if first_command == 'talk':
        talk, some_name = line.split(' ')
        for species, animal in animals.items():
            for current_name, current_animal in animal.items():
                if current_name == some_name:
                    print(current_animal.produce_sound())
        line = input()
    else:
        class_name, animal_name, animal_age, animal_parameter = line.split(' ')
        if class_name == 'Dog':
            animals['dogs'].update({animal_name: Dog(animal_name, animal_age, animal_parameter)})
        elif class_name == 'Cat':
            animals['cats'].update({animal_name: Cat(animal_name, animal_age, animal_parameter)})
        elif class_name == 'Snake':
            animals['snakes'].update({animal_name: Snake(animal_name, animal_age, animal_parameter)})
        line = input()

for s, animal in animals.items():
    for current_name, current_animal in animal.items():
            print(current_animal.get_info())
