logBeg = r"""\begin{longtable}{|
		>{\raggedright\arraybackslash}p{.2\textwidth - 2\tabcolsep}|
		>{\raggedright\arraybackslash}p{.2\textwidth - 2\tabcolsep}|
		>{\raggedright\arraybackslash}p{.3\textwidth - 2\tabcolsep}|
		>{\raggedright\arraybackslash}p{.3\textwidth - 2\tabcolsep}|
	}
	\caption{Функциональные тесты}\label{tbl:tests} \\\hline
	№ заявки & № потока & время начала обслучивания заявки & время конца обслуживания заявки \\\hline
	\endfirsthead
	\caption{Функциональные тесты (продолжение)} \\\hline
	№ заявки & № потока & время начала обслучивания заявки & время конца обслуживания заявки \\\hline                    
	\endhead
	\endfoot
	"""
logEnd = r"""
\end{longtable}"""

need = r"""
	0 & 1 & 249 & 270 \\\hline
	0 & 1 & 249 & 270 \\\hline
"""


# tstart=249        tend=270        request=0    thread=1

def create_table_log():
    tabstr = ''
    filename = 'log/log.txt'
    with open(filename, 'r') as f:
        line = f.readline()
        while line != '':
            d = line.split('=')
            ts, te, req, thr = d[1].split()[0], d[2].split()[0], d[3].split()[0], d[4].split()[0]
            s = rf'{req} & {thr} & {ts} & {te} \\\line' + '\n'

            tabstr += s

            line = f.readline()
    table = logBeg + tabstr + logEnd
    fileout = 'log/tex_table_log.txt'
    with open(fileout, 'w') as f:
        f.write(table)


# - среднее время существования задачи;
# - среднее время ожидания задачи в каждой из очередей;
# - среднее время обработки задачи на каждой из стадий.
def get_statistic():
    goods = 'good_'
    with open(f'log/{goods}p1_log.txt', 'r') as f1:
        with open(f'log/{goods}p2_log.txt', 'r') as f2:
            with open(f'log/{goods}p3_log.txt', 'r') as f3:
                lines = [f1.readline(), f2.readline(), f3.readline()]

                exist_time, q2_time, q3_time, thr1_time, thr2_time, thr3_time = [], [], [], [], [], []
                while lines[0] != '':
                    times = [(int(elem[0]), int(elem[1])) for elem in [line.split() for line in lines]]
                    # print(times)

                    exist_time.append(times[-1][-1] - times[0][0])
                    q2_time.append(times[1][0] - times[0][1])
                    q3_time.append(times[2][0] - times[1][1])
                    thr1_time.append(times[0][1] - times[0][0])
                    thr2_time.append(times[1][1] - times[1][0])
                    thr3_time.append(times[2][1] - times[2][0])

                    lines = [f1.readline(), f2.readline(), f3.readline()]

                print('avg exist_time =', sum(exist_time) / len(exist_time))
                print('avg q2_time =', sum(q2_time) / len(q2_time))
                print('avg q3_time =', sum(q3_time) / len(q3_time))
                print('avg thr1_time =', sum(thr1_time) / len(thr1_time))
                print('avg thr2_time =', sum(thr2_time) / len(thr2_time))
                print('avg thr3_time =', sum(thr3_time) / len(thr3_time))


if __name__ == '__main__':
    # get_statistic()
    create_table_log()
