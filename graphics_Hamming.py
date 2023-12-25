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

f = open('output/vectors_Hamming.txt')
values_Hamming = f.read().split()
values_Hamming = {x[0] : int(x[1]) / n for x in enumerate(values_Hamming)}
# print(values_Hamming)
f.close()


f = open('output/tree_log.txt')
size = int(f.readline())
for _ in range(size - 2):
    f.readline()
layer = f.readline().split()
values_expected = [0 for _ in range(size - 1)]
for i, x in enumerate(layer):
    v = bin(i)[2::]
    values_expected[v.count("1")] += float(x)
values_expected = {x[0]: x[1] for x in enumerate(values_expected)}
# print(values_expected)
f.close()


fig = go.Figure()

fig.add_trace(go.Scatter(x=list(values_Hamming.keys()), y=list(values_Hamming.values())))
fig.add_trace(go.Scatter(x=list(values_expected.keys()), y=list(values_expected.values())))

fig.show()
