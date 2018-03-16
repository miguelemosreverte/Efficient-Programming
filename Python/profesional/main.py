from profesional.grid import Grid, Layer, Coordinate

from utils import read_data_into_layers
from profesional.algorithms import flood_fill_iteration


if __name__ == "__main__":
    layers = read_data_into_layers()

    def type_grid(untyped_layers):
        grid = {}
        for z in untyped_layers:
            matrix = []
            for i, row in enumerate(untyped_layers[z]):
                typed_row = []
                for x, value in enumerate(row):
                    typed_row.append(Coordinate((x, i, z), value))
                matrix.append(typed_row)
            grid[z] = Layer(matrix)

        return Grid(grid)

    typedGrid = type_grid(layers)
    
    flood_fill_iteration(typedGrid)

    print("output:")
    print()
    print(typedGrid)
