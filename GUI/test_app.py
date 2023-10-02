import io  # don't forget to import io
import pandas as pd  # don't forget to import pandas
import pytest
from unittest.mock import MagicMock, patch, ANY, call
from unittest import mock
import unittest
import createDatabase as db
import tkinter as tk
import sqlite3
from unittest import TestCase


# Sample CSV data as string
listings_csv = """listing_id,column2,column3,column4
1,val1,val2,val3
2,val1,val2,val3"""

reviews_csv = """listing_id,id,date,reviewer_id,reviewer_name,comments
1,1,2023-10-01,1,John,Good
2,2,2023-10-01,2,Alice,Excellent"""

calendar_csv = """listing_id,date,available,price
1,2023-10-01,true,100
2,2023-10-01,false,200"""

mocked_df_listings = pd.read_csv(io.StringIO(listings_csv))
mocked_df_reviews = pd.read_csv(io.StringIO(reviews_csv))
mocked_df_calendar = pd.read_csv(io.StringIO(calendar_csv))


# Test case for the get_the_data function
@patch("pandas.read_csv")
def test_get_the_data(mock_read_csv):
    mock_read_csv.side_effect = [mocked_df_listings, mocked_df_reviews, mocked_df_calendar]

    # Mock the SQLite cursor and connection
    mock_cursor = MagicMock()
    mock_connection = MagicMock()

    # Mock the Tkinter root and Text widget
    mock_root = MagicMock()
    mock_output_text = MagicMock()

    # Call the function with the mocks
    db.get_the_data(mock_cursor, mock_connection, mock_root, mock_output_text)

    # Assertions to check the behavior of the function
    mock_cursor.execute.assert_any_call("CREATE TABLE IF NOT EXISTS listingsDec (listing_id,column2,column3,column4)")
    mock_cursor.execute.assert_any_call(ANY,
                                        ANY)

    # Ensure the commit method was called on the connection
    assert mock_connection.commit.call_count == 3

    # Ensure the Tkinter Text widget received the correct strings to insert
    expected_insert_calls = [
        call('end', 'Database Created Successfully!\n'),
        call('end', 'You can now close this window.\n')

        # ...Add more calls for other expected insertions
    ]
    mock_output_text.insert.assert_has_calls(expected_insert_calls, any_order=True)  # Adjust any_order as needed

    # Ensure the Tkinter root's update_idletasks method was called (if you want to test this)
    assert mock_root.update_idletasks.called


@patch("pandas.read_csv")
def test_file_not_found(mock_read_csv):
    mock_read_csv.side_effect = FileNotFoundError('Test error: file not found')

    mock_cursor = MagicMock()
    mock_connection = MagicMock()
    mock_root = MagicMock()
    mock_output_text = MagicMock()

    # Call the function with mocks
    db.get_the_data(mock_cursor, mock_connection, mock_root, mock_output_text)

    # Add assertions to check how the function handles the error


@patch("pandas.read_csv")
def test_empty_dataframes(mock_read_csv):
    empty_df = pd.DataFrame()
    mock_read_csv.return_value = empty_df

    mock_cursor = MagicMock()
    mock_connection = MagicMock()
    mock_root = MagicMock()
    mock_output_text = MagicMock()

    db.get_the_data(mock_cursor, mock_connection, mock_root, mock_output_text)

    # Add assertions to check how the function handles empty data
@patch("sqlite3.connect")
def test_database_error_on_execute(mock_connect):
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_connect.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor
    mock_root = MagicMock()
    mock_output_text = MagicMock()

    # Simulate a database error when calling the execute method on the cursor
    mock_cursor.execute.side_effect = sqlite3.OperationalError('Test database error')

    # Call the function with mocks
    db.get_the_data(mock_cursor, mock_connection, mock_root, mock_output_text)

    # Add assertions to check how the function handles the database error
    # For example, check if the error message is displayed in the Tkinter Text widget
    mock_output_text.insert.assert_called_with('end', 'Database error occurred.\n')


class TestRunCreateDb(unittest.TestCase):
    @patch('createDatabase.sqlite3')
    @patch('createDatabase.show_app')
    def test_run_create_db(self, mock_show_app, mock_sqlite3):
        # Set up the mock objects
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_sqlite3.connect.return_value.__enter__.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        # Call the function
        db.run_create_db()

        # Check if connect was called with the correct argument
        mock_sqlite3.connect.assert_called_once_with('data.db')

        # Check if execute was called with the correct arguments
        expected_calls = [
            call("CREATE TABLE IF NOT EXISTS reviewsDec(listing_id,id,date,reviewer_id,reviewer_name,comments)"),
            call("CREATE TABLE IF NOT EXISTS calendarDec(listing_id,date,available,price)")
        ]
        mock_cursor.execute.assert_has_calls(expected_calls, any_order=True)

        # Check if show_app was called with the correct arguments
        mock_show_app.assert_called_once_with(mock_cursor, mock_connection)

@patch('createDatabase.get_the_data')
@patch('tkinter.Text')
@patch('tkinter.Tk')
def test_get_data(mock_tk, mock_text, mock_get_data):
    # Setup
    mock_cursor = MagicMock()
    mock_connection = MagicMock()
    db.root = mock_tk
    db.output_text = mock_text

    # Call the function
    db.get_data(db.root, mock_cursor, mock_connection)

    # Assert
    mock_text.insert.assert_has_calls([call(tk.END, "Creating Database...\n"), call(tk.END, "Please wait...\n")])
    mock_tk.update_idletasks.assert_called_once()
    mock_get_data.assert_called_once()  # add appropriate arguments


def test_close():
    mock = MagicMock()
    db.close(mock)
    mock.destroy.assert_called_once()

@patch('createDatabase.get_data')
@patch('createDatabase.close')
@patch('tkinter.Tk')
def test_show_app(mock_tk, mock_close, mock_get_data):
    mock_cursor = MagicMock()
    mock_connection = MagicMock()
    db.show_app(mock_cursor, mock_connection)
    # Add assertions and other testing logic here


@pytest.fixture
def mock_sqlite3_connect():
    with mock.patch('createDatabase.sqlite3.connect') as mock_connect:
        yield mock_connect

@pytest.fixture
def mock_show_app():
    with mock.patch('createDatabase.show_app') as mock_func:
        yield mock_func


def test_run_create_db(mock_sqlite3_connect, mock_show_app):
    mock_connection = mock_sqlite3_connect.return_value.__enter__.return_value

    # Call the function
    db.run_create_db()

    # Assert the expected calls were made
    mock_connection.cursor.assert_called_once()
    mock_show_app.assert_called_once_with(mock_connection.cursor.return_value, mock_connection)

