import matplotlib.pyplot as plt
import mplcursors
import numpy as np
from utils import *
from constants import *


def initial_window():
    global window
    window = make_window()
    print('initial window Created')
    return window


def display_suburb_listings( results, column_names, suburb):
    """displays the suburb listings"""
    initial_width = min(window.winfo_screenwidth(), MAX_WIDTH)
    initial_height = min(window.winfo_screenheight() - 100, MAX_HEIGHT)
    new_window = create_new_window(suburb, initial_width, initial_height)
    tree = configure_treeview(new_window, results, column_names, initial_width, initial_height)
    add_scrollbars_to_treeview(new_window, tree, initial_width, initial_height)
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


def display_keyword_results( results, column_names, keywords):
    """displays the search for keywords"""
    initial_width = min(window.winfo_screenwidth(), MAX_WIDTH)
    initial_height = min(window.winfo_screenheight() - 100, MAX_HEIGHT)
    new_window = create_new_window(keywords, initial_width, initial_height)
    tree = configure_treeview(new_window, results, column_names, initial_width, initial_height)
    add_scrollbars_to_treeview(new_window, tree, initial_width, initial_height)
    tree.place(x=10, y=10, width=initial_width - 40, height=initial_height - 100)


def display_cleanliness(result_number, suburb, label3):
    """displays for analysis of comments for cleanliness"""
    print("display cleanliness")
    label3.config(text=f"The number of reviews that mention cleanliness in {suburb} is: {result_number}")


def display_suburb_ratings_records( results, column_names, suburb):
    """displays the suburb ratings in a table"""
    initial_width = min(window.winfo_screenwidth(), MAX_WIDTH)
    initial_height = min(window.winfo_screenheight() - 100, MAX_HEIGHT)
    new_window = create_new_window(suburb, initial_width, initial_height)
    tree = configure_treeview(new_window, results, column_names, initial_width, initial_height)
    add_scrollbars_to_treeview(new_window, tree, initial_width, initial_height)
    tree.place(x=10, y=10, width=initial_width - 40, height=initial_height - 100)


def display_suburb_ratings_chart(the_score, the_suburb, the_names):
    """displays the suburb ratings in a chart"""
    fig, ax = plt.subplots(figsize=(5, 2.7))
    ax.scatter(np.arange(len(the_score)), the_score, label='Rating')
    ax.set_yticklabels([])
    ax.set_title(f"Ratings over 75 for {the_suburb}")
    ax.legend()
    mplcursors.cursor(ax, hover=True).connect('add', lambda sel: on_hover_ratings(sel, the_score, the_names))
    show_chart(fig, f"Ratings over 75 for {the_suburb}")
