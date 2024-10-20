# test_main.py

import pytest
from main import validate_date, add_event, update_event, view_calendar, delete_event

@pytest.fixture
def test_validate_date():
    assert validate_date("12/31/2023") == True
    assert validate_date("02/29/2020") == True  # Leap year
    assert validate_date("02/30/2020") == False  # Invalid date
    assert validate_date("13/01/2020") == False  # Invalid month
    assert validate_date("12/31/20") == False  # Invalid year format

def test_add_event():
    assert add_event("12/31/2023", "New Year Party") == "Event has been successfully added"
    assert add_event("02/30/2020", "Invalid Date Event") == "Invalid date entered"

def test_update_event():
    add_event("12/31/2023", "New Year Party")
    assert update_event("12/31/2023", "Updated Party") == "Calendar has been updated successfully"
    assert update_event("02/30/2020", "Invalid Date Update") == "Invalid date format. Please use MM/DD/YYYY."

def test_view_calendar():
    assert view_calendar() == "Calendar is empty"
    add_event("12/31/2023", "New Year Party")
    assert view_calendar() == {"12/31/2023": "New Year Party"}

def test_delete_event():
    add_event("12/31/2023", "New Year Party")
    assert delete_event("New Year Party") == "Event successfully deleted"
    assert delete_event("Nonexistent Event") == "Incorrect event specified"