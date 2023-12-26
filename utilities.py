from math import log2


def lpad(s : str, l : int):
    while len(s) < l:
        s = ('0' + s)
    return s

def file_length(filename : str):
    with open(filename) as f:
        n = len(f.read())
    return n


def get_values(filename : str, metrics: str, size: int):
    if not isinstance(size, int): raise Exception(f'Wrong file size: {size}')
    n = size
    with open(filename) as f:
        values = f.read().split()
    if metrics == "hamming":
        values = {x[0] : int(x[1]) / n for x in enumerate(values)}
    elif metrics == "abs":
        values = [int(x) / n for x in values]
        values = dict(zip(list(lpad(bin(i)[2::], int(log2(len(values)))) for i in range(len(values))), values))
    else:
        raise Exception(f"Wrong metrics type: {metrics}")
    return values


def get_expected_values(metrics: str):
    f = open('output/tree_log.txt')
    size = int(f.readline())
    p0, p1 = 0, 0
    for i in range(size - 2):
        temp = f.readline()
        if i == 1: p0, p1 = map(float, temp.split())
    layer = list(map(float, f.readline().split()))
    f.close()
    if metrics == "hamming":
        values_expected = [0 for _ in range(size - 1)]
        for i, x in enumerate(layer):
            v = bin(i)[2::]
            values_expected[v.count("1")] += float(x)
        values_expected = {x[0]: x[1] for x in enumerate(values_expected)}
    elif metrics == "abs":
        values_expected = dict(zip(list(lpad(bin(i)[2::], int(log2(len(layer)))) for i in range(len(layer))), layer))
    else:
        raise Exception(f"Wrong metrics type: {metrics}")
    # print(values_expected)
    return (values_expected, p0, p1)


def devation(values, values_expected):
    d_pos, d_neg = 0, 0
    k_pos, k_neg = 0, 0
    for expected, actual in zip(values_expected.items(), values.items()):
        if (expected[1] - actual[1] >= 0):
            d_pos += (expected[1] - actual[1])
            k_pos += 1
        else:
            d_neg += (actual[1] - expected[1])
            k_neg += 1
    return ((d_pos, k_pos), (d_neg, k_neg))


def devation_list(values, values_expected):
    dev = {}
    for expected, actual in zip(values_expected.items(), values.items()):
        dev[expected[0]] = expected[1] - actual[1]
    return dev