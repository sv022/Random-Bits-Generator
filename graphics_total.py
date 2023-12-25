import plotly.graph_objects as go
from math import log2
import numpy as np


def lpad(s : str, l : int):
    while len(s) < l:
        s = ('0' + s)
    return s

# номер слоя
f = open('output/output.txt')
n = len(f.read())
f.close()

# подсчет частоты в полученной последовательности
f = open('output/vectors_total.txt')
values_total = f.read().split()
values_total = [int(x) / n for x in values_total]
values_total = dict(zip(list(lpad(bin(i)[2::], int(log2(len(values_total)))) for i in range(len(values_total))), values_total))
f.close()

# подсчет ожидаемых значений
f = open('output/tree_log.txt')
size = int(f.readline())
p0, p1 = 0, 0
for i in range(size - 2):
    temp = f.readline()
    if i == 1: p0, p1 = map(float, temp.split())
layer = list(map(float, f.readline().split()))
values_expected = dict(zip(list(lpad(bin(i)[2::], int(log2(len(layer)))) for i in range(len(layer))), layer))
f.close()

# подсчет отклонения
d_pos, d_neg = 0, 0
k_pos, k_neg = 0, 0
for expected, actual in zip(values_expected.items(), values_total.items()):
    if (expected[1] - actual[1] >= 0):
        d_pos += (expected[1] - actual[1])
        k_pos += 1
    else:
        d_neg += (actual[1] - expected[1])
        k_neg += 1

print('Отклонения')
print(f"Положительные: {d_pos} Отрицательные: {d_neg}")
print(f'Полученное значение C/D: {(d_pos / k_pos) / (d_neg / k_neg)}')
print(f'Ожидаемое значение C/D: {(k_pos + k_neg) / k_pos - 1}')


fig = go.Figure()
fig.update_layout(title=f'p(0) = {p0}, p(1) = {p1}')
fig.update_xaxes(title="Вектор")
fig.update_yaxes(title="Абсолютная вероятность")

fig.add_trace(go.Scatter(x=list(values_expected.keys()), y=list(values_expected.values()), name='Ожидаемые значения'))
fig.add_trace(go.Scatter(x=list(values_total.keys()), y=list(values_total.values()), name='Полученные значения'))


fig.show()




