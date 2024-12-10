import matplotlib.pyplot as plt


def draw_graph(filename, split_by):
    data_triangles = []
    pTh = [0, 1, 2, 4, 8, 16, 32, 100, 1000]
    data_pTh = [[] for _ in range(len(pTh))]

    with open(filename) as f:
        f.readline()
        line = f.readline()
        while line != '':
            # print(line.split(split_by)[:])
            data = list(map(float, line.split()[:]))

            data_triangles.append(int(data[0]))
            for i in range(len(pTh)):
                data_pTh[i].append(int(data[i + 1]))
            line = f.readline()

    # for i in range(len(pTh)):
    #     print(data_pTh[i])

    for i in range(len(data_pTh)):
        data_pTh[i] = [elem // 1000000 for elem in data_pTh[i]]

    plt.figure(1)
    plt.plot(data_triangles[:], data_pTh[0], color='r', linestyle='solid', label='без дополнительных потоков')
    plt.plot(data_triangles[:], data_pTh[1], color='g', linestyle='dotted', label='1 дополнительный поток')
    plt.plot(data_triangles[:], data_pTh[2], color='b', linestyle='dashed', label='2 дополнительных потока')
    plt.plot(data_triangles[:], data_pTh[3], color='black', linestyle='dashdot', label='4 дополнительный поток')
    plt.plot(data_triangles[:], data_pTh[4], color='c', marker='.', label='8 дополнительных потока')
    plt.plot(data_triangles[:], data_pTh[5], color='m', marker='v', label='16 дополнительных потока')
    plt.plot(data_triangles[:], data_pTh[6], color='k', marker='x', label='32 дополнительных потока')
    plt.plot(data_triangles[:], data_pTh[6], color='y', marker='*', label='64 дополнительных потока')
    # plt.plot(data_triangles[:], data_pTh[6], color='r', marker='+', label='1000 дополнительных потока')
    plt.title('Зависимость времени отрисовки сцены от количества треугольных полигонов на сцене')  # Подпись для оси х
    plt.xlabel('Количество треугольных полигонов на сцене')  # Подпись для оси х
    plt.ylabel('Время, с')  # Подпись для оси y
    plt.legend()
    plt.show()

# 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline
def getTab(filename, split_by):
    text = ''
    with open(filename) as f:
        f.readline()
        line = f.readline()
        while line != '':
            sp = line.split()
            data = list(map(lambda x: float(x) / 1e6, sp[1:-1]))

            tline = ''
            tline += f'{sp[0]} & ' + ' & '.join([f'{elem:.2f}' for elem in data])
            tline += ' \\\\ \\hline\n'
            text += tline
            line = f.readline()
    print(text)


getTab('data_time/dataTime.txt', '\t')
# draw_graph('data_time/dataTime.txt', '\t')