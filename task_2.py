from string import ascii_uppercase

class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(f"Буквы алфавита: {' '.join(self.letters)}")

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    letters_num = 26

    def __init__(self):
        super().__init__("EN", list(ascii_uppercase))
        self.__letters_num = 26

    def is_en_letter(self, let):
        if let.upper() in self.letters:
            print(f"Буква {let} есть в алфавите")
        else:
            print(f"Буквы {let} нет в алфавите")
            return

    @staticmethod
    def example():
        return "This an example text in English"

def main():
    while True:
        print("Выберите один из вариантов:\n"
              "1. Просмотр класса родителя\n"
              "2. Просмотр дочерний класс")
        while True:
            try:
                n = int(input())
                if n != 1 and n != 2:
                    raise Exception
                break
            except ValueError:
                print("Вы ввели не число. Введите ещё раз")
            except Exception:
                print("Ввести можно только 1 или 2")
        if n == 1:
            while True:
                try:
                    lang = input("Введите язык: 'EN' или 'RUS':")
                    for i in lang:
                        if i.isdigit():
                            raise Exception
                    break
                except Exception:
                    print("Название языка не может включать цифры")

            while True:
                try:
                    letters = input("Введите буквы алфавита через пробел").split()
                    for i in letters:
                        if i.isdigit():
                            raise Exception("Алфавит не может включать цифры")
                        if len(i) != 1:
                            raise Exception("Длинна буквы не может быть больше 1 символа")
                    break
                except Exception as e:
                    print(e)

            alpha = Alphabet(lang, letters)
            while True:
                print("Меню методов родительского класса:\n"
                      "1. Вывод букв алфавита\n"
                      "2. Вывод длинны алфавита\n"
                      "Другое -  выход в меню")
                while True:
                    try:
                        m = int(input("Введите номер метода:"))
                        break
                    except ValueError:
                        print("Вы ввели не цифру, попробуйте ещё раз")
                if m == 1:
                    alpha.print()
                elif m == 2:
                    print(f"Размер алфавита равен: {alpha.letters_num()}")
                else:
                    break
        else:
            eng = EngAlphabet()

            while True:
                print("Меню методов дочернего класса:\n"
                      "1. Проверка отношения введённой буквы к алфавиту\n"
                      "2. Вывод длинны алфавита\n"
                      "3. Вывод предложения на английском языке\n"
                      "Другое - выход в главное меню")
                while True:
                    try:
                        m = int(input("Введите номер метода:"))
                        break
                    except ValueError:
                        print("Вы ввели не цифру, попробуйте ещё раз")
                if m == 1:
                    while True:
                        try:
                            letter = input("Введите одну букву английского алфавита:")
                            if letter.isdigit():
                                raise ValueError("Введите букву: ")
                            if len(letter) != 1:
                                raise ValueError("Только 1")
                            break
                        except ValueError as e:
                            print(e)
                    eng.is_en_letter(letter)
                    print()
                elif m == 2:
                    print(f"Размер алфавита равен: {eng.letters_num}")
                elif m == 3:
                    print("Вывод предложения на русском языке: ")
                    print(EngAlphabet.example())
                else:
                    break




if __name__ == "__main__":
    main()


# Задание 2:
# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены два
# динамических свойства: 1) lang - язык и 2) letters - список букв. Начальные
# значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите
# Класс EngAlphabet
# 1. Создайте класс EngAlphabet путем наследования от класса Alphabet
# 2. Создайте метод __init__(), внутри которого будет вызываться
# родительский метод __init__(). В качестве параметров ему будут
# передаваться обозначение языка(например, 'En') и строка, состоящая из всех
# букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля
# string).
# 3. Добавьте приватное статическое свойство __letters_num, которое будет
# хранить количество букв в алфавите.
# 4. Создайте метод is_en_letter(), который будет принимать букву в качестве
# параметра и определять, относится ли эта буква к английскому алфавиту.
# 5. Переопределите метод letters_num() - пусть в текущем классе классе он
# будет возвращать значение свойства __letters_num.
# 6. Создайте статический метод example(), который будет возвращать пример
# текста на английском языке. – 3 балла