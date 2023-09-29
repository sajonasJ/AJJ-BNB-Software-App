def on_hover(sel, the_prices, the_names, the_dates):
    index = sel.index
    sel.annotation.set_text(f'Price: {the_prices[index]}\nName:{the_names[index]}\nDate: {the_dates[index]}')


def select_date(start_date, end_date):
    """grab and store the start and end date for a user selected period from 2 calendars"""
    # date.config(text = "Selected Date is: " + cal.get_date())
    print(start_date.get_date(), end_date.get_date())
    return start_date.get_date(), end_date.get_date()


def clean_user_input(input):
    # clear the user input
    split_input = [item.strip() for item in input.split(',')]
    return split_input


def on_hover_ratings(sel, the_score, the_names):
    index = sel.index
    sel.annotation.set_text(f'Rating: {the_score[index]}\nPlace Name: {the_names[index]}')


# clear search fields (button will be needed for it)
def clear_search_query():
    print("clear search fields")


# display error messages
def display_error_message(error_message):
    print("display error message" + error_message)
