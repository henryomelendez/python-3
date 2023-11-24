from pprint import pprint


def build_car_list():
    mileage_data = {}

    with open('../files/input.txt', 'r') as file:
        next(file)
        for line in file:
            parts = line.strip().split(',')
            car_id, mileage = int(parts[0].strip()), parts[1].strip()

            if mileage.isdigit():
                mileage_data[car_id] = int(mileage)

    car_model = {}
    with open("../files/car-ids.txt", 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            car_id, model = int(parts[0].strip()), parts[1].strip()
            car_model[car_id] = model

    car_list = []
    for car_id, miles in mileage_data.items():
        if car_id in car_model:
            car_list.append({'id': car_id, 'miles': miles, 'model': car_model[car_id]})

    return car_list


def ex5():
    car_list = build_car_list()
    pprint(car_list)


ex5()
