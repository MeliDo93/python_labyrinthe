from csv import reader


def import_csv_layout(path):
    data = []
    with open(path) as map:
        d = reader(map, delimiter=',')
        for row in d:
            data.append(list(row))
        return data
