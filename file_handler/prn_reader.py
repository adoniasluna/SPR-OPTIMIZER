def get_experimental_table(path):
    table = []
    file = open(path, 'r', encoding='utf8', errors="ignore")
    lines = file.readlines()

    for i in range(1, len(lines)):
        angle, reflectance, _, _, _ = (float(s) for s in lines[i].split())
        if angle > 42.2:
            table.append([angle, reflectance])

    return table


def get_normalized_experimental_table(path):
    table_normalized = get_experimental_table(path)
    biggest_reflectance = table_normalized[0][1]

    for i in range(1, len(table_normalized)):
        if table_normalized[i][1] > biggest_reflectance:
            biggest_reflectance = table_normalized[i][1]

    for i in range(len(table_normalized)):
        table_normalized[i][1] = table_normalized[i][1] / biggest_reflectance

    return table_normalized
