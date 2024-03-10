from typing import Optional, List

'''
Создать класс с двумя переменными. Добавить функцию вывода на экран и функцию изменения этих переменных. 
Добавить функцию, которая находит сумму значений этих переменных, 
и функцию которая находит наибольшее значение из этих двух переменных.
'''


class TwoVariables:
    def __init__(self, var1: int, var2: int):
        self._var1 = var1
        self._var2 = var2

    def display(self) -> None:
        print(f'TwoVariables.display: var1: {self._var1}, var2: {self._var2}')

    def sum(self) -> None:
        print('TwoVariables.sum: ', self._var1 + self._var2)

    def max(self) -> None:
        print('TwoVariables.max: ', max(self._var1, self._var2))

    def modify(self, new_var1: int, new_var2: int) -> None:
        print('TwoVariables.modify: ', new_var1, new_var2)
        self._var1 = new_var1
        self._var2 = new_var2


variables = TwoVariables(3, 14)
variables.display()
variables.sum()
variables.max()

variables.modify(5, 15)
variables.display()
variables.sum()
variables.max()

print('-------------------------------------------------')

'''
Описать класс, реализующий десятичный счетчик, который может увеличивать или уменьшать свое значение на единицу в заданном диапазоне. 
Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями. 
Счетчик имеет два метода: увеличения и уменьшения, — и свойство, позволяющее получить его текущее состояние. 
Написать программу, демонстрирующую все возможности класса.
'''

# Десятичная система счисления основана на числе 10 и использует десять цифр от 0 до 9


class DecimalCounter:
    def __init__(self, init_val: int = 0, min_val: int = 0, max_val: int = 9):
        self._value = init_val
        self._min_val = min_val
        self._max_val = max_val

    def increment(self) -> None:
        if (self._value + 1) <= self._max_val:
            self._value = self._value + 1

    def decrement(self) -> None:
        if (self._value - 1) >= self._min_val:
            self._value = self._value - 1

    @property
    def value(self) -> int:
        return self._value


counter = DecimalCounter()


counter.increment()
print('counter.value: ', counter.value)

counter2 = DecimalCounter(init_val=5, min_val=3, max_val=6)
counter2.increment()
counter2.increment()
counter2.decrement()
print('counter2.value: ', counter2.value)

print('-------------------------------------------------')

'''
Реализуйте класс Shop. Предусмотреть возможность работы с произвольным числом продуктов, 
поиска продуктов по названию, добавления их в магазин и удаления продуктов из него.
'''


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class Shop:
    def __init__(self):
        self._products: List[Product] = []

    def add_product(self, product: Product) -> None:
        print('Shop.add_product: ', product.price, product.name)
        self._products.append(product)

    def find_product(self, product_name: str) -> Optional[Product]:
        for product in self._products:
            if product.name == product_name:
                return product
        return None

    def remove_product(self, product_name: str) -> None:
        product = self.find_product(product_name)
        if product:
            self._products.remove(product)

    def display_products(self) -> None:
        if not self._products:
            print("The shop is empty")
        else:
            print("Products in the shop: ")
            for product in self._products:
                print(f"Name: {product.name}, Price: {product.price}")


new_shop = Shop()

new_product1 = Product('Apple', 1.5)
new_product2 = Product('Potato', 0.5)
new_product3 = Product('Pineapple', 4.5)


new_shop.add_product(new_product1)
new_shop.add_product(new_product2)
new_shop.add_product(new_product3)

new_shop.remove_product('Potato')

found_product = new_shop.find_product('Apple')
print('Found product: ', found_product.name,
      found_product.price) if found_product else print('Found product: Not found')

new_shop.display_products()

print('-------------------------------------------------')


'''
Реализуйте класс MoneyBox, для работы с виртуальной копилкой. Каждая копилка имеет ограниченную вместимость, 
которая выражается целым числом – количеством монет(capacity -вместимость), которые можно положить в копилку. 
Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность добавлять монеты в копилку и узнавать, 
можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость. 
Класс должен иметь следующий вид:
class MoneyBox: 
    def__init__(self, capacity) :
    #конструктор с аргументом- вместимость копилки 
    def can_add(self,v)
    #True, если можно добавить v монет, False иначе
    def add(self,v)
    #положить v монет в копилку

При создании копилки, число монет в ней равно 0.
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.
'''


class MoneyBox:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._coins = 0

    def can_add(self, coins: int) -> bool:
        return self._coins + coins <= self._capacity

    def add(self, coins: int) -> None:
        if self.can_add(coins):
            self._coins += coins
            print(
                f'MoneyBox.add: Added {coins} to MoneyBox. Total coins: {self._coins}')
        else:
            print('MoneyBox.add: Cannot add more coins')


money_box = MoneyBox(100)

money_box.add(70)
print(money_box.can_add(70))
print(money_box.can_add(20))
money_box.add(70)
money_box.add(20)

print('-------------------------------------------------')

'''
Создайте класс fraction. Данные класса должны быть представлены двумя полями: числителем и знаменателем. 
Методы класса должны получать от пользователя значения числителя и знаменателя дроби и выводить значение дроби в форме 3/5. 
Кроме того, должен быть разработан метод, складывающий значения двух дробей и метод для сокращения дробей.
'''


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self._numerator = numerator
        self._denominator = denominator

    def display(self) -> None:
        print(f'Fraction.display: {self._numerator}/{self._denominator}')

    def add(self, fraction: 'Fraction') -> 'Fraction':
        new_numerator = self._numerator * fraction._denominator + \
            fraction._numerator * self._denominator
        new_denominator = self._denominator * fraction._denominator

        result_fraction = Fraction(new_numerator, new_denominator)
        print('--Before reduce: ')
        result_fraction.display()
        result_fraction.reduce()
        print('--After reduce: ')
        result_fraction.display()
        return result_fraction

    def reduce(self) -> None:
        denominator = self.grt_cmmn_denominator(
            self._numerator, self._denominator)

        self._numerator //= denominator
        self._denominator //= denominator

    def grt_cmmn_denominator(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a


fraction1 = Fraction(3, 4)
fraction1.display()

fraction2 = Fraction(1, 4)
fraction2.display()

fractions_sum = fraction1.add(fraction2)
print('--fractions sum: ')
fractions_sum.display()
print('-------------------------------------------------')
