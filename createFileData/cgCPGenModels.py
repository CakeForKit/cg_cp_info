import math
from chessboard import chessboard
from pawn import pawn
from rook import rook
from knight import knight
from bishop import bishop
from queen import queen
from king import king

gRatio = 0.618
gRatio_ = 1 - gRatio

if __name__ == '__main__':
    # alpha = 20
    # r = 15.45 # h * gRatio / 2  # 0.309 * h -> 15.45
    # delta_r = 0.55
    # board_plus, height_chessboard = (r + delta_r), int(r + delta_r) * 2

    pawn_h = 50
    rook_h = 55
    knight_h = 60
    bishop_h = 70
    queen_h = 85
    king_h = 95
    width_cell = pawn_h
    board_plus = width_cell // 2
    height_chessboard = width_cell

    chessboard(width_cell, board_plus, height_chessboard)
    pawn(pawn_h)
    rook(rook_h)
    knight(knight_h)
    bishop(bishop_h)
    queen(queen_h)
    king(king_h)


