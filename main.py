import csv
import pandas
import sqlite3
from tkinter import *
from database import *
import matplotlib.pyplot as plt


# Creating the main tkinter window for the app to run
window = Tk()
window.title("Kids' Illness Tracker")

# This large section is setting up the labels and text entry fields to capture input
child_labeltext = StringVar()
child_labeltext.set("Which kid is this for?")
child_label = Label(window, textvariable=child_labeltext, height=4)
child_label.grid(row=1, column=1)
child_value = StringVar()
child_field = Entry(window, textvariable=child_value)
child_field.grid(row=1, column=2)

date_labeltext = StringVar()
date_labeltext.set("Enter the date in yyyy-mm-dd format")
date_label = Label(window, textvariable=date_labeltext, height=4)
date_label.grid(row=3, column=1)
date_value = StringVar()
date_field = Entry(window, textvariable=date_value)
date_field.grid(row=3, column=2)

time_labeltext = StringVar()
time_labeltext.set("Enter the time in HH:MMam format")
time_label = Label(window, textvariable=time_labeltext, height=4)
time_label.grid(row=5, column=1)
time_value = StringVar()
time_field = Entry(window, textvariable=time_value)
time_field.grid(row=5, column=2)

temp_labeltext = StringVar()
temp_labeltext.set("Enter the temperature")
temp_label = Label(window, textvariable=temp_labeltext, height=4)
temp_label.grid(row=7, column=1)
temp_value = StringVar()
temp_field = Entry(window, textvariable=temp_value)
temp_field.grid(row=7, column=2)

spo2_labeltext = StringVar()
spo2_labeltext.set("Enter the SpO2")
spo2_label = Label(window, textvariable=spo2_labeltext, height=4)
spo2_label.grid(row=9, column=1)
spo2_value = StringVar()
spo2_field = Entry(window, textvariable=spo2_value)
spo2_field.grid(row=9, column=2)

meds_labeltext = StringVar()
meds_labeltext.set("Any meds or treatments?")
meds_label = Label(window, textvariable=meds_labeltext, height=4)
meds_label.grid(row=11, column=1)
meds_value = StringVar()
meds_field = Entry(window, textvariable=meds_value)
meds_field.grid(row=11, column=2)

notes_labeltext = StringVar()
notes_labeltext.set("Any other notes to add?")
notes_label = Label(window, textvariable=notes_labeltext, height=4)
notes_label.grid(row=13, column=1)
notes_value = StringVar()
notes_field = Entry(window, textvariable=notes_value)
notes_field.grid(row=13, column=2)

success_labeltext = StringVar()
success_labeltext.set("Data Successfully Added!")
success_label = Label(window, textvariable=success_labeltext, height=4)

error_labeltext = StringVar()
error_labeltext.set("Please enter either Isaac's or Oliver's Name")
error_label = Label(window, textvariable=error_labeltext, height=4)


# Capturing the data that was entered in the fields and associating each field with a variable
# So that the data can be passed into the add_vitals function and added to the spreadsheets
def input_vitals():
    kids = child_value.get()
    date = date_value.get()
    time = time_value.get()
    temp = temp_value.get()
    spo2 = spo2_value.get()
    meds = meds_value.get()
    extra_notes = notes_value.get()
    add_vitals(kids, date, time, temp, spo2, meds, extra_notes)


# Takes the data that was passed from the input_vitals function deciding which child it's for
# and inserting the inputted data into a new row on the spreadsheet
def add_vitals(kids, date, time, temp, spo2, meds, extra_notes):
    timestamp = date + ' ' + time
    new_vitals = (date, time, timestamp, temp, spo2, meds, extra_notes)

    insert(kids, timestamp, temp, spo2, meds, extra_notes)
    success_label.grid(row=13, column=1)
    # if kids.lower() == 'isaac':
    #     with open("Isaac_Data.csv", 'a+', newline='\n') as write_obj:
    #         writer = csv.writer(write_obj)
    #         writer.writerow(new_vitals)
    #     success_label.grid(row=13, column=1)
    #     return True
    # elif kids.lower() == 'oliver':
    #     with open("Oliver_Data.csv", 'a+', newline='\n') as write_obj:
    #         writer = csv.writer(write_obj)
    #         writer.writerow(new_vitals)
    #     success_label.grid(row=13, column=1)
    #     return True
    # else:
    #     error_label.grid(row=13, column=1)
    #     return False


# This uses matplotlib to take all of the data from the spreadsheet and turning it into a spreadsheet
def scatter_time():
    name = 'Isaac'
    data = view(name)
    time_of_day = []
    temperature = []
    o2 = []
    treatments = []
    notes = []
    for row in data:
        time_of_day.append(row[1])
        temperature.append(row[2])
        o2.append(row[3])
        treatments.append(row[4])
        notes.append(row[5])
    # data = pandas.read_csv("Isaac_Data.csv", parse_dates=['Timestamp'])
    # time_of_day = data['Timestamp']
    # temperature = data['Temperature']
    # o2 = data['SpO2']
    # treatments = data['Medicine/Treatments Given']
    # notes = data['Notes']
    plt.scatter(time_of_day, temperature, alpha=0.5)
    plt.title("Isaac's Temperature Visualized")
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.show()


# Creates a submit button that runs the input_vitals function
submit_button = Button(window, text="Submit", command=input_vitals)
submit_button.grid(row=15, column=2)


# Creates a Plot Vitals button that runs the scatter_time function for the scatter plot
plot_button = Button(window, text="Plot Vitals", command=scatter_time)
plot_button.grid(row=17, column=2)

# Opens the window and starts the main loop of the program
window.mainloop()


# Playing around with tkinter functionality, commenting out Main CLI loop
# In case I need to roll back to it
#
# class Main:
#     while True:
#         print("Welcome to the Sick Kids Tracker: ")
#         print("\n 1. Input New Vitals \n 2. Show Chart \n 3. Quit Program \n")
#         input1 = input('Please Select a Menu Option: ')
#
#         if input1 == '1':
#             input_vitals()
#
#         elif input1 == '2':
#             scatter_time()
#
#         elif input1 == '3':
#             print('Exiting Program, bye! \n')
#             break

