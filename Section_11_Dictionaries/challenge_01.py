
vehicle = {
    'model': 'FRV',
    'make': 'Honda',
    'year': 2007,
    'mileage': 215000
}

print(vehicle['year'])

vehicle['year'] = 2022
print(vehicle['year'])

vehicle['type'] = 'car'
print(vehicle)

vehicle.pop('make')
print(vehicle)
