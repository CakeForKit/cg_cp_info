from createFile import *


def knight(H):
    R = 0.25 * H
    r1 = (R, 0)
    r2 = (R, 0.15 * H)
    r3 = (0, 0.15 * H)
    rs = [(0, 0), r1, r2, r3]
    text = create_file(rs)

    base1 = [
        (0.5 * R, 0.15 * H),
        (R, 0.5 * H),
        (R, 0.75 * H),
        (0, H),
        (0, 0.94 * H),
        (-R, 0.7 * H),
        (-R, 0.6 * H),
        (0, 0.6 * H),
        (-0.75 * R, 0.4 * H),
        (-0.5 * R, 0.15 * H),
    ]

    base2 = base1[:]
    width_2 = 0.35 * R
    for i in range(len(base1)):
        base1[i] = (*base1[i], width_2)
        base2[i] = (*base2[i], -width_2)

    vs = base1 + base2
    text += '\n'
    for i in range(len(vs)):
        text += 'v ' + ' '.join(map(str, vs[i])) + f'\t\t# {i + 1}\n'

    n = len(base1)
    f_indexes = [
        (0, 8, 9),
        (0, 8, 1),
        (1, 8, 7),
        (1, 7, 2),
        (7, 2, 3),
        (7, 4, 5),
        (7, 5, 6)
    ]
    flen = len(f_indexes)
    for i in range(flen):
        f_indexes.append(tuple(map(lambda x: x + n, f_indexes[i])))

    # боковая часть
    for i in range(n - 1):
        f_indexes.extend([
            (i, i + 1, i + n),
            (i + n, i + 1 + n, i + 1)
        ])

    for i in range(len(f_indexes)):
        text += 'f ' + ' '.join(map(lambda x: f'v{x + 1}', f_indexes[i])) + '\n'

    with open(fn_knight, 'w') as f:
        f.write(f'# knight \n# r={R}, h={H}\n\n')
        f.write(text)
        # print(create_file(rs))