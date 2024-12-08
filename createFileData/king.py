from createFile import *


def king(H):
    R = 0.25 * H
    r1 = (R, 0)
    r2 = (R, 0.15 * H)
    rs = [
        (0, 0),
        r1,
        r2,
        (0.6 * R, 0.25 * H),
        (0.33 * R, 0.42 * H),
        (0.33 * R, 0.65 * H),
        (0.5 * R, 0.67 * H),
        (0.33 * R, 0.69 * H),

        (0.65 * R, 0.88 * H),
        (0.5 * R, 0.92 * H),
        (0.1 * R, 0.93 * H),
        (0.2 * R, H),
        (0, 0.98 * H),
    ]

    # print('\n'.join([f'({x:.3f}, {y:.3f})' for x, y in rs]))
    with open(fn_king, 'w') as f:
        f.write(f'# king \n# r={R}, h={H}\n\n')
        f.write(create_file(rs))
        # print(create_file(rs))