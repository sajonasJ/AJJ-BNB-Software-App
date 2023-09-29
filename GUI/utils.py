# This file is for helper functions for the app

def on_hover(sel, the_prices, the_names, the_dates):
    index = sel.index
    sel.annotation.set_text(f'Price: {the_prices[index]}\nName:{the_names[index]}\nDate: {the_dates[index]}')


def select_date(start_date, end_date):
    """grab and store the start and end date for a user selected period from 2 calendars"""
    # date.config(text = "Selected Date is: " + cal.get_date())
    print(start_date.get_date(), end_date.get_date())
    return start_date.get_date(), end_date.get_date()


def clean_user_input(input):
    """cleans the user input"""
    split_input = [item.strip() for item in input.split(',')]
    return split_input


def on_hover_ratings(sel, the_score, the_names):
    """hover over data function"""
    index = sel.index
    sel.annotation.set_text(f'Rating: {the_score[index]}\nPlace Name: {the_names[index]}')


def clear_search_query():
    """clear search fields (button will be needed for it)"""
    print("clear search fields")


def display_error_message(error_message):
    """display error messages"""
    print("display error message" + error_message)


def center_screen(window, window_width, window_height):
    """ gets the coordinates of the center of the screen """
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # Coordinates of the upper left corner of the window to make the window appear in the center
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
