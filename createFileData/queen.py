from createFile import *


def queen(H):
    R = 0.25 * H
    r1 = (R, 0)
    r2 = (R, 0.15 * H)
    rs = [
        (0, 0),
        r1,
        r2,
        (0.6 * R, 0.25 * H),
        (0.33 * R, 0.42 * H),
        (0.33 * R, 0.7 * H),
        (0.5 * R, 0.73 * H),
        (0.33 * R, 0.75 * H),
        (0.36 * R, 0.85 * H),
        (0.55 * R, 0.94 * H),
        (0, 0.94 * H),
        (0.1 * R, 0.97 * H),
        (0, H),
    ]

    # print('\n'.join([f'({x:.3f}, {y:.3f})' for x, y in rs]))
    with open(fn_queen, 'w') as f:
        f.write(f'# queen \n# r={R}, h={H}\n\n')
        f.write(create_file(rs))
        # print(create_file(rs))