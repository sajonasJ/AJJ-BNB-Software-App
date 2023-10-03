from unittest.mock import MagicMock, patch, call
from mod_widgets import *
from mod_widgets import relative_to_assets, ASSETS_PATH
import pytest
from pathlib import Path


def test_create_canvas():
    mock_window = MagicMock()
    mock_canvas_class = MagicMock()
    mock_create_button = MagicMock()
    mock_img = {
        'home_image': MagicMock(),
        'suburb_listing_image': MagicMock(),
        'price_chart_image': MagicMock(),
        'search_image': MagicMock(),
        'cleanliness_image': MagicMock(),
        'display_ratings_image': MagicMock()
    }

    show_suburb = MagicMock()
    show_cleanliness = MagicMock()
    show_price = MagicMock()
    show_search = MagicMock()
    show_listings = MagicMock()

    canvas = create_canvas(
        mock_window, mock_canvas_class, mock_create_button, mock_img,
        show_suburb, show_cleanliness, show_price, show_search, show_listings
    )

    mock_canvas_class.assert_called_once_with(
        mock_window, bg="#E8E8E8", height=626, width=932, bd=0, highlightthickness=0, relief="ridge"
    )


def test_create_button():
    MockButtonClass = MagicMock()
    mock_image = MagicMock()
    mock_command = MagicMock()
    x, y, w, h = 10, 20, 30, 40

    button = create_button(MockButtonClass, mock_image, mock_command, x, y, w, h)

    MockButtonClass.assert_called_once_with(image=mock_image, borderwidth=0, highlightthickness=0, command=mock_command, relief="flat")
    button.place.assert_called_once_with(x=x, y=y, width=w, height=h)


@patch('modwidgets.PhotoImage')
def test_load_images(MockPhotoImage):
    mock_relative_to_assets = MagicMock(side_effect=lambda x: f"mocked_path/{x}")

    returned_images = load_images(MockPhotoImage, mock_relative_to_assets)

    print(mock_relative_to_assets.mock_calls)

    expected_calls = [call('welcome_img.png'), call('home.png'), call('entry_4.png')]

    mock_relative_to_assets.assert_has_calls(expected_calls, any_order=True)


def test_relative_to_assets():
    test_input = "some_directory/some_file.txt"
    expected_output = ASSETS_PATH / Path(test_input)
    result = relative_to_assets(test_input)

    assert result == expected_output, f"Expected {expected_output}, but got {result}"
