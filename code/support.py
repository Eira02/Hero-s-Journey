from csv import reader


def import_csv_layout(path):
    card_map = []
    with open(path) as map:
        level = reader(map, delimiter = ',')
        for row in level:
            card_map.append(list(row))
    
    return card_map