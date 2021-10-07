import csv
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt


def input_vitals():
    date = input("What day is it? Please enter in yyyy-mm-dd format: \n")
    time = input("What time did you take the reading? ex. 1:34PM: \n")
    temp = input("What was their temperature? ex. 98.6: \n")
    spo2 = input("What was their SpO2 reading?: \n")
    meds = input("Did you give them any meds or treatments?: \n")
    extra_notes = input("Any notes you would like to add?: \n")
    add_vitals(date, time, temp, spo2, meds, extra_notes)


def add_vitals(date, time, temp, spo2, meds, extra_notes):
    timestamp = date + ' ' + time
    new_vitals = (date, time, timestamp, temp, spo2, meds, extra_notes)
    with open("Isaac_Data.csv", 'a+', newline='\n') as write_obj:
        writer = csv.writer(write_obj)
        writer.writerow(new_vitals)
    return True


def scatter_time():
    data = pandas.read_csv("Isaac_Data.csv", parse_dates=['Timestamp'])
    time_of_day = data['Timestamp']
    temperature = data['Temperature']
    o2 = data['SpO2']
    treatments = data['Medicine/Treatments Given']
    notes = data['Notes']
    plt.scatter(time_of_day, temperature, alpha=0.5)
    plt.title("Isaac's Temperature Visualized")
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.show()


class Main:
    while True:
        print("Welcome to the Sick Kids Tracker: ")
        print("\n 1. Input New Vitals \n 2. Show Chart \n 3. Quit Program \n")
        input1 = input('Please Select a Menu Option: ')

        if input1 == '1':
            input_vitals()

        elif input1 == '2':
            scatter_time()

        elif input1 == '3':
            print('Exiting Program, bye! \n')
            break

