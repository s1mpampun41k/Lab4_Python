class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def my_sum(self):
        return self.a + self.b

    def difference(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def division(self):
        if self.b == 0:
            print("Нельзя делить на ноль!")
        return self.a / self.b


def input_data():
    while True:
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            break
        except ValueError:
            print("Введите число")
    return a, b


def main():
    x, y = input_data()
    calculator = Calculator(x, y)
    print(f"Сумма: {calculator.my_sum()}")
    print(f"Разность: {calculator.difference()}")
    print(f"Произведение: {calculator.multiply()}")
    print(f"Деление: {calculator.division()}")


if __name__ == "__main__":
    main()

# Задание 1:
# Калькулятор.
# Создайте класс, где реализованы функции(методы) математических
# операций. А также функция, для ввода данных. – 1 балл
