import math
from createFile import *

def rook(H):
    R = 0.25 * H
    r1 = (R, 0)
    r2 = (R, 0.15 * H)
    
    rs = [
        (0, 0),
        r1,
        r2,
        (0.6 * R, 0.8 * H),
        (0.9 * R, 0.8 * H),
        (R, H),
        (0.8 * R, H),
        (0.7 * R, 0.85 * H),
        (0, 0.85 * H),
    ]
    # print('\n'.join([f'({x:.3f}, {y:.3f})' for x, y in rs]))
    with open(fn_rook, 'w') as f:
        f.write(f'# rook \n# r={R}, h={H}\n\n')
        f.write(create_file(rs))