from unittest.mock import MagicMock, call
from mod_displays import *


def test_initial_window():
    # Arrange
    mock_make_window_function = MagicMock(return_value="mock_window")

    # Act
    result = initial_window(mock_make_window_function)

    # Assert
    mock_make_window_function.assert_called_once()
    assert result == "mock_window"


def test_display_suburb_listings():
    # Arrange
    mock_results = [...]  # replace with your test data
    mock_column_names = [...]  # replace with your test data
    mock_suburb = "TestSuburb"
    mock_window_size = (1000, 800)
    mock_create_new_window_func = MagicMock()
    mock_configure_treeview_func = MagicMock()
    mock_add_scrollbars_func = MagicMock()

    # Act
    display_suburb_listings(
        mock_results,
        mock_column_names,
        mock_suburb,
        mock_window_size,
        mock_create_new_window_func,
        mock_configure_treeview_func,
        mock_add_scrollbars_func
    )


def test_display_keyword_results():
    # Arrange
    mock_results = [...]  # replace with your test data
    mock_column_names = [...]  # replace with your test data
    mock_keywords = "TestKeywords"
    mock_window_size = (1000, 800)
    mock_create_new_window_func = MagicMock()
    mock_configure_treeview_func = MagicMock()
    mock_add_scrollbars_func = MagicMock()

    # Act
    display_keyword_results(
        mock_results,
        mock_column_names,
        mock_keywords,
        mock_window_size,
        mock_create_new_window_func,
        mock_configure_treeview_func,
        mock_add_scrollbars_func
    )


def test_display_cleanliness():
    # Arrange
    mock_result_number = 5
    mock_suburb = "TestSuburb"
    mock_label = MagicMock()

    # Act
    result = display_cleanliness(mock_result_number, mock_suburb, mock_label)

    # Assert
    expected_text = f"The number of reviews that mention cleanliness in {mock_suburb} is: {mock_result_number}"
    mock_label.config.assert_called_once_with(text=expected_text)
    assert result == expected_text


def test_display_suburb_ratings_records():
    mock_window = MagicMock()
    mock_window.winfo_screenwidth.return_value = 1000
    mock_window.winfo_screenheight.return_value = 800
    mock_create_new_window = MagicMock()
    mock_configure_treeview = MagicMock()
    mock_add_scrollbars_to_treeview = MagicMock()
    mock_place = MagicMock()
    mock_results = MagicMock()
    mock_column_names = MagicMock()
    suburb = "TestSuburb"
    max_width = 800
    max_height = 700

    display_suburb_ratings_records(
        mock_window, mock_create_new_window, mock_configure_treeview,
        mock_add_scrollbars_to_treeview, mock_place, mock_results, mock_column_names,
        suburb, max_width, max_height
    )

    # add your assertions here
    mock_window.winfo_screenwidth.assert_called_once()
    mock_window.winfo_screenheight.assert_called_once()
    mock_create_new_window.assert_called_once_with(suburb, max_width, 800-100)


def test_display_suburb_ratings_chart():
    # Arrange
    mock_plt = MagicMock()
    mock_np = MagicMock()
    mock_mplcursors = MagicMock()
    mock_on_hover_ratings = MagicMock()
    mock_show_chart = MagicMock()
    mock_the_score = [4.5, 4.7, 5.0]
    mock_the_suburb = "TestSuburb"
    mock_the_names = ["Place1", "Place2", "Place3"]

    # Act
    display_suburb_ratings_chart(
        mock_the_score, mock_the_suburb, mock_the_names,
        plt_module=mock_plt, np_module=mock_np, mplcursors_module=mock_mplcursors,
        on_hover_ratings_func=mock_on_hover_ratings, show_chart_func=mock_show_chart)

    # Assert
    # Add your assertions here to verify the expected behavior of your function