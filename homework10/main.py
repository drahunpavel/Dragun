from typing import Dict, Optional, List

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

#Десятичная система счисления основана на числе 10 и использует десять цифр от 0 до 9

class DecimalCounter:
    def __init__(self, init_val: int = 0, min_val: int = 0, max_val:int = 9):
        self._value = init_val
        self._min_val = min_val
        self._max_val = max_val

    def increment(self) -> None:
        if(self._value + 1) <= self._max_val:
            self._value = self._value + 1

    def decrement(self) -> None:
        if(self._value - 1) >= self._min_val:
            self._value = self._value -1

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
print('Found product: ', found_product.name, found_product.price) if found_product else print('Found product: Not found')

new_shop.display_products()