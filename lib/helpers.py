def normalize_area(area):
    new_area = area.split(" ", maxsplit=1)
    new_area = new_area[1]
    new_area = new_area.replace("/", "-")

    return new_area

def alfa_order_by_key(uo_dict):
    o_dict = sorted(uo_dict, key=uo_dict.__get_key__)
    return list(o_dict)