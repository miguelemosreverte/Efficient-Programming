from profesional.grid import Grid
from profesional.contents import Contents


def flood_fill_iteration(grid_to_flood: Grid) -> Grid:

    def try_fill(a, b, c):
        # secondary effects FTW
        try:
            grid_to_flood.grid[c][a, b].content = Contents.Water.value
        except KeyError:
            print("try_fill problem at ", a, b, c)
            pass

    def is_water(coordinate):
        # first order function
        return coordinate.content == Contents.Water.value

    flood_coordinates = grid_to_flood.get_coordinates_by_condition(is_water)

    for flood_coordinate in flood_coordinates:  # and then, we use them.
        x, y, z, value = flood_coordinate

        plusX, lessX, plusY, lessY, plusZ, lessZ = grid_to_flood.get_neighbors(x, y, z)

        for floodable_neighbor in [plusX, lessX, plusY, lessY, lessZ]:
            if floodable_neighbor:
                x, y, z, value = floodable_neighbor
                try_fill(x, y, z)

    return grid_to_flood
