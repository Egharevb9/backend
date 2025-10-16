class pet:
    def __init__(self, name, species ,age):
        self.name = name
        self.species = species
        self.age = age

    def displayClass(self):
        print(f"name {self.name} species {self.species} age {self.age}")
    def celebrateBirthday(self):
        # if self.age == self.age +1:
        print("Happy Birthday",self.name)

    def displayNewAge(self, new_age):
        if new_age > self.age:
            print("happybirthday", self.name)

dog = pet("bingo", "gemer", 13 )



dog.displayNewAge(14)
        