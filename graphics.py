import plotly.graph_objects as go
from plotly.subplots import make_subplots
from math import log2
import numpy as np
from utilities import *


def plot_abs():
    n = file_length('output/output.txt')
    values_abs = get_values('output/vectors_total.txt', "abs", n)
    values_expected, p0, p1 = get_expected_values('abs')
    d = devation(values_abs, values_expected)
    d_pos, k_pos = d[0]
    d_neg, k_neg = d[1]
    dev_list = devation_list(values_abs, values_expected)
    #print(list(dev_list.values()))
    # print('Отклонения')
    # print(f"Положительные: {d_pos} Отрицательные: {d_neg}")
    # print(f'Полученное значение C/D: {(d_pos / k_pos) / (d_neg / k_neg)}')
    # print(f'Ожидаемое значение C/D: {(k_pos + k_neg) / k_pos - 1}')
    # print(devation_list(values_abs, values_expected))


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
    # print('Отклонения')
    # print(f"Положительные: {k_pos} Отрицательные: {k_neg}")
    # print(f"Сум. положительные: {d_pos} Сум. отрицательные: {d_neg}")
    # print(f'Полученное значение C/D: {(d_pos / k_pos) / (d_neg / k_neg)}')
    # print(f'Ожидаемое значение C/D: {(k_pos + k_neg) / k_pos - 1}')
    # print(devation_list(values_Hamming, values_expected))
    
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


# plot_abs()
plot_Hamming()