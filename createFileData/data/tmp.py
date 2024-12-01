import math

gRatio = 0.618
gRatio_ = 1 - gRatio

folder = 'data/'
fn_pawn = folder + 'pawn.txt'
fn_rook = folder + 'rook.txt'
folder_board = folder + 'chessboard/'
fn_white_chessboard = folder_board + 'white_cells_chessboard.txt'
fn_black_chessboard = folder_board + 'black_cells_chessboard.txt'
fn_base_chessboard = folder_board + 'base_chessboard.txt'
fn_data_chessborad = folder_board + 'positions_cells.txt'

# BOARD, PAWN, ROOK = [i for i in range(3)]
# act = ROOK


def create_file(rs):
    text = 'c 0 0 0\n'

    for i in range(len(rs)):
        r = rs[i]
        text += f'r {r[0]} {r[1]} \t\t\t# {i + 1}\n'
    text += '\n'

    for i in range(len(rs) - 1):
        text += f'l r{i+1} r{i+2}\n'

    return text

def pawn(rad, plus_alpha):
    H = rad / gRatio
    r1 = (rad, 0)                    # r1 = (0.309*H, 0)
    r2 = (r1[0], r1[0] / 2)                     # r2 = (0.309*H, 0.5 * 0.309 * H)
    # x**2 + (y-b)**2 = R**2
    b = H * (gRatio + gRatio_ / 2)              # b = 809 * H
    R = H * gRatio_ / 2                         # R = 0.191 * H
    center = (0, b)                             # center = (0, b)

    # прямая между center-r2
    k = (r2[1] - center[1]) / (r2[0] - center[0])
    # точка пересечения между окружностью и прямой
    xr3 = R / math.sqrt(1 + k**2)
    yr3 = k * xr3 + b
    r3 = (xr3, yr3)

    alpha = -math.degrees(math.atan(-k))
    print(f'k={k}, aten={alpha}')
    circle_r = []
    alpha += plus_alpha
    while alpha <= 90:
        x = R * math.cos(math.radians(alpha)) + center[0]
        y = R * math.sin(math.radians(alpha)) + center[1]
        circle_r.append((x, y))
        alpha += plus_alpha

    circle_r.append((0, H))

    rs = [(0, 0), r1, r2, r3, *circle_r]
    print('\n'.join([f'({x:.3f}, {y:.3f})' for x, y in rs]))
    with open(fn_pawn, 'w') as f:
        f.write(f'# pawn h={H}, alpha={alpha}\n\n')
        f.write(create_file(rs))
        print(create_file(rs))

def rook(rad):
    H = rad / gRatio
    r1 = (rad, 0)  # r1 = (0.309*H, 0)
    r2 = (r1[0], r1[0] / 2)  # r2 = (0.309*H, 0.5 * 0.309 * H)
    rs = [(0, 0), r1, r2]
    M = 0.25 * H
    rs.extend([
        (0.8 * M, 0.7 * H),
        (M, 0.7 * H),
        (M, H),
        (0.7 * M, H),
        (0.7 * M, 0.8085 * H),
        (0, 0.8085 * H)
    ])
    print('\n'.join([f'({x:.3f}, {y:.3f})' for x, y in rs]))
    with open(fn_rook, 'w') as f:
        f.write(f'# rook h={H}\n\n')
        f.write(create_file(rs))
        print(create_file(rs))


'''
r - радиус шахмат
delta_r - насколько ширина ячейки шахматной доски больше / 2 больше радиуса шахмат
board_plus - отступ деревянной части шахматной доски от чб ячеек
width - высота шахматной доски
'''
def chessboard(r, delta_r, board_plus, height_chessboard):
    width_cell = 2 * (r + delta_r)
    h = r
    plus_width_board = r // 2
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
            print(f'{i}: ', (x, 0, z), f'\t({i // 9}, {i % 9})')
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
        f.write(f'# r = {r} (of chess), delta_r = {delta_r}\n')
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
        file.write(f'r_chess {r}\n')
        file.write(f'delta_r {delta_r}\n')
        # file.write(f'board_plus {board_plus}\n')
        # file.write(f'height {height_chessboard}\n')





if __name__ == '__main__':
    alpha = 20
    r = 15 # h * gRatio / 2  # 0.309 * h -> 15.45
    delta_r = 1
    board_plus, height_chessboard = (r + delta_r), int(r + delta_r) * 2
    print(board_plus, height_chessboard)

    chessboard(r, delta_r, board_plus, height_chessboard)
    pawn(r, alpha)
    rook(r)
    # if act == BOARD:
    #     chessboard(r, delta_r, board_plus, height_chessboard)
    # elif act == PAWN:
    #     pawn(h, alpha)
    # elif act == ROOK:
    #     rook(h)

