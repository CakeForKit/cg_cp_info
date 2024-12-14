
'''
ka
kd
ks
n
'''


def c_to_i(name, rgb, pka=10, pkd=79, pks=10//2):
    # rgb = 255, 243, 223
    maxI = [elem / 255 for elem in rgb]
    ka = [elem * pka / 100 for elem in maxI]
    kd = [elem * pkd / 100 for elem in maxI]
    ks = [elem * pks / 100 for elem in maxI]


    # for k in [ka, kd, ks]:
    #     print(f'{k[0]:.2f} {k[1]:.2f} {k[2]:.2f}\n')

    text = f'''    materialSolution.registrateMaterial(idMaterial::{name}, 
                                    std::make_shared<Material>( Intensity({ka[0]:.2f}, {ka[1]:.2f}, {ka[2]:.2f}),    // ka
                                                                Intensity({kd[0]:.2f}, {kd[1]:.2f}, {kd[2]:.2f}),       // kd
                                                                Intensity({ks[0]:.2f}, {ks[1]:.2f}, {ks[2]:.2f}),       // ks
                                                                5)); '''
    print(text)


if __name__ == '__main__':
    c_to_i('CLASSIC_WHITE', (255, 230, 184))#(255, 243, 223))
    c_to_i('CLASSIC_BLACK', (145, 78, 12))# (112, 66, 20))
    c_to_i('orange'.upper(), (255, 153, 0))
    c_to_i('purple'.upper(), (157, 0, 255))
    c_to_i('pink'.upper(), (255, 0, 200))
    c_to_i('green'.upper(), (0, 148, 0))
    c_to_i('BLUE'.upper(), (95, 204, 230))
    c_to_i('RED'.upper(), (255, 0, 0))
