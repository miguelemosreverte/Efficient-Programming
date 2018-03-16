
from typing import Tuple, List, Dict


class Coordinate:

    def __init__(self, coord: Tuple[int, int, int], value: int):
        self.coordinate = coord
        self.x = self.coordinate[0]
        self.y = self.coordinate[1]
        self.z = self.coordinate[2]
        self.content = value

    def __str__(self):
        return str([self.x, self.y, self.z, self.content])

    def __iter__(self):
        return iter([self.x, self.y,  self.z, self.content])

    def __repr__(self):
        return self.__str__()


class Layer:
    def __init__(self, layer_as_2d_array: List[List[Coordinate]]):
        self.layer = layer_as_2d_array

    def get_horizontal_neighbors(self, x_y_tuple):
        x, y = x_y_tuple

        def try_getitem(x, y):
            if x == -1 or y == -1:
                return None
            try:
                return self.__getitem__((x, y))
            except IndexError:
                return None

        neighbors = [try_getitem(x + 1, y),
                     None if (x-1 == -1) else try_getitem(x - 1, y),
                     try_getitem(x, y + 1),
                     None if (y - 1 == -1) else try_getitem(x, y - 1),
                     ]
        return neighbors

    def get_coordinates_by_condition(self, coordinate_condition):
        return [maybe_water_coordinate
                for row_that_may_contain_water in self.layer
                for maybe_water_coordinate in row_that_may_contain_water
                if coordinate_condition(maybe_water_coordinate)]

    def __getitem__(self, x_y_tuple):
        x, y = x_y_tuple
        return self.layer[x][y]

    def __str__(self):
        return "\n".join([" ".join([str(coord.content)
                          for coord in row])
                          for row in self.layer])

    def verbose(self):
        return "\n".join([" ".join([str(coord)
                          for coord in row])
                          for row in self.layer])


class Grid:

    def __init__(self, layers_by_height: Dict[int, Layer]):
        self.grid = layers_by_height

    def get_coordinates_by_condition(self, coordinate_condition) -> List[Coordinate]:
        return [coordinate for layer in
                [self.grid[layer_height].get_coordinates_by_condition(coordinate_condition)
                    for layer_height in self.grid]
                for coordinate in layer]

    def get_neighbors(self, x, y, z):

        def try_getitem(x, y, z):
            coordinate = None
            # height check
            if z != -1 and z != len(self.grid.keys()):
                coordinate = self.__getitem__((x, y, z))
            return coordinate

        neighbors = self.grid[z].get_horizontal_neighbors((x, y))

        vertical_neighbors = [try_getitem(x, y, z + 1), try_getitem(x, y, z - 1)]
        neighbors.extend(vertical_neighbors)

        return neighbors

    def __getitem__(self, x_y_z_tuple):
        x, y, z = x_y_z_tuple
        return self.grid[z][x, y]

    def __str__(self):
        return "\n\n".join([str(layer_to_print) for layer_to_print in self.grid.values()])

    def verbose(self):
        return "\n\n".join([layer_to_print.verbose() for layer_to_print in self.grid.values()])
