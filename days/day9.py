import numpy as np

def part_1(input_data):
    total = 0
    for history in input_data:
        layers = get_layers(history)

        val = 0
        for layer in layers[::-1]:
            val += layer[-1]

        total += val

    return total

def part_2(input_data):
    total = 0
    for history in input_data:
        layers = get_layers(history)

        val = 0
        for layer in layers[::-1]:
            val = layer[0] - val

        total += val

    return total

def get_layers(history):
    values = np.array(list(map(int, history.split(" "))))
    layers = [values]
    while not (layers[-1]==0).all():
        layers.append(np.diff(layers[-1]))

    return layers