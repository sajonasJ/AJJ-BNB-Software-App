#from displays import display_suburb_listing
import unittest
from unittest.mock import patch, MagicMock


#from getData import get_suburb_listings
#import getData as gd

class TestGetSuburbListings(unittest.TestCase):

    @patch('getData.sqlite3')
    @patch('getData.display_suburb_listings')
    def test_function(self, mock_display, mock_sqlite3):
        from getData import get_suburb_listings
        from datetime import datetime
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_fetchall = MagicMock()
        mock_display.return_value = MagicMock()
        # mock_displaySuburbListing = MagicMock()
        # mock_displaySuburbListings.return_value = mock_displaySuburbListing
        mock_sqlite3.connect = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = mock_fetchall
        
        startDate = MagicMock()
        endDate = MagicMock()
        startDate.get_date.return_value = datetime(2019, 1, 1)
        endDate.get_date.return_value = datetime(2019, 1, 2)

        get_suburb_listings(startDate,endDate,'Bondi Beach', 'Short')
        #mock_display.assert_called_once()
        mock_sqlite3.connect.assert_called_once()
        mock_connection.assert_called()
        mock_display.assert_called()
        #mock_cursor.assert_any_call()
        #mock_cursor.execute.assert_called()
        #mock_connection.__enter__.assert_called_once()
        #mock_connection.assert_called_once()
        #mock_display.assert_called_once_with(2, 3)
        #print('mock display',mock_display)
        #assert(mock_display() == 'test')
    
    
'''
import unittest
from unittest.mock import patch, MagicMock
from my_module import my_function

class TestMyModule(unittest.TestCase):

    @patch('my_module.my_function', return_value=MagicMock())
    def test_my_function_with_patched_mock(self, mock_my_function):'''