from createFile import *


def bishop(H):
    R = 0.25 * H
    r1 = (R, 0)
    r2 = (R, 0.15 * H)
    rs = [
        (0, 0),
        r1,
        r2,
        # (0.5 * R, 0.28 * H),
        (0.35 * R, 0.47 * H),
        (0.35 * R, 0.57 * H),
        (0.6 * R, 0.8 * H),
        (0.4 * R, 0.9 * H),
        (0, H)
    ]

    c = H ** 2 + R ** 2
    sphere = c / ((4 * c - 4 * R ** 2) ** 0.5)
    with open(fn_bishop, 'w') as f:
        f.write(f'# bishop \n# r={R}, h={H}\n\n')
        f.write(create_file(rs, sphere, H - sphere))
        # print(create_file(rs))