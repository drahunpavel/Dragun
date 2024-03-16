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
    def __init__(self, color: Chess_Piece_Color, position: Tuple[int, int]):
        super().__init__(color, position)

    def carry_out_attack(self, target_position: Tuple[int, int]) -> bool:
        if self.color == Chess_Piece_Color.WHITE:
            return abs(target_position[0] - self.position[0]) == 1 and target_position[1] - self.position[1] == 1
        else:
            return abs(target_position[0] - self.position[0]) == 1 and target_position[1] - self.position[1] == -1


class Queen(ChessPiece):
    def __init__(self, color: Chess_Piece_Color, position: Tuple[int, int]):
        super().__init__(color, position)

    def carry_out_attack(self, target_position: Tuple[int, int]) -> bool:
        return (target_position[0] == self.position[0] or target_position[1] == self.position[1] or
                abs(target_position[0] - self.position[0]) == abs(target_position[1] - self.position[1]))


class Horse(ChessPiece):
    def __init__(self, color: Chess_Piece_Color, position: Tuple[int, int]):
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
