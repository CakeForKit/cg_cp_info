folder = 'data/'
fn_pawn = folder + 'pawn.txt'
fn_rook = folder + 'rook.txt'
fn_bishop = folder + 'bishop.txt'
fn_queen = folder + 'queen.txt'
fn_king = folder + 'king.txt'
fn_knight = folder + 'knight.txt'
folder_board = folder + 'chessboard/'
fn_white_chessboard = folder_board + 'white_cells_chessboard.txt'
fn_black_chessboard = folder_board + 'black_cells_chessboard.txt'
fn_base_chessboard = folder_board + 'base_chessboard.txt'
fn_data_chessborad = folder_board + 'positions_cells.txt'

def create_file(rs):
    text = 'c 0 0 0\n'

    for i in range(len(rs)):
        r = rs[i]
        text += f'r {r[0]} {r[1]} \t\t\t# {i + 1}\n'
    text += '\n'

    for i in range(len(rs) - 1):
        text += f'l r{i+1} r{i+2}\n'

    return text