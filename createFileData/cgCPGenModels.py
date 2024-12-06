import math
from chessboard import chessboard
from pawn import pawn
from rook import rook
from knight import knight
from bishop import bishop

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
    width_cell = pawn_h
    board_plus = width_cell // 2
    height_chessboard = width_cell

    chessboard(width_cell, board_plus, height_chessboard)
    pawn(pawn_h)
    rook(rook_h)
    knight(knight_h)
    bishop(bishop_h)
    # queen(r)
    # king(r)



def pawn_old(radius, plus_alpha):
    H = 2 * radius / gRatio
    r1 = (radius, 0)
    # r1 = (H * gRatio / 2, 0)                    # r1 = (0.309*H, 0)
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
        f.write(f'# r={R}, pawn h={H}, alpha={plus_alpha}\n\n')
        f.write(create_file(rs))
        print(create_file(rs))

def rook_old(radius):
    H = 2 * radius / gRatio * 1.2
    r1 = (radius, 0)
    # r1 = (H * gRatio / 2, 0)  # r1 = (0.309*H, 0)
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
        f.write(f'# r={radius}, rook h={H}\n\n')
        f.write(create_file(rs))
        print(create_file(rs))

def bishop_old(radius, plus_alpha):
    H = 2 * radius / gRatio * 1.2
    r1 = (radius, 0)                   # r1 = (0.309*H, 0)
    r2 = (r1[0], r1[0] / 2)
    r3 = (H * gRatio / 6, gRatio * H)
    r4 = (H * gRatio / 4, H * 0.809)
    r5 = (0, H)
    rs = [(0, 0), r1, r2, r3, r4, r5]

    print('\n'.join([f'({x:.3f}, {y:.3f})' for x, y in rs]))
    with open(fn_bishop, 'w') as f:
        f.write(f'# r={radius}, bishop h={H}, alpha={plus_alpha}\n\n')
        f.write(create_file(rs))
        print(create_file(rs))
    # center = (0, H)
    # plus_alpha = math.radians(plus_alpha)
    # pozah = r3[1] * 1.2
    # def poza(alpha1):
    #     return pozah * abs((math.cos(2 * alpha1)) ** 0.6)
    #
    # rs_poza = []
    # y = H
    # alpha = math.pi / 2 # math.pi * 5 / 4 + plus_alpha
    # while alpha < math.pi * 3 / 4: # and y > r3[1]:
    #     tmp_r = poza(alpha)
    #     print(f'alphs = {alpha}, r = {tmp_r:.3f}')
    #     if not isinstance(tmp_r, complex):
    #         x = tmp_r * math.cos(alpha + math.pi) + center[0]
    #         y = tmp_r * math.sin(alpha + math.pi) + center[1]
    #         if abs(x) < 1e-5: x = 0
    #         if abs(y) < 1e-5: y = 0
    #         rs_poza.append((x, y))
    #     alpha += plus_alpha # math.pi / 10
    # rs_poza.append(center)
    #
    # for elem in rs_poza:
    #     print(elem)
    #
    # rs = []

def queen(radius):
    H = 2 * radius / gRatio * 1.3
    r1 = (radius, 0)  # r1 = (0.309*H, 0)
    r2 = (r1[0], r1[0] / 2)
    rs = [(0, 0), r1, r2]
    rs.extend([
        (H * gRatio / 6, H * gRatio),
        (H * gRatio / 3.5, H * (1 - (1 - gRatio) / 2.5)),
        (H * gRatio / 2, H),
        (H * gRatio / 3.5, H * (1 - (1 - gRatio) / 5.5)),
        (H * gRatio / 5.5, H * (1 - (1 - gRatio) / 2.5)),
        (0, H * (1 - (1 - gRatio) / 2.5)),
    ])
    print('\n'.join([f'({x:.3f}, {y:.3f})' for x, y in rs]))
    with open(fn_queen, 'w') as f:
        f.write(f'# r={radius}, queen h={H}\n\n')
        f.write(create_file(rs))
        print(create_file(rs))

def king(radius):
    H = 2 * radius / gRatio * 1.3
    r1 = (radius, 0)  # r1 = (0.309*H, 0)
    r2 = (r1[0], r1[0] / 2)
    rs = [(0, 0), r1, r2]
    rs.extend([
        (H * gRatio / 6, H * gRatio),
        (H * gRatio / 3, H * 0.9),
        (H / 40, H),
        (H / 20, H * 1.05),
        (0, H * 1.1),
    ])
    print('\n'.join([f'({x:.3f}, {y:.3f})' for x, y in rs]))
    with open(fn_king, 'w') as f:
        f.write(f'# r={radius}, king h={H}\n\n')
        f.write(create_file(rs))
        print(create_file(rs))

# def knight(radius)







