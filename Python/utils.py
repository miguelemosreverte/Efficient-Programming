
def read_data_into_layers():
    from collections import defaultdict

    layers = defaultdict(list)
    import os.path

    closer_relative_path = "../data"
    longer_relative_path = "../../data"
    data_relative_path = closer_relative_path if os.path.exists(closer_relative_path) else longer_relative_path
    with open(data_relative_path) as f:
        data = f.readlines()

    layer_index = 0
    for line in data:
        if line != "\n":
            matrix_row = \
                [int(a) for a in line.strip() if a != " "]
            layers[layer_index].append(matrix_row)
        else:
            layer_index += 1
    return layers
