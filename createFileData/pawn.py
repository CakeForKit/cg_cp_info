import math

def pawn(radius, plus_alpha, fn_pawn):
    H = 2 * radius
    r1 = (radius, 0)                # r1 = (0.309*H, 0)
    r2 = (radius, 0.1 * H)                     # r2 = (0.309*H, 0.5 * 0.309 * H)
    r3 = (radius / 2, H / 3)
    # x**2 + (y-b)**2 = R**2
    b = 0.84 * H # H * (gRatio + gRatio_ / 2)              # b = 809 * H
    R = H - b                       # R = 0.191 * H
    center = (0, b)                             # center = (0, b)

    # прямая между center-r2
    k = (r2[1] - center[1]) / (r2[0] - center[0])
    # точка пересечения между окружностью и прямой
    xr3 = R / math.sqrt(1 + k**2)
    yr3 = k * xr3 + b
    r4 = (xr3, yr3)

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

    rs = [(0, 0), r1, r2, r3, r4, *circle_r]
    print('\n'.join([f'({x:.3f}, {y:.3f})' for x, y in rs]))
    with open(fn_pawn, 'w') as f:
        f.write(f'# r={R}, pawn h={H}, alpha={plus_alpha}\n\n')
        f.write(create_file(rs))
        print(create_file(rs))