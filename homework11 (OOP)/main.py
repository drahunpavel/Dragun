'''
Определить класс «Шахматная фигура» с ее координатами на шахматной доске, 
ее цветом (черный или белый), виртуальным методом «битья» другой фигуры, 
и унаследовать от него классы, соответствующие шахматным фигурам «Ферзь», «Пешка», «Конь». 
Написать виртуальные методы «битья» другой фигуры, которые принимают координаты другой фигуры и определяют, может ли данная  фигура «бить» фигуру с теми (принятыми) координатами.
'''

from enum import Enum
from typing import Tuple

# x: a-h(1-8)
# y: 1-8

# белые снизу
# черные сверху


class Chess_Piece_Color(Enum):
    BLACK = 'black'
    WHITE = 'white'


class ChessPiece:
    def __init__(self, color: Chess_Piece_Color, position: Tuple[int, int]) -> None:
        self.color = color
        self.position = position

    def carry_out_attack(self) -> None:
        raise NotImplementedError(
            f"Subclass {self.__class__.__name__} must call the abstract method carry_out_attack")


class Pawn(ChessPiece):
    def __init__(self, color: Chess_Piece_Color, position: Tuple[int, int]) -> None:
        super().__init__(color, position)

    def carry_out_attack(self, target_position: Tuple[int, int]) -> bool:
        if self.color == Chess_Piece_Color.WHITE:
            return abs(target_position[0] - self.position[0]) == 1 and target_position[1] - self.position[1] == 1
        else:
            return abs(target_position[0] - self.position[0]) == 1 and target_position[1] - self.position[1] == -1


class Queen(ChessPiece):
    def __init__(self, color: Chess_Piece_Color, position: Tuple[int, int]) -> None:
        super().__init__(color, position)

    def carry_out_attack(self, target_position: Tuple[int, int]) -> bool:
        return (target_position[0] == self.position[0] or target_position[1] == self.position[1] or
                abs(target_position[0] - self.position[0]) == abs(target_position[1] - self.position[1]))


class Horse(ChessPiece):
    def __init__(self, color: Chess_Piece_Color, position: Tuple[int, int]) -> None:
        super().__init__(color, position)

    def carry_out_attack(self, target_position: Tuple[int, int]) -> bool:
        row_diff = abs(target_position[0] - self.position[0])
        col_diff = abs(target_position[1] - self.position[1])
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)


pawn_wh_at = Pawn(Chess_Piece_Color.WHITE, (2, 2))
pawn_wh_def = Pawn(Chess_Piece_Color.WHITE, (8, 8))
pawn_bl_def_1 = Pawn(Chess_Piece_Color.BLACK, (3, 3))
pawn_bl_def_2 = Pawn(Chess_Piece_Color.BLACK, (3, 1))

queen_1 = Queen(Chess_Piece_Color.BLACK, (8, 1))
queen_2 = Queen(Chess_Piece_Color.BLACK, (4, 5))

horse_1 = Horse(Chess_Piece_Color.WHITE, (2, 1))
horse_2 = Horse(Chess_Piece_Color.WHITE, (3, 1))

print(pawn_wh_at.carry_out_attack(pawn_bl_def_1.position))  # true
print(pawn_wh_at.carry_out_attack(pawn_bl_def_2.position))  # false
print(horse_1.carry_out_attack(pawn_bl_def_1.position))  # true
print(horse_2.carry_out_attack(pawn_bl_def_1.position))  # false
print(queen_1.carry_out_attack(pawn_wh_def.position))  # true
print(queen_2.carry_out_attack(pawn_wh_def.position))  # false

print('-------------------------------------------------')

'''
Создать класс «Живое». Определить наследуемые классы – «лиса», «кролик» и «растение». 
Лиса ест кролика. Кролик ест растения. Растение поглощает солнечный свет. 
Представитель каждого класса может умереть, если достигнет определенного возраста или для него не будет еды. 
Напишите виртуальные методы поедания и определения состояния живого существа (живой или нет, в зависимости от достижения предельного возраста и наличия еды (входной параметр)).
'''


class Living:
    def __init__(self, max_age: int) -> None:
        self.age: int = 0
        self.max_age = max_age
        self.is_alive: bool = True

    def eat(self) -> None:
        raise NotImplementedError(
            f"Subclass {self.__class__.__name__} must call the abstract method eat")

    def check_survivability(self) -> bool:
        self.age += 1
        if self.age >= self.max_age:
            self.is_alive = False
            print(f"{self.__class__.__name__} died of passion")
            return False
        else:
            print(f"{self.__class__.__name__} is alive")
            return True


class Fox(Living):
    def __init__(self, max_age: int) -> None:
        super().__init__(max_age)

    def eat(self) -> None:
        print("Fox eats Rabbit")

    def check_survivability(self, have_food: bool) -> None:
        if super().check_survivability() and not have_food:
            self.is_alive = False
            print(f"{self.__class__.__name__} died of starvation")
            return False

        return True


class Rabbit(Living):
    def __init__(self, max_age: int) -> None:
        super().__init__(max_age)

    def eat(self) -> None:
        print("Rabbit eats Plant")

    def check_survivability(self, have_food: bool) -> None:
        if super().check_survivability() and not have_food:
            self.is_alive = False
            print(f"{self.__class__.__name__} died of starvation")
            return False

        return True


class Plant(Living):
    def __init__(self, max_age: int) -> None:
        super().__init__(max_age)

    def eat(self) -> None:
        print("Plant absorbs sunlight")

    def check_survivability(self, have_food: bool) -> bool:
        if super().check_survivability() and not have_food:
            self.is_alive = False
            print(f"{self.__class__.__name__} died of starvation")
            return False

        return True


plant = Plant(max_age=500)
rabbit = Rabbit(max_age=10)
fox = Fox(max_age=15)


# Предпогалаем, что идут годы...
years: int = 0

plant.eat()
rabbit.eat()
fox.eat()
print('------')
while years < 15:
    plant.check_survivability(have_food=True)
    rabbit.check_survivability(have_food=plant.is_alive)
    fox.check_survivability(have_food=rabbit.is_alive)

    print('------')
    years += 1

print('-------------------------------------------------')

'''
Создать базовый класс «Грузоперевозчик» и производные классы «Самолет», «Поезд», «Автомобиль». 
Определить время и стоимость перевозки для указанных городов и расстояний


Разработайте программу, имитирующую работу транспортного агентства. Транспортное агентство имеет сеть филиалов в нескольких городах. 
Транспортировка грузов осуществляется между этими городами тремя видами транспорта: автомобильным, железнодорожным и воздушным. 

Любой вид транспортировки имеет стоимость единицы веса на единицу пути и скорость доставки. 
Воздушный транспорт можно использовать только между крупными городами, этот вид самый скоростной и самый дорогой.  
Железнодорожный транспорт можно использовать между крупными и средними городами, этот вид самый дешевый. Автомобильный транспорт можно использовать между любыми городами. 
Заказчики через случайные промежутки времени обращаются в один из филиалов транспортного агентства с заказом на перевозку определенной массы груза и возможным пожеланием о скорости/цене доставки. 
Транспортное агентство организует отправку грузов одним из видов транспорта с учетом пожеланий клиента.
 -Доход транспортного агентства, в том числе с разбивкой по видам транспорта и городам.
 -Среднее время доставки груза, в том числе с разбивкой по видам транспорта и городам.
 -Список исполняемых заказов с возможность сортировки по городам, видам транспорта, стоимости перевозки.
'''

'''
1. время перевозки
2. стоимость перевозки
3. 
'''

from typing import List, Union, Dict
import random

class Transport_Types(Enum):
    Plane = 'Plane'
    Train = 'Train'
    Truck = 'Truck'

class City_Size_Types(Enum):
    Large = 'Large'
    Medium = 'Medium'
    Small = 'Small'

class Preference_Types(Enum):
    Speed = 'Speed'
    Cost = 'Cost'

branches_dict = {
    "Moscow": {"size": City_Size_Types.Large.value},
    "New York": {"size": City_Size_Types.Large.value},
    "Tokyo": {"size": City_Size_Types.Large.value},
    "London": {"size": City_Size_Types.Medium.value},
    "Paris": {"size": City_Size_Types.Medium.value},
    "Berlin": {"size": City_Size_Types.Medium.value},
    "Beijing": {"size": City_Size_Types.Medium.value},
    "Los Angeles": {"size": City_Size_Types.Small.value},
    "Chicago": {"size": City_Size_Types.Small.value},
    "Toronto": {"size": City_Size_Types.Small.value}
}

class Transport:
    def __init__(self, name: Transport_Types, cost_per_weight_per_distance: int, speed: int) -> None:
        self.name = name
        self.cost_per_weight_per_distance = cost_per_weight_per_distance
        self.speed = speed

class Branch:
    def __init__(self, city: str, city_size: City_Size_Types, transports: List[Transport]) -> None:
        self.city = city
        self.transports = self._get_trasnport(city_size, transports)
        self.income = {city: {Transport_Types.Plane.value: 0, Transport_Types.Train.value: 0, Transport_Types.Truck.value: 0}}
        self.average_time = {city: {Transport_Types.Plane.value: 0, Transport_Types.Train.value: 0, Transport_Types.Truck.value: 0}}


    def calculate_income(self, city: str, transport: City_Size_Types, income: int):
        self.income[city][transport] = self.income[city][transport] + income

    def calculate_average_time(self, city: str, transport: City_Size_Types, average_time: int):
        if(self.average_time[city][transport] == 0):
            self.average_time[city][transport] = average_time
        else:
            self.average_time[city][transport] = (self.average_time[city][transport] + average_time)/2


    def _get_trasnport(self, city_size: City_Size_Types, transports: List[Transport]) -> List[Transport]:
        if city_size == City_Size_Types.Small.value:
            return [transport for transport in list(transports) if transport.name == Transport_Types.Truck.value]
        
        if city_size == City_Size_Types.Medium.value:
            return [transport for transport in list(transports) if transport.name != Transport_Types.Plane.value]

        return transports

class Order:
    def __init__(self, weight: int, from_city: str, to_city: str, distance: int, preference: Preference_Types) -> None:
        self.weight = weight #тон
        self.from_city = from_city
        self.to_city = to_city
        self.distance = distance
        self.preference = preference 

class LogisticsCenter:
    def __init__(self, branches: List[Branch], transports: List[Transport]) -> None:
        self.branches = branches
        self.transports = transports
        self.orders: List[Order] = []
        self.tamp_list: List[Dict[str, Union[str, int]]] = []

    def receive_order(self, order: Order) -> None:
        self.orders.append(order)

    def show_orders(self) -> None:
        print('-----show orders:')
        for order in self.orders:
            print(f'from: {order.from_city}, to: {order.to_city}, weight: {order.weight}, distance: {order.distance}, preference: {order.preference}')

    def show_income(self) -> None:
        print(' ')
        print('-----SHOW INCOME: ')
        print(' ')
        total: int = 0
        for branch in self.branches:
            for city, transport_dict in branch.income.items():
                print(f'city: {city} : {transport_dict}')
                for transport, income in transport_dict.items():
                    total += income
        print(' ')
        print(f'-----SHOW INCOME: TOTAL: {total}')
        print(' ')

    def show_average_time(self) -> None:
        print(' ')
        print('-----SHOW AVERAGE TIME: ')
        print(' ')
        transport_counts = {'Plane': 0, 'Train': 0, 'Truck': 0} 
        transport_occurrences = {'Plane': 0, 'Train': 0, 'Truck': 0} 

        for branch in self.branches:
            for city, transport_dict in branch.average_time.items():
                print(f'city: {city} : {transport_dict}')
                for transport, time in transport_dict.items():
                    transport_counts[transport] += time
                    transport_occurrences[transport] += 1

        print(' ')
        for transport, total_time in transport_counts.items():
            if transport_occurrences[transport] != 0:
                average_time = total_time / transport_occurrences[transport]
                print(f'{transport}: average_time: {average_time}')

    def sort_tamp_list_by_id(self, sort_key: str):
        if sort_key in ['from_city', 'to_city', 'transport', 'cost', 'delivery_time']:
            self.tamp_list.sort(key=lambda x: x[sort_key])
        
    def show_sorted_list(self) -> None:
        print('-----show sorted list:')
        for item in self.tamp_list:
            print(item)

    def process_orders(self) -> None:
        print('-----PROCESS ORDERS: ')
        print('')
        for order in self.orders:
            branch = self.__find_branch(order.from_city)
            transport = self._find_transport(order.from_city, order.to_city, order.preference)
            if branch and transport:
                cost = self._calculate_cost_transportation(order.weight, order.distance, transport.cost_per_weight_per_distance)
                delivery_time = order.distance / transport.speed
                branch.calculate_income(order.from_city, transport.name, cost)
                branch.calculate_average_time(order.from_city, transport.name, int(delivery_time))
                self.tamp_list.append({'from_city': order.from_city, 'to_city': order.to_city, 'cost': cost, 'delivery_time': int(delivery_time), 'transport': transport.name})
                print(f'from: {order.from_city}, to: {order.to_city}, cost: {cost}, delivery time: {int(delivery_time)}, by: {transport.name}')

    def _calculate_cost_transportation(self, weight: int, distance: int, cost_per_weight_per_distance: int) -> int:
        return weight * distance * cost_per_weight_per_distance

    def __find_branch(self, city: str) -> Union[Branch, None]:
        branch_by_city = {branch.city: branch for branch in self.branches}
        return branch_by_city.get(city)

    def _find_transport(self, from_city: str, to_city: str, order: Preference_Types) -> Union[Transport, None]:

        found_from_branch = self.__find_branch(from_city)
        found_to_branch = self.__find_branch(to_city)

        if not found_from_branch or not found_to_branch:
            return None

        # множества для уникальных значений
        transports_from_set = set(found_from_branch.transports)
        transports_to_set = set(found_to_branch.transports)
 
        accessible_transport = transports_from_set.intersection(transports_to_set)
        list(accessible_transport)

        if order == Preference_Types.Speed.value:
            found_plane = [transport for transport in list(accessible_transport) if transport.name == Transport_Types.Plane.value]
            if(found_plane):
                return found_plane[0]
            
            found_truck = [transport for transport in list(accessible_transport) if transport.name == Transport_Types.Truck.value]
            if(found_truck):
                return found_truck[0]
            
            return None
        else:
            found_train = [transport for transport in list(accessible_transport) if transport.name == Transport_Types.Train.value]
            if(found_train):
                return found_train[0]
            
            found_truck = [transport for transport in list(accessible_transport) if transport.name == Transport_Types.Truck.value]
            if(found_truck):
                return found_truck[0]
            
            return None


def get_random_km() -> int:
    return random.randint(500, 10000)

# transports
transport_train = Transport(name=Transport_Types.Train.value, cost_per_weight_per_distance=1, speed=90)
transport_truck = Transport(name=Transport_Types.Truck.value, cost_per_weight_per_distance=2, speed=80)
transport_plane = Transport(name=Transport_Types.Plane.value, cost_per_weight_per_distance=10, speed=700)
transport_list = [transport_train, transport_truck, transport_plane]


# branches
branch_moscow = Branch(city='Moscow', city_size=branches_dict.get('Moscow')['size'], transports=transport_list)
branch_new_york = Branch(city='New York', city_size=branches_dict.get('New York')['size'], transports=transport_list)
branch_tokyo = Branch(city='Tokyo', city_size=branches_dict.get('Tokyo')['size'], transports=transport_list)
branch_london = Branch(city='London', city_size=branches_dict.get('London')['size'], transports=transport_list)
branch_paris = Branch(city='Paris', city_size=branches_dict.get('Paris')['size'], transports=transport_list)
branch_berlin = Branch(city='Berlin', city_size=branches_dict.get('Berlin')['size'], transports=transport_list)
branch_beijing = Branch(city='Beijing', city_size=branches_dict.get('Beijing')['size'], transports=transport_list)
branch_los_angeles = Branch(city='Los Angeles', city_size=branches_dict.get('Los Angeles')['size'], transports=transport_list)
branch_chicago = Branch(city='Chicago', city_size=branches_dict.get('Chicago')['size'], transports=transport_list)
branch_toronto = Branch(city='Toronto', city_size=branches_dict.get('Toronto')['size'], transports=transport_list)

# orders
order_1 = Order(weight=100, from_city='Moscow', to_city='New York', distance=get_random_km(), preference=Preference_Types.Speed.value)
order_2 = Order(weight=200, from_city='Tokyo', to_city='London', distance=get_random_km(), preference=Preference_Types.Cost.value)
order_3 = Order(weight=15, from_city='Paris', to_city='Berlin', distance=get_random_km(), preference=Preference_Types.Speed.value)
order_4 = Order(weight=60, from_city='Beijing', to_city='Los Angeles', distance=get_random_km(), preference=Preference_Types.Cost.value)
order_5 = Order(weight=90, from_city='Chicago', to_city='Toronto', distance=get_random_km(), preference=Preference_Types.Speed.value)
order_6 = Order(weight=45, from_city='Berlin', to_city='Paris', distance=get_random_km(), preference=Preference_Types.Cost.value)
order_7 = Order(weight=37, from_city='Beijing', to_city='London', distance=get_random_km(), preference=Preference_Types.Speed.value)
order_8 = Order(weight=44, from_city='Los Angeles', to_city='Tokyo', distance=get_random_km(), preference=Preference_Types.Cost.value)
order_9 = Order(weight=55, from_city='Moscow', to_city='New York', distance=get_random_km(), preference=Preference_Types.Speed.value)
order_10 = Order(weight=26, from_city='Moscow', to_city='New York', distance=get_random_km(), preference=Preference_Types.Cost.value)

logisticsCenter = LogisticsCenter(branches=[branch_moscow, branch_new_york, branch_tokyo, branch_london, branch_paris, 
                                            branch_berlin, branch_beijing, branch_los_angeles, branch_chicago, branch_toronto], 
                                            transports=transport_list)

logisticsCenter.receive_order(order_1)
logisticsCenter.receive_order(order_2)
logisticsCenter.receive_order(order_3)
logisticsCenter.receive_order(order_4)
logisticsCenter.receive_order(order_5)
logisticsCenter.receive_order(order_6)
logisticsCenter.receive_order(order_7)
logisticsCenter.receive_order(order_8)
logisticsCenter.receive_order(order_9)
logisticsCenter.receive_order(order_10)

# logisticsCenter.show_orders()

logisticsCenter.process_orders()
logisticsCenter.show_income()
logisticsCenter.show_average_time()
print('before sort: ')
logisticsCenter.show_sorted_list()
logisticsCenter.sort_tamp_list_by_id('cost')
print('after sort: ')
logisticsCenter.show_sorted_list()