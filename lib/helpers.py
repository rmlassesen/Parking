def _normalize_area(area):
    new_area = area.split(" ", maxsplit=1)
    new_area = new_area[1]
    new_area = new_area.replace("/", "-")

    return new_area

def _alfa_order_by_key(uo_dict):
    o_dict = sorted(uo_dict)
    o_list = [uo_dict[value] for value in uo_dict]
    return o_list

def _income_to_int(inc_dict):
    new_dict = {}
    for k, v in inc_dict.items():
        temp_val = v
        temp_val = temp_val.split()[0]
        temp_val = temp_val.split("-")[0]
        temp_val = "".join(temp_val.split("."))
        new_dict[k] = int(temp_val)

    return new_dict