"""
building a basic calendar application
"""

from time import sleep, strftime
from datetime import datetime

name = "Benny"
calendar = {}

def welcome():
    print("Welcome, " + name)
    print("Calendar starting...")
    sleep(1)
    print("Today is: " + strftime("%A %B %d, %Y"))
    print("Current time is: " + strftime("%H:%M:%S"))
    sleep(1)
    print("What would you like to do?")

def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%m/%d/%Y')
        return True
    except ValueError:
        return False

def add_event(date, event):
    if validate_date(date) and int(date[6:]) >= int(strftime("%Y")):
        calendar[date] = event
        return "Event has been successfully added"
    else:
        return "Invalid date entered"

def update_event(date, update):
    if validate_date(date):
        calendar[date] = update
        return "Calendar has been updated successfully"
    else:
        return "Invalid date format. Please use MM/DD/YYYY."

def view_calendar():
    if not calendar:
        return "Calendar is empty"
    else:
        return calendar

def delete_event(event):
    dates_to_delete = [date for date, evt in calendar.items() if evt == event]
    if dates_to_delete:
        for date in dates_to_delete:
            del calendar[date]
        return "Event successfully deleted"
    else:
        return "Incorrect event specified"

def start_calendar():
    welcome()
    start = True

    while start:
        user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit: ").strip().upper()

        if user_choice == "V":
            print(view_calendar())
        elif user_choice == "U":
            date = input("What date? (MM/DD/YYYY): ").strip()
            update = input("Enter the update: ").strip()
            print(update_event(date, update))
        elif user_choice == "A":
            event = input("Enter event: ").strip()
            date = input("Enter date (MM/DD/YYYY): ").strip()
            print(add_event(date, event))
        elif user_choice == "D":
            event = input("What event? ").strip()
            print(delete_event(event))
        elif user_choice == "X":
            start = False
        else:
            print("Invalid option entered")
            start = False

if __name__ == "__main__":
    start_calendar()