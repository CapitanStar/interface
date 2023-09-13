import matplotlib.pyplot as plt
import numpy as np


width = 0.25
x_list = list(range(0, 5))
y1_list = [29, 20, 14, 13, 9]
y2_list = [13, 25, 36, 43, 59]
y3_list = [2, 5, 15, 30, 50]
y4_list = [59, 50, 35, 27, 10]
x_indexes = np.arange(len(x_list))

plt.figure()
plt.subplot()

plt.subplot(2, 2, 1)
plt.title("My darkest fears")
plt.xticks(x_indexes, ["5 y/o", "10 y/o", "14 y/o", "18 y/o", "21 y/o",])
plt.xlabel("Time")
plt.ylabel("fear rate")
plt.bar(x_indexes - (width/2), y1_list,
        label="being alone for a lifetime", width=width)
plt.bar(x_indexes + (width/2), y2_list, label="become hobo", width=width)
plt.bar(x_indexes - (width/4), y3_list,
        label="get sick with an incurable disease", width=width)
plt.bar(x_indexes + (width/4), y4_list,
        label="see the monster", width=width)
plt.legend()

plt.subplot(2, 2, 2)
plt.title("Мои худшие кошмары(обновленное)")
plt.xticks(x_indexes, ["5/8/2023", "6/8/2023",
           "7/8/2023", "8/8/2023", "9/8/2023",])
plt.xlabel("Время")
plt.ylabel("Уровень страха")
plt.plot(x_indexes, y1_list,
         label="Страх неизвестности", marker='^')
plt.plot(x_indexes, y2_list, label="Страх потерять время", marker='o')
plt.plot(x_indexes, y3_list,
         label="Боязнь бюрократии", marker='o')
plt.plot(x_indexes, y4_list,
         label="Боязнь службы", marker='^')
plt.legend()

plt.subplot(2, 2, 3)
plt.title("Состояние на сегодняшний день")
plt.xticks(x_indexes, ["5/8/2023", "6/8/2023",
           "7/8/2023", "8/8/2023", "9/8/2023",])
plt.xlabel("Время")
plt.ylabel("Интенсивность")
plt.plot(x_indexes, y1_list, label="Паника, страх и прочее", marker='^')
plt.plot(x_indexes, y2_list,
         label="Желание использовать графики в повседневной жизни", marker='^')
plt.legend()
plt.show()
