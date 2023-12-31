from unittest import expectedFailure
from unittest.mock import MagicMock, Mock, call, patch
from mod_utils import *
import mod_utils
import sqlparse
from pathlib import Path

import unittest

class TestUtils(unittest.TestCase):
    
    #Test that the clean_user_input function is turning a string into a list
    def test_clean_user_input_turn_string_into_list(self):
        input_string = "item1,item2,item3"
        expected_output = ['item1', 'item2', 'item3']

        self.assertEqual(clean_user_input(input_string),expected_output)
        
        
    #test that the clean_user_input function is stripping the input string
    def test_clean_user_input_test_strip(self):
        input_string = "   item1  ,  item2   ,   item3   "
        expected_output = ['item1', 'item2', 'item3']

        self.assertEqual(clean_user_input(input_string),expected_output)

    def test_clean_user_input_integer_input(self):
        self.assertRaises(ValueError, clean_user_input, 12345)

    def test_clean_user_input_none_input(self):
        self.assertRaises(ValueError, clean_user_input, None)

    def test_clean_user_input_empty_string(self):
        self.assertRaises(ValueError, clean_user_input,"   ")


    def test_select_date_return_something(self):
        mock_start_date = MagicMock()
        mock_end_date = MagicMock()

        mock_start_date.get_date.return_value = '2021-01-01'
        mock_end_date.get_date.return_value = '2021-12-31'

        result = select_date(mock_start_date, mock_end_date)
        self.assertIsNotNone(result)
        

    #check if the select_date function returns a tuple
    def test_select_date_return_tuple(self):
        mock_start_date = MagicMock()
        mock_end_date = MagicMock()

        mock_start_date.get_date.return_value = '2021-01-01'
        mock_end_date.get_date.return_value = '2021-12-31'

        result = select_date(mock_start_date, mock_end_date)
        self.assertIsInstance(result, tuple)


    #check if the select_date function returns 2 results
    def test_select_date_return_two_results(self):
        mock_start_date = MagicMock()
        mock_end_date = MagicMock()

        mock_start_date.get_date.return_value = '2021-01-01'
        mock_end_date.get_date.return_value = '2021-12-31'

        result = select_date(mock_start_date, mock_end_date)
        self.assertEqual(len(result), 2)
        
    
    #check if the select_date function check if start_date.get_date gets called once
    def test_select_date_start_get_date_called(self):
        mock_start_date = MagicMock()
        mock_end_date = MagicMock()

        mock_start_date.get_date.return_value = '2021-01-01'
        mock_end_date.get_date.return_value = '2021-12-31'

        select_date(mock_start_date, mock_end_date)
        
        mock_start_date.get_date.assert_called_once()


    #check if the select_date function check if end_date.get_date gets called once
    def test_select_date_end_get_date_called(self):
        mock_start_date = MagicMock()
        mock_end_date = MagicMock()

        mock_start_date.get_date.return_value = '2021-01-01'
        mock_end_date.get_date.return_value = '2021-12-31'

        select_date(mock_start_date, mock_end_date)

        mock_end_date.get_date.assert_called_once()


    @expectedFailure
    def test_select_date_future_dates(self):
        self.mock_start_date = MagicMock()
        self.mock_end_date = MagicMock()

        """Test if the function handles future dates properly."""
        self.mock_start_date.get_date.return_value = '3023-01-01'
        self.mock_end_date.get_date.return_value = '3023-12-31'

        with self.assertRaises(ValueError):
            select_date(self.mock_start_date, self.mock_end_date)

    @expectedFailure
    def test_select_date_dates_not_in_database(self):
        """Test if the function handles dates not present in the database properly."""
        self.mock_start_date.get_date.return_value = '1999-01-01'  # Assuming this date is not in your database
        self.mock_end_date.get_date.return_value = '1999-12-31'

        with self.assertRaises(ValueError):
            select_date(self.mock_start_date, self.mock_end_date)

    def test_make_window(self):
        mock_center_screen = MagicMock
        window = MagicMock

        mock_center_screen.return_value = (window, 626, 932)
        mock_window = make_window(mock_center_screen)

        self.assertIsInstance(mock_window, Tk)

    @patch('mod_utils.sqlite3.connect')
    def test_run_create_db(self, mock_connect):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()

        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        mod_utils.run_create_db()
        mock_connect.assert_called_once_with('data.db')
        mock_connection.cursor.assert_called_once()

        expected_calls = [
            call("CREATE TABLE IF NOT EXISTS reviewsDec(listing_id,id,date,reviewer_id,reviewer_name,comments)"),
            call("CREATE TABLE IF NOT EXISTS calendarDec(listing_id,date,available,price)")
        ]
        mock_cursor.execute.assert_has_calls(expected_calls)
        self.assertEqual(mock_cursor.execute.call_count, 2, "Execute method call count mismatch")

    @patch('mod_utils.sqlite3.connect')
    @expectedFailure
    def test_run_create_db_failure(self, mock_connect):

        mock_connection = MagicMock()
        mock_cursor = MagicMock()

        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        mod_utils.run_create_db()
        mock_connect.assert_called_once_with('data.db')
        mock_connection.cursor.assert_called_once()

        # Wrong SQL queries to induce an assertion failure
        expected_failure_calls = [
            call("CREATE TABLE IF NOT EXISTS WrongTable(listing_id,id,date,reviewer_id,reviewer_name,comments)"),
            call("CREATE TABLE IF NOT EXISTS calendarDec(listing_id,date,available,price)")
        ]
        mock_cursor.execute.assert_has_calls(expected_failure_calls, any_order=True)
        self.assertEqual(mock_cursor.execute.call_count, 2, "Execute method call count mismatch")


    def test_close(self):
        mock = MagicMock()
        close(mock)
        self.assertTrue(mock.destroy.called)
        self.assertEqual(mock.destroy.call_count, 1)

    def test_close_not_called(self):
        mock = MagicMock()
        # Do not call close(mock)
        # close(mock)

        self.assertFalse(mock.destroy.called, "Destroy method was not expected to be called but was called")

    def test_close_called_multiple_times(self):
        mock = MagicMock()
        close(mock)
        close(mock)  # called twice

        self.assertNotEqual(mock.destroy.call_count, 1,
                            "Destroy method was expected to be called once but was called multiple times")


    def test_load_images(self):
        mock_PhotoImage = MagicMock()
        mock_relative_to_assets = MagicMock(side_effect=lambda x: f"mocked_path/{x}")

        result = load_images(mock_PhotoImage, mock_relative_to_assets)

        expected_calls = [
            call("mocked_path/welcome_img.png"),
            call("mocked_path/home.png"),
            call("mocked_path/display_price_distribution.png"),
            call("mocked_path/display.png"),
            call("mocked_path/display_chart.png"),
            call("mocked_path/display_list.png"),
            call("mocked_path/cleanliness.png"),
            call("mocked_path/display_by_ratings.png"),
            call("mocked_path/search.png"),
            call("mocked_path/suburb_listing.png"),
            call("mocked_path/price_chart.png"),
            call("mocked_path/display_listings_for_suburb_img.png"),
            call("mocked_path/display_chart_by_cleanliness.png"),
            call("mocked_path/display_listings_by_ratings.png"),
            call("mocked_path/Display_Search_Records.png"),
            call("mocked_path/entry_4.png")
        ]
        self.assertEqual(mock_PhotoImage.call_args_list, expected_calls,
                         "PhotoImage was not called with expected arguments")
        self.assertTrue(all(isinstance(key, str) and isinstance(value, MagicMock) for key, value in result.items()))

    def test_get_price_chart_data(self):
        mock_select_date_func = Mock(return_value=('2022-01-01', '2022-12-31'))
        mock_connection = MagicMock()
        mock_execute_query = Mock(return_value=[('name', 100, '2022-01-01')])
        mock_display_func = Mock()

        get_price_chart_data('2022-01-01', '2022-12-31', 'TestSuburb', mock_select_date_func, mock_connection,
                             mock_execute_query, mock_display_func)

        self.assertEqual(mock_select_date_func.call_args, call('2022-01-01', '2022-12-31'))
        self.assertEqual(mock_execute_query.call_count, 1)
        self.assertEqual(mock_display_func.call_args, call([100], 'TestSuburb', ['name'], ['2022-01-01']))

    @patch("mod_utils.ASSETS_PATH", Path("/your/mock/path"))
    def test_relative_to_assets(self):
        given_path = "some/file/path.txt"
        result = relative_to_assets(given_path)
        expected_result = Path("/your/mock/path/some/file/path.txt")
        self.assertEqual(result, expected_result)

    @patch("mod_utils.ASSETS_PATH", Path("/your/mock/path"))
    @expectedFailure
    def test_relative_to_assets_expected_failure(self):
        given_path = "some/file/path.txt"
        result = mod_utils.relative_to_assets(given_path)
        expected_result = Path("/wrong/expected/path/some/file/path.txt")  # Intentionally set the wrong expected result
        self.assertEqual(result, expected_result)

    @expectedFailure
    @patch('mod_utils.sqlite3.connect')
    def test_connect_to_db(self, mock_connect):
        mock_connect.return_value = None

        result = mod_utils.connect_to_db()

        self.assertIsNotNone(result)
        # Assert that connect was called once
        mock_connect.assert_called_once_with('data.db')

    @patch('mod_utils.pd.read_csv')
    def test_successful_file_read(self, mock_read_csv):
        mock_df = MagicMock(spec=pd.DataFrame)
        mock_read_csv.return_value = mock_df

        df_listings, df_reviews, df_calendar = mod_utils.read_csv_files()

        # Checking that read_csv was called three times (for each file)
        self.assertEqual(mock_read_csv.call_count, 3, "Expected read_csv to have been called three times")

        # Asserting that each returned value is an instance of DataFrame (or Mock in this case)
        self.assertIsInstance(df_listings, MagicMock, "Expected df_listings to be a DataFrame")
        self.assertIsInstance(df_reviews, MagicMock, "Expected df_reviews to be a DataFrame")
        self.assertIsInstance(df_calendar, MagicMock, "Expected df_calendar to be a DataFrame")

    @patch('mod_utils.pd.read_csv')
    def test_file_not_found(self, mock_read_csv):
        mock_read_csv.side_effect = FileNotFoundError("Sample error message")

        # Now when calling read_csv_files, it should handle FileNotFoundError and return None, None, None
        df_listings, df_reviews, df_calendar = mod_utils.read_csv_files()

        # Check that None is returned for each dataframe when FileNotFoundError is raised
        self.assertIsNone(None, "Expected df_listings to be None when file is not found")
        self.assertIsNone(None, "Expected df_reviews to be None when file is not found")
        self.assertIsNone(None, "Expected df_calendar to be None when file is not found")

    @expectedFailure
    @patch("pandas.read_csv")
    def test_empty_or_corrupted_file(self, mock_read_csv):
        # Mocking the behavior of pd.read_csv to raise EmptyDataError for empty/corrupted file
        mock_read_csv.side_effect = [pd.read_csv('../bnb_data/listings_dec18.csv', low_memory=False),
                                     pd.errors.EmptyDataError("File is empty or corrupted"),
                                     pd.read_csv('../bnb_data/calendar_dec18.csv', low_memory=False)]

        # Calling the function; expecting it to handle EmptyDataError properly
        df_listings, df_reviews, df_calendar = mod_utils.read_csv_files()

        # Checking that appropriate action was taken for empty/corrupted file (e.g., df_reviews should be None)
        self.assertIsNotNone(df_listings, "Expected df_listings not to be None when file is valid")
        self.assertIsNone(df_reviews, "Expected df_reviews to be None when file is empty or corrupted")
        self.assertIsNotNone(df_calendar, "Expected df_calendar not to be None when file is valid")

    def test_sql_syntax(self):
        try:
            sqlparse.parse(SUBURB_LISTING_SHORTQUERY)
        except sqlparse.exceptions.SQLParseError:
            self.fail("SQL Syntax is invalid")

    @expectedFailure
    def test_sql_syntax_failure(self):
        bad_sql_query = "SELECT * FROM something WHERE foo = 'bar"
        with self.assertRaises(sqlparse.exceptions.SQLParseError):
            sqlparse.parse(bad_sql_query)

    @patch('mod_utils.time.time')
    def test_throttle_click(self, mock_time):
        mod_utils.last_click_time = 0  # reset last_click_time

        # Case 1: Enough time has passed since the last click
        mock_time.return_value = 2  # Simulating that the current time is 2 seconds since epoch
        result = mod_utils.throttle_click()
        self.assertTrue(result)  # Asserting that throttle_click returns True

        # Case 2: Clicking too fast
        mock_time.return_value = 2.5  # Not enough time has passed since the last click
        result = mod_utils.throttle_click()
        self.assertFalse(result)  # Asserting that throttle_click returns False

        # Case 3: Enough time has passed again
        mock_time.return_value = 4  # Enough time has passed since the last click
        result = mod_utils.throttle_click()
        self.assertTrue(result)  # Asserting that throttle_click returns True
