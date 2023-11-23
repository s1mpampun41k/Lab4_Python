class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Ручка рисует линии")

class Pencil(Stationery):
    def draw(self):
        print("Карандаш рисует линии")

class Handle(Stationery):
    def draw(self):
        print("Маркер рисует линии")

pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")

pen.draw()
pencil.draw()
handle.draw()
# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод
# выводит сообщение «Запуск отрисовки»; создать три дочерних класса Pen
# (ручка), Pencil (карандаш), Handle (маркер); в каждом классе реализовать
# переопределение метода draw. Для каждого класса метод должен выводить
# уникальное сообщение; создать экземпляры классов и проверить, что
# выведет описанный метод для каждого экземпляра. - 3 балла