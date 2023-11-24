from ValidationException import ValidationException


def validate_file(file):
    with open(f"../files/{file}", 'r') as csv_file:
        next(csv_file)
        for row in csv_file:
            parts = row.strip().split(",")
            if len(parts) != 2:
                raise ValidationException(f"Invalid line format: {row.strip()}")
            car_id, mileage = parts
            try:
                if not mileage.strip().isdigit():
                    raise ValidationException(f"Invalid milage {mileage.strip()}")
            except ValidationException:
                raise ValidationException(f"Invalid milage: {mileage.strip()}")


def ex1():
    try:
        validate_file("input.txt")
    except ValidationException as ve:
        print(ve)


ex1()
