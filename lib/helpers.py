def normalize_area(area):
    new_area = area.split(" ", maxsplit=1)
    new_area = new_area[1]
    new_area = new_area.replace("/", "-")

    return new_area