import plotly.graph_objects as go
from math import log2
import numpy as np


def lpad(s : str, l : int):
    while len(s) < l:
        s = ('0' + s)
    return s

f = open('output/output.txt')
n = len(f.read())
f.close()

f = open('output/vectors_total.txt')
values_total = f.read().split()
values_total = [int(x) / n for x in values_total]
values_total = dict(zip(list(lpad(bin(i)[2::], int(log2(len(values_total)))) for i in range(len(values_total))), values_total))
f.close()

f = open('output/tree_log.txt')
size = int(f.readline())
for _ in range(size - 2):
    f.readline()
layer = f.readline().split()
values_expected = dict(zip(list(lpad(bin(i)[2::], int(log2(len(layer)))) for i in range(len(layer))), layer))
f.close()

# print(s)

fig = go.Figure()


fig.add_trace(go.Scatter(x=list(values_total.keys()), y=list(values_total.values())))
fig.add_trace(go.Scatter(x=list(values_expected.keys()), y=list(values_expected.values())))


fig.show()




