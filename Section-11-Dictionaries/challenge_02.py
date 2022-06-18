vehicle = {
    'model': 'FRV',
    'make': 'Honda',
    'year': 2007,
    'mileage': 215000
}

for x, y in vehicle.items():
    print(x, y)


vehicle2 = vehicle.copy()

vehicle2['number_of_tires'] = 4

for x, y in vehicle2.items():
    print(x, y)

    