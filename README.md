# Basic Calendar Application

This is a simple command-line calendar application written in Python. It allows users to add, update, view, and delete events from a calendar.

## Features

- **Add Event**: Add an event to the calendar with a specified date.
- **Update Event**: Update an existing event on the calendar.
- **View Calendar**: View all events in the calendar.
- **Delete Event**: Delete an event from the calendar.

## Commands

* A: Add an event
* U: Update an event
* V: View the calendar
* D: Delete an event
* X: Exit the application

## Example

```
Welcome, Benny
Calendar starting...
Today is: Monday October 02, 2023
Current time is: 14:30:00
What would you like to do?
A to Add, U to Update, V to View, D to Delete, X to Exit: A
Enter event: Meeting with team
Enter date (MM/DD/YYYY): 10/05/2023
Event has been successfully added
A to Add, U to Update, V to View, D to Delete, X to Exit: V
{'10/05/2023': 'Meeting with team'}
A to Add, U to Update, V to View, D to Delete, X to Exit: X
```

## Testing

This project uses pytest for testing. To run the tests, ensure you have pytest installed:

```
pytest test_main.py
```
