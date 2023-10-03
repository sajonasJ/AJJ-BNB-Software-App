import pytest
from unittest.mock import MagicMock, Mock, call
from mod_utils import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Label, StringVar, Toplevel, CENTER, VERTICAL, \
    HORIZONTAL, BOTH, END, TOP
from mod_constants import *
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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
        
    
    #check that the select_date function returns something
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
   
def test_show_chart():
    mock_tk = MagicMock()
    mock_Frame = MagicMock()
    mock_FigureCanvasTkAgg = MagicMock()
    mock_center_screen = MagicMock()

    mock_fig = MagicMock()
    title = "Test Title"

    show_chart(mock_fig, title, tk=mock_tk, Frame=mock_Frame, FigureCanvasTkAgg=mock_FigureCanvasTkAgg, center_screen=mock_center_screen)

    mock_tk.Tk.assert_called_once()
    mock_Frame.assert_called_once_with(master=mock_tk.Tk())


def test_add_scrollbars_to_treeview():
    mock_window = MagicMock()
    mock_tree = MagicMock()
    mock_ttk_module = Mock()
    mock_scrollbar = Mock()
    mock_ttk_module.Scrollbar.return_value = mock_scrollbar

    width = 500
    height = 400

    add_scrollbars_to_treeview(mock_window, mock_tree, width, height, ttk_module=mock_ttk_module)

    mock_ttk_module.Scrollbar.assert_called()
    assert mock_tree.configure.call_args_list[0] == call(yscrollcommand=mock_scrollbar.set)
    assert mock_tree.configure.call_args_list[1] == call(xscrollcommand=mock_scrollbar.set)
    mock_scrollbar.place.assert_called()


def test_configure_treeview():
    # Set up
    mock_window = MagicMock()
    mock_treeview_constructor = MagicMock()
    results = [(1, "Alice", 30), (2, "Bob", 28)]
    column_names = ["ID", "Name", "Age"]
    width = 800
    height = 600

    configure_treeview(mock_window, results, column_names, width, height, treeview_constructor=mock_treeview_constructor)

    # Verify
    mock_treeview_constructor.assert_called_once_with(mock_window, columns=column_names, show='headings')



def test_create_new_window():
    # Set up
    mock_toplevel_constructor = MagicMock()
    mock_parent_window = MagicMock()
    mock_center_func = MagicMock()
    suburb = "TestSuburb"
    width = 800
    height = 600

    # Exercise
    create_new_window(suburb, width, height, toplevel_constructor=mock_toplevel_constructor, parent_window=mock_parent_window, center_func=mock_center_func)

    # Verify
    mock_toplevel_constructor.assert_called_once_with(mock_parent_window)
    mock_center_func.assert_called_once_with(mock_toplevel_constructor.return_value, width, height)
    # ... any other assertions needed


def test_calculate_initial_size():
    # Set up
    mock_window = MagicMock()
    mock_window.winfo_screenwidth.return_value = 1200
    mock_window.winfo_screenheight.return_value = 800
    max_width = 1000
    max_height = 700

    # Exercise
    width, height = calculate_initial_size(mock_window, max_width, max_height)

    # Verify
    mock_window.winfo_screenwidth.assert_called_once()
    mock_window.winfo_screenheight.assert_called_once()
    assert width == 1000  # screen_width is 1200 but max_width is 1000
    assert height == 700  #


def test_make_window():
    # Set up
    mock_window = MagicMock()
    window_title = "Test Window"
    bg_color = "#FFFFFF"
    window_height = 600
    window_width = 900

    # Define a lambda or function to pass as center_func
    center_func = lambda win, width, height: center_screen(win, width, height, 1920, 1080)

    # Exercise
    result = make_window(mock_window, window_title, bg_color, window_height, window_width, center_func)

    # Your assertions here


def test_center_screen():
    # Set up
    mock_window = MagicMock()
    window_width = 800
    window_height = 600
    screen_width = 1920
    screen_height = 1080

    # Exercise
    center_screen(mock_window, window_width, window_height, screen_width, screen_height)

    # Verify
    expected_geometry = f"{window_width}x{window_height}+560+240"
    mock_window.geometry.assert_called_once_with(expected_geometry)


def test_display_error_message(capsys):
    error = "Test error"
    expected_output = "display error messageTest error\n"

    display_error_message(error)

    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_clear_search_query(capsys):
    expected_output = "clear search fields\n"

    clear_search_query()

    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_on_hover_ratings():
    # Set up
    mock_annotation = MagicMock()
    mock_selection = MagicMock()
    mock_selection.index = 1
    mock_selection.annotation = mock_annotation
    scores = [3.5, 4.5]
    names = ["Place1", "Place2"]
    expected_output = 'Rating: 4.5\nPlace Name: Place2'

    # Exercise
    on_hover_ratings(mock_selection, scores, names)

    # Verify
    mock_annotation.set_text.assert_called_once_with(expected_output)


def test_on_hover():
    class MockSel:
        def __init__(self):
            self.index = 1
            self.annotation = MagicMock()

    sel = MockSel()
    the_prices = [100, 200]
    the_names = ['Name1', 'Name2']
    the_dates = ['Date1', 'Date2']

    on_hover(sel, the_prices, the_names, the_dates)
    sel.annotation.set_text.assert_called_once_with('Price: 200\nName:Name2\nDate: Date2')
