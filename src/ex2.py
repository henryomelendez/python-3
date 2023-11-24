import csv


def find_total_visits():
    files = ["week-1.csv", "week-2.csv", "week-3.csv"]
    total_visit = 0

    for file_name in files:
        with open(f"../files/{file_name}", 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                total_visit += sum(int(val) for val in row[1:])
    return  total_visit

def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()