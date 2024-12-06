import math
from createFile import *


'''
width_cell - ширина клетки (два диаметра основания пешки)
board_plus - отступ деревянной части шахматной доски от чб ячеек
width - высота шахматной доски
'''
def chessboard(width_cell, board_plus, height_chessboard):
    points = []
    basep, basev = [], []
    whitep, whitev = [], []
    blackp, blackv = [], []
    i = 0
    # for x in range(-4 * width_cell, 5 * width_cell, width_cell):
        # for z in range(-4 * width_cell, 5 * width_cell, width_cell):
    x = -4 * width_cell
    while x < 5 * width_cell:
        z = -4 * width_cell
        while z < 5 * width_cell:
            points.append((x, 0, z))
            # print(f'{i}: ', (x, 0, z), f'\t({i // 9}, {i % 9})')
            i += 1

            z += width_cell
        x += width_cell

    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0: # white
                whitep.append(points[i * 9 + j])
                whitep.append(points[i * 9 + (j + 1)])
                whitep.append(points[(i + 1) * 9 + (j + 1)])
                whitep.append(points[(i + 1) * 9 + j])
                n = len(whitep)
                whitev.append((n - 4, n - 3, n - 2))
                whitev.append((n - 4, n - 1, n - 2))
                # print(f'[{i}, {j}]', whitep[-4:])
            else:
                blackp.append(points[i * 9 + j])
                blackp.append(points[i * 9 + (j + 1)])
                blackp.append(points[(i + 1) * 9 + (j + 1)])
                blackp.append(points[(i + 1) * 9 + j])
                n = len(blackp)
                blackv.append((n - 4, n - 3, n - 2))
                blackv.append((n - 4, n - 1, n - 2))

    def plus_board(pts):
        x = pts[0] + (board_plus if pts[0] > 0 else -board_plus)
        y = pts[1]
        z = pts[2] + (board_plus if pts[2] > 0 else -board_plus)
        return (x, y, z)

    def minus_y(pts):
        x = pts[0]
        y = pts[1] - height_chessboard
        z = pts[2]
        return (x, y, z)

    basep.extend(
                [points[0], points[8], points[80], points[72], # 0 1 2 3
                plus_board(points[0]),      # 4
                plus_board(points[8]),      # 5
                plus_board(points[80]),     # 6
                plus_board(points[72]),     # 7
                minus_y(plus_board(points[0])),     # 8
                minus_y(plus_board(points[8])),     # 9
                minus_y(plus_board(points[80])),    # 10
                minus_y(plus_board(points[72])),    # 11
               ]
    )
    basev.extend([(0, 4, 5), (0, 5, 1), (1, 5, 6), (1, 6, 2),
                  (2, 6, 7), (2, 7, 3), (3, 7, 4), (0, 4, 3),
                  (8, 9, 10), (8, 10, 11),
                  (8, 4, 5), (8, 9, 5), (9, 5, 6), (9, 10, 6),
                  (10, 6, 7), (10, 11, 7), (11, 7, 4), (11, 8, 6)])

    def write_data_to_file(f, text_name):
        f.write(text_name)
        f.write(f'# width_cell = {width_cell} ')
        f.write(f'# board_plus = {board_plus}, height_chessboard = {height_chessboard}\n')
        f.write('c 0 0 0\n')

    with open(fn_white_chessboard, 'w') as file:
        write_data_to_file(file, '# white cells of chessboard\n')
        for i in range(len(whitep)):
            file.write(f'v {whitep[i][0]} {whitep[i][1]} {whitep[i][2]}\t\t# {i + 1}\n')
        for i in range(len(whitev)):
            file.write(f'f v{whitev[i][0] + 1} v{whitev[i][1] + 1} v{whitev[i][2] + 1}\n')

    with open(fn_black_chessboard, 'w') as file:
        write_data_to_file(file, '# black cells of chessboard\n')
        for i in range(len(blackp)):
            file.write(f'v {blackp[i][0]} {blackp[i][1]} {blackp[i][2]}\t\t# {i + 1}\n')
        for i in range(len(blackv)):
            file.write(f'f v{blackv[i][0] + 1} v{blackv[i][1] + 1} v{blackv[i][2] + 1}\n')

    with open(fn_base_chessboard, 'w') as file:
        write_data_to_file(file, '# base of chessboard\n')
        for i in range(len(basep)):
            file.write(f'v {basep[i][0]} {basep[i][1]} {basep[i][2]}\t\t# {i + 1}\n')
        for i in range(len(basev)):
            file.write(f'f v{basev[i][0] + 1} v{basev[i][1] + 1} v{basev[i][2] + 1}\n')

    with open(fn_data_chessborad, 'w') as file:
        file.write(f'cell_width {width_cell}\n')
        # file.write(f'r_chess {r}\n')
        # file.write(f'delta_r {delta_r}\n')