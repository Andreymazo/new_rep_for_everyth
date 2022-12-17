import csv
class ReadItems:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        # print('enter exist')
        self.items = open(self.path, self.mode)
        return self.items

        # return self

    def __exit__(self, exc_type, exc_val, traceback):
        # print('exit exist')
        self.items.close()


def show_items(file):
    result = {}
    with ReadItems(file, 'r') as f:#Nado opredelit slovarem items
        reader = csv.DictReader(f)
        for row in reader:
            for column, value in row.items():
                result[column] = value
            print(result)

show_items('items.csv')

# вывод в консоль
# {'name': 'Phone', 'price': '100', 'quantity': '1'}
# {'name': 'Laptop', 'price': '1000', 'quantity': '3'}
# {'name': 'Cable', 'price': '10', 'quantity': '5'}
# {'name': 'Mouse', 'price': '50', 'quantity': '5'}
# {'name': 'Keyboard', 'price': '74.90', 'quantity': '5'}