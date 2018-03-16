from utils import read_data_into_layers


def flood_fill_iteration(layers):

    def try_fill(x, y, z):
        # secondary effects FTW
        try:
            layers[z][y][x] = 1
        except IndexError:
            pass

    flood_coordinates = []  # we store them
    for z in layers:
        for y in range(0, len(layers[z])):
            for x in range(0, len(layers[z][y])):
                if layers[z][y][x] == 1:
                    flood_coordinates.append((x, y, z))
    for flood_coordinate in flood_coordinates:  # and then, whe use them.
        x, y, z = flood_coordinate
        try_fill(x + 1, y, z)
        try_fill(x - 1, y, z)
        try_fill(x, y + 1, z)
        try_fill(x, y - 1, z)
        try_fill(x, y, z - 1)


    return layers


if __name__ == "__main__":
    layers = read_data_into_layers()

    flood_fill_iteration(layers)

    print("output:")
    for height in layers:
        print()
        for row in layers[height]:
            print(" ".join((str(coord) for coord in row)))
