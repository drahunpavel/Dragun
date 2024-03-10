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

print('-------------------------------------------------')

counter.increment()
print('counter.value: ', counter.value)

counter2 = DecimalCounter(init_val=5, min_val=3, max_val=6) 
counter2.increment()
counter2.increment()
counter2.decrement()
print('counter2.value: ', counter2.value)