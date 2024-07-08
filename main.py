import pickle

# Создаем базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

# Создаем подклассы Bird, Mammal, Reptile с переопределением метода make_sound
class Bird(Animal):
    def make_sound(self):
        return "Чирик-чирик"

class Mammal(Animal):
    def make_sound(self):
        return "Рррррр"

class Reptile(Animal):
    def make_sound(self):
        return "Шшшшш"

# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

# Класс Zoo с использованием композиции для хранения животных и сотрудников
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staff.append(staff)

    def save_zoo(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load_zoo(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)

# Классы ZooKeeper и Veterinarian с собственными методами
class ZooKeeper:
    def feed_animal(self, animal):
        return f"{animal.name} кормят"

class Veterinarian:
    def heal_animal(self, animal):
        return f"{animal.name} лечат"

# Демонстрация
bird = Bird("Попугай", 5)
mammal = Mammal("Лев", 10)
reptile = Reptile("Змея", 3)

animals = [bird, mammal, reptile]
animal_sound(animals)

zoo = Zoo()
zoo_keeper = ZooKeeper()
veterinarian = Veterinarian()

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zoo.add_staff(zoo_keeper)
zoo.add_staff(veterinarian)

print(zoo_keeper.feed_animal(bird))
print(veterinarian.heal_animal(mammal))

# Сохранение состояния зоопарка в файл
zoo.save_zoo('zoo.pickle')

# Загрузка состояния зоопарка из файла
zoo_loaded = Zoo.load_zoo('zoo.pickle')
print(zoo_loaded.animals)