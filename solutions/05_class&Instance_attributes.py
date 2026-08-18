class Dog:
    species="Canis familiaris"
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"{self.name}: {self.species}")
dog1=Dog("Buddy")
dog2=Dog("Max")

dog1.show()
dog2.show()
