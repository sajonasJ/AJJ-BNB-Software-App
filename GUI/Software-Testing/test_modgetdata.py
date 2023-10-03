# test_modgetdata.py
import pytest
from unittest.mock import patch, Mock, MagicMock
from mod_getdata import *
import sqlite3
from unittest.mock import patch
from mod_utils import *
from mod_constants import *


def test_get_price_chart_data():

    mock_select_date_func = Mock(return_value=('2022-01-01', '2022-12-31'))
    mock_connection = MagicMock()
    mock_execute_query = Mock(return_value=[('name', 100, '2022-01-01')])
    mock_display_func = Mock()


    get_price_chart_data('2022-01-01', '2022-12-31', 'TestSuburb', mock_select_date_func, mock_connection, mock_execute_query, mock_display_func)

    mock_select_date_func.assert_called_once_with('2022-01-01', '2022-12-31')
    mock_execute_query.assert_called_once()
    mock_display_func.assert_called_once_with([100], 'TestSuburb', ['name'], ['2022-01-01'])

def test_get_cleanliness_data(mocker, mock_connection):
    mocker.patch('sqlite3.connect', return_value=mock_connection)

    # Call the function with sample parameters
    keywords = ['keyword1', 'keyword2']
    suburb = 'TestSuburb'
    label3 = 'TestLabel'
    get_cleanliness_data(keywords, suburb, label3)

    mock_connection.cursor().execute.assert_called_once_with(
        CLEANLINESS_QUERY.format(like_clauses='comments LIKE ? OR comments LIKE ?'),
        (suburb, '%keyword1%', '%keyword2%')
    )

CLEANLINESS_QUERY = """
            SELECT rev.*
            FROM reviewsDec rev
            INNER JOIN listingsDec l ON rev.listing_id = l.id
            WHERE l.city = ? AND ({like_clauses})"""
@pytest.fixture
def mock_cursor(mocker):

    cursor = mocker.MagicMock()
    cursor.fetchall.return_value = [('result1',), ('result2',), ('result3',)]
    return cursor

@pytest.fixture
def mock_connection(mock_cursor, mocker):

    connection = mocker.MagicMock()
    connection.cursor.return_value = mock_cursor
    return connection

@pytest.fixture
def mock_display_cleanliness(mocker):
    """Fixture for mocking the display_cleanliness function."""
    return mocker.patch('mod_getdata.display_cleanliness', autospec=True)


def test_get_cleanliness_data(mocker):
    mock_cursor = mocker.MagicMock()
    mock_cursor.fetchall.return_value = [(1,), (2,), (3,)]
    mock_connection = mocker.MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    mock_display = mocker.patch('mod_getdata.display_cleanliness')

    keywords = ['clean']
    suburb = 'TestSuburb'
    label3 = mocker.MagicMock()

    get_cleanliness_data(keywords, suburb, label3, connection=mock_connection)

    mock_cursor.execute.assert_called_once()
    mock_cursor.fetchall.assert_called_once()
    mock_display.assert_called_once_with(len(mock_cursor.fetchall.return_value), suburb, label3)


def test_get_keyword_results(mocker):
    mock_cursor = mocker.MagicMock()
    mock_cursor.fetchall.return_value = [(1,), (2,), (3,)]
    mock_connection = mocker.MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    mock_display_func = mocker.patch(
        'mod_getdata.display_keyword_results')
    mock_clean_user_input = mocker.patch('mod_getdata.clean_user_input', return_value=['clean'])
    mock_select_date = mocker.patch('mod_getdata.select_date', return_value=('2022-01-01', '2022-12-31'))

    start_date = '2022-01-01'
    end_date = '2022-12-31'
    key_words = 'test'
    how_much_data = 'Short'

    get_keyword_results(start_date, end_date, key_words, how_much_data, connection=mock_connection,
                        display_func=mock_display_func)

    mock_cursor.execute.assert_called_once()
    mock_cursor.fetchall.assert_called_once()
    mock_display_func.assert_called_once()


def test_get_suburb_ratings(mocker):
    mock_cursor = mocker.MagicMock()
    mock_cursor.fetchall.return_value = [(1,), (2,), (3,)]
    mock_connection = mocker.MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    mock_display_records_func = mocker.patch(
        'mod_getdata.display_suburb_ratings_records')
    mock_display_chart_func = mocker.patch('mod_getdata.display_suburb_ratings_chart')

    suburb = 'TestSuburb'
    how_much_data = 'Short'
    data_type = 'Record'

    get_suburb_ratings(suburb, how_much_data, data_type, connection=mock_connection,
                       display_records_func=mock_display_records_func, display_chart_func=mock_display_chart_func)

    mock_cursor.execute.assert_called_once()
    mock_cursor.fetchall.assert_called_once()
    mock_display_records_func.assert_called_once()

