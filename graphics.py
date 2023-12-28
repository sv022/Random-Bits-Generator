import plotly.graph_objects as go
from plotly.subplots import make_subplots
from math import log2
import numpy as np
from utilities import *


irises_colors = ['rgb(33, 75, 99)', 'rgb(79, 129, 102)', 'rgb(151, 179, 100)',
                 'rgb(175, 49, 35)', 'rgb(36, 73, 147)']
sunflowers_colors = ['rgb(177, 127, 38)', 'rgb(205, 152, 36)', 'rgb(99, 79, 37)',
                     'rgb(129, 180, 179)', 'rgb(124, 103, 37)']


def plot_abs():
    n = file_length('output/output.txt')
    values_abs = get_values('output/vectors_total.txt', "abs", n)
    values_expected, p0, p1 = get_expected_values('abs')
    d = devation(values_abs, values_expected)
    d_pos, k_pos = d[0]
    d_neg, k_neg = d[1]
    dev_list = devation_list(values_abs, values_expected)

    fig_abs = make_subplots(rows=2, cols=1)
    fig_abs.update_layout(title=f'p(0) = {p0}, p(1) = {p1}')
    fig_abs.update_xaxes(title="Вектор", row=1, col=1)
    fig_abs.update_yaxes(title="Абсолютная вероятность", row=1, col=1)
    
    fig_abs.update_xaxes(title="Вектор", row=2, col=1)
    fig_abs.update_yaxes(title="Отклонение", row=2, col=1)
    

    fig_abs.add_trace(go.Scatter(x=list(values_expected.keys()), y=list(values_expected.values()), name='Ожидаемые значения', mode='lines+markers'), 1, 1)
    fig_abs.add_trace(go.Scatter(x=list(values_abs.keys()), y=list(values_abs.values()), name='Полученные значения', mode='lines+markers'), 1, 1)
    
    fig_abs.add_trace(go.Scatter(x=list(dev_list), y=list(dev_list.values()), name='Отклонение', mode='lines+markers'), 2, 1)

    fig_abs.show()
    

def plot_Hamming():
    n = file_length('output/output.txt')
    values_Hamming = get_values('output/vectors_Hamming.txt', "hamming", n)
    values_expected, p0, p1 = get_expected_values("hamming")    
    d = devation(values_Hamming, values_expected)
    d_pos, k_pos = d[0]
    d_neg, k_neg = d[1]
    dev_list = devation_list(values_Hamming, values_expected)
    
    fig_Hamming = make_subplots(rows=2, cols=1)     
    fig_Hamming.update_layout(title=f'p(0) = {p0}, p(1) = {p1}')
    fig_Hamming.update_xaxes(title="Расстояние Хемминга", row=1, col=1)
    fig_Hamming.update_yaxes(title="Абсолютная вероятность", row=1, col=1)
    
    fig_Hamming.update_xaxes(title="Расстояние Хемминга", row=2, col=1)
    fig_Hamming.update_yaxes(title="Отклонение", row=2, col=1)

    fig_Hamming.add_trace(go.Scatter(x=list(values_Hamming.keys()), y=list(values_Hamming.values()), name='Ожидаемые значения', mode='lines+markers'), 1, 1)
    fig_Hamming.add_trace(go.Scatter(x=list(values_expected.keys()), y=list(values_expected.values()), name='Полученные значения', mode='lines+markers'), 1, 1)

    fig_Hamming.add_trace(go.Scatter(x=list(dev_list), y=list(dev_list.values()), name='Отклонение', mode='lines+markers'), 2, 1)
    
    fig_Hamming.show()


def plot_packets(size : int, extend_to : int):
    f = open('output/packets.txt')
    packets = [line.strip() for line in f]
    packets_normal = len([x for x in packets if len(x) == extend_to])
    packets_extended = len([x for x in packets if len(x) == size])
    
    fig_packets = make_subplots(rows=2, cols=1, specs=[[{'type':'xy'}], [{'type':'domain'}]])    
    fig_packets.update_xaxes(title="Номер пакета", row=1, col=1)
    fig_packets.update_yaxes(title="Размер пакета", row=1, col=1)
    fig_packets.add_trace(go.Bar(y=[len(p) for p in packets], name="Размер пакета", marker_color='lightslategrey'), 1, 1)
    fig_packets.add_trace(go.Pie(values=[packets_normal, packets_extended], labels=[f'Размер {size}', f'Размер {extend_to}'], marker_colors=irises_colors), 2, 1)
    fig_packets.update_layout(title=f"Размер пакета: {size}, после расширения: {extend_to}")
    fig_packets.show()


# plot_abs()
# plot_Hamming()
plot_packets(8, 16)