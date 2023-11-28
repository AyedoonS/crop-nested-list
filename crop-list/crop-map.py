# CROP NESTED LIST (MAP)

def crop_map(m: list[list[int]], corner_1: tuple[int, int],
             corner_2: tuple[int, int]) -> list[list[int]]:
    """
    Crops a nested list, <m>, and returns the cropped list
    """
    cropped_map = []

    for i in range(min(corner_1[0], corner_2[0]),
                   max(corner_1[0] + 1, corner_2[0] + 1)):

        cropped_map.append(m[i][min(corner_1[1], corner_2[1]):
                                max(corner_1[1] + 1, corner_2[1] + 1)])
    return cropped_map
