'''
Создать класс с двумя переменными. Добавить функцию вывода на экран и функцию изменения этих переменных. 
Добавить функцию, которая находит сумму значений этих переменных, 
и функцию которая находит наибольшее значение из этих двух переменных.
'''

class TwoVariables:
    def __init__(self, var1: int, var2: int):
        self.var1 = var1
        self.var2 = var2

    def display(self) -> None:
        print(f'TwoVariables.display: var1: {self.var1}, var2: {self.var2}')

    def sum(self) -> None:
        print('TwoVariables.sum: ', self.var1 + self.var2)


    def max(self) -> None:
        print('TwoVariables.max: ', max(self.var1, self.var2))

    def modify(self, new_var1: int, new_var2: int) -> None:
        print('TwoVariables.modify: ', new_var1, new_var2)
        self.var1 = new_var1
        self.var2 = new_var2

variables = TwoVariables(3, 14)
variables.display()
variables.sum()
variables.max()

variables.modify(5, 15)
variables.display()
variables.sum()
variables.max()

#----------------------------------------------------------------------------------