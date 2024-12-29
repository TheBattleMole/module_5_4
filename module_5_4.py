class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)


    def __init__(self, name, number_of_floors):
        self.name = name
        self.floors = number_of_floors

    def __del__(self):
        return print(f"{self.name} cнесен, но он останется в истории")

h1 = House("Бурдж-Халифа", 163)
print(House.houses_history)
h2 = House("Хрущевка", 5)
print(House.houses_history)
h3 = House("Бунгало", 1)
print(House.houses_history)
del h2
del h3
print(House.houses_history)