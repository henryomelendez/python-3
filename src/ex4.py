import boto3
from botocore.exceptions import ClientError

def calculate():
    calulations = []

    while True:
        first_number = input("Enter first number (or 'q' to quit): ")
        if first_number.lower() == 'q':
            break
        second_number = input("Enter Second Number: ")
        try:
            sum = int(first_number) + int(second_number)
            calculation = f"{first_number} + {second_number} = {sum}"
            print(calculation)
            calulations.append(calculation)
        except ValueError:
            print("Invalid Input Please Enter Numbers.")
    student_id = "f9xxxxxx"
    file_name = f"calculator-log-{student_id}.txt"
    with open(file_name, 'w') as file:
        file.write('\n'.join(calulations))
    s3 = boto3.resource('s3')
    bucket_name = 'your-bucket-name'
    s3.meta.client.upload_file(file_name, bucket_name, file_name)
    print("**** Uploaded to S3 ****")

def ex4():
    calculate()

ex4()
