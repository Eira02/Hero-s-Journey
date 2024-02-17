from csv import reader


def import_csv_layout(path):
    """
    Import a CSV file representing the layout of a card map.

    Args:
        path (str): The file path to the CSV file.

    Returns:
        list: A list of lists representing the layout of the card map.
              Each inner list represents a row in the CSV file, and
              each element in the inner list represents a value in
              that row.
    """
    card_map = []
    with open(path) as map:
        level = reader(map, delimiter = ',')
        for row in level:
            card_map.append(list(row))
    
    return card_map