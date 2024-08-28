# Импорт библеотек
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Напряжение U_a_0
Ua0 = -6

# Напряжение U_0
U0 = 3

# Частота w
w = 1

# Формула для t_k
t_k1 = (np.arcsin(U0 / Ua0)) / w

# Создание списка с разными t_k от -30 град до 30 град с интервалом 10 град
t_k = np.linspace(0, t_k1, 4)
t_k2 = t_k * (-1)
a = np.sort(np.concatenate([t_k, t_k2[1:]]))

t = np.linspace(0, 13 * np.pi / 6, 1050)

tw = w * t


# Функция, описывающая траекторию электрона в высокочастотном диоде

def z(tk, t1):
    z1 = -np.sin(w * t1) - np.cos(w * tk) * (w * tk - w * t1) + np.sin(w * tk) * (
            -0.5 * np.power(w, 2) * np.power(t1, 2) +
            np.power(w, 2) * tk * t1 + 1 + 0.5 * np.power(w, 2) * tk - np.power(w, 2) * np.power(tk, 2))
    return z1


# Функция для создания графиков

def picture(h, c):
    k = j - c
    return plt.plot(tw[:k], z(a[h], t)[:k], "k")


# Создание графиков

j = 0
s = 0

while j != (len(tw) * 2):
    j = j + 10
    print(f"Процесс завершён на: {round(j / 21, 1)}%")
    plt.xlim([0, 7])
    plt.ylim([-5, 20])
    plt.xlabel(r'$\omega t$')
    plt.ylabel(r'$Z$')
    plt.title('Траектории электронов в высокочастотном диоде' + '\n' + 'с разными параметрами ' + r'$\omega t_{k}$')
    picture(0, 0)

# Создание задержки между графиками с разными w*t_k
    if j >= 150:
        picture(1, 150)
    if j >= 300:
        picture(2, 300)
    if j >= 450:
        picture(3, 450)
    if j >= 600:
        picture(4, 600)
    if j >= 750:
        picture(5, 750)
    if j >= 900:
        picture(6, 900)

    plt.grid(linewidth=1)
    # Сохранение графиков в формате .png
    plt.savefig(f'figure{s}.png', dpi=100)

    # Подсчёт количества графиков(картинок)
    s = s + 1

# Создание анимации графиков в формате .gif
# Список для хранения кадров.
frames = []

for frame_number in range(0, 209):
    # Открываем изображение каждого кадра.
    frame = Image.open(f'figure{frame_number}.png')
    # Добавляем кадр в список с кадрами.
    frames.append(frame)

# Берем первый кадр и в него добавляем оставшееся кадры.
frames[0].save(
    'figures.gif',
    save_all=True,
    append_images=frames[1:],  # Срез который игнорирует первый кадр.
    optimize=True,
    duration=10,
    loop=0
)

# Удаление графиков
import pathlib

for i in range(210):
    file = pathlib.Path(f"figure{i}.png")
    file.unlink()
