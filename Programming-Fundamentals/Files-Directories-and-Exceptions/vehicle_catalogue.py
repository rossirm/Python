class Vehicle:
    def __init__(self, v_type, model, color, hp):
        self.v_type = v_type
        self.model = model
        self.color = color
        self.hp = hp

    def print_data(self):
        return f'Type: {self.v_type}\n' \
               f'Model: {self.model}\n' \
               f'Color: {self.color}\n' \
               f'Horsepower: {self.hp}\n'


def fill_catalog():
    catalog = {}
    line = input()
    while line != 'End':
        v_t, m, c, h_p = line.split(' ')
        catalog[m] = Vehicle(v_t[:1].upper() + v_t[1:].lower(), m, c, int(h_p))
        line = input()
    return catalog


def print_data(catalog):
    result = ''
    model = input()
    while model != 'Close the Catalogue':
        if model in catalog:
            result += f'{catalog[model].print_data()}'
        model = input()

    car_avg = [v.hp for v in catalog.values() if v.v_type.lower() == 'car']
    truck_avg = [v.hp for v in catalog.values() if v.v_type.lower() == 'truck']
    result += f'Cars have average horsepower of: {0.00 if not car_avg else (sum(car_avg) / len(car_avg)):.2f}.\n' \
              f'Trucks have average horsepower of: {0.00 if not truck_avg else (sum(truck_avg) / len(truck_avg)):.2f}.'
    return result


models = fill_catalog()
print(print_data(models))
