class Car:
    def __init__(self,brand,year):
        self.brand=brand 
        self.year=year 
    def show(self):
        print(f"Brand:{self.brand} and Year:{self.year}")
car1=Car("Toyota",2020)
car2=Car("Honda", 2019)

car1.show()
car2.show()