import matplotlib.pyplot as plt
import mplcursors
import numpy as np
from mod_utils import *
from mod_constants import *


def initial_window(make_window_function):
    window = make_window_function()
    return window


def display_suburb_listings(results, column_names, suburb, window_size, create_new_window_func, configure_treeview_func, add_scrollbars_func):
    """displays the suburb listings"""
    initial_width = min(window_size[0], MAX_WIDTH)
    initial_height = min(window_size[1] - 100, MAX_HEIGHT)
    new_window = create_new_window_func(suburb, initial_width, initial_height)
    tree = configure_treeview_func(new_window, results, column_names, initial_width, initial_height)
    add_scrollbars_func(new_window, tree, initial_width, initial_height)
    tree.place(x=10, y=10, width=initial_width - 40, height=initial_height - 100)


def display_price_chart(the_prices, suburb, the_names, the_dates):
    """displays the price chart"""
    fig, ax = plt.subplots(figsize=(5, 2.7))
    ax.scatter(np.arange(len(the_prices)), the_prices, label='Price')
    ax.set_yticklabels([])
    ax.set_title(f"Price Data for {suburb}")
    ax.legend()
    mplcursors.cursor(ax, hover=True).connect('add', lambda sel: on_hover(sel, the_prices, the_names, the_dates))
    show_chart(fig, f"Price Data for {suburb}")


def display_keyword_results(results, column_names, keywords, window_size, create_new_window_func, configure_treeview_func, add_scrollbars_func):
    """displays the search for keywords"""
    initial_width = min(window_size[0], MAX_WIDTH)
    initial_height = min(window_size[1] - 100, MAX_HEIGHT)
    new_window = create_new_window_func(keywords, initial_width, initial_height)
    tree = configure_treeview_func(new_window, results, column_names, initial_width, initial_height)
    add_scrollbars_func(new_window, tree, initial_width, initial_height)
    tree.place(x=10, y=10, width=initial_width - 40, height=initial_height - 100)


def display_cleanliness(result_number, suburb, label):
    """displays for analysis of comments for cleanliness"""
    text_to_display = f"The number of reviews that mention cleanliness in {suburb} is: {result_number}"
    label.config(text=text_to_display)
    return text_to_display


def display_suburb_ratings_records(window, create_new_window, configure_treeview,
                                   add_scrollbars_to_treeview, place_method, results, column_names,
                                   suburb, max_width, max_height):
    """displays the suburb ratings in a table"""
    initial_width = min(window.winfo_screenwidth(), max_width)
    initial_height = min(window.winfo_screenheight() - 100, max_height)
    new_window = create_new_window(suburb, initial_width, initial_height)
    tree = configure_treeview(new_window, results, column_names, initial_width, initial_height)
    add_scrollbars_to_treeview(new_window, tree, initial_width, initial_height)
    place_method(tree, x=10, y=10, width=initial_width - 40, height=initial_height - 100)


def display_suburb_ratings_chart(the_score, the_suburb, the_names, plt_module=plt, np_module=np, mplcursors_module=mplcursors, on_hover_ratings_func=None, show_chart_func=None):
    """displays the suburb ratings in a chart"""
    fig, ax = plt_module.subplots(figsize=(5, 2.7))
    ax.scatter(np_module.arange(len(the_score)), the_score, label='Rating')
    ax.set_yticklabels([])
    ax.set_title(f"Ratings over 75 for {the_suburb}")
    ax.legend()
    mplcursors_module.cursor(ax, hover=True).connect('add', lambda sel: on_hover_ratings_func(sel, the_score, the_names))
    show_chart_func(fig, f"Ratings over 75 for {the_suburb}")
