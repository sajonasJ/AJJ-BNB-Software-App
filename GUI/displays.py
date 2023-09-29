from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Label, StringVar, Toplevel, CENTER, VERTICAL, \
    HORIZONTAL, BOTH, END, TOP
from tkinter import ttk
import matplotlib.pyplot as plt
import mplcursors
import numpy as np
from utils import *


def make_window():
    window = Tk()
    window.title("AJJ BNB")
    window.configure(bg="#E8E8E8")
    window_height = 626
    window_width = 932
    return window, window_height, window_width


window, window_height, window_width = make_window()
global screen_height, screen_width, x_cordinate, y_cordinate


def center_screen():
    """ gets the coordinates of the center of the screen """

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # Coordinates of the upper left corner of the window to make the window appear in the center
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


def display_suburb_listings(results, column_names, suburb):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    new_window = Toplevel(window)
    new_window.title(f"Listings for {suburb}")

    # Set maximum width and height for the window
    max_width = 1200  # Replace with your desired maximum width
    max_height = 800  # Replace with your desired maximum height
    new_window.maxsize(max_width, max_height)

    # Set the initial size, but do not exceed the maximum size
    initial_width = min(screen_width, max_width)
    initial_height = min(screen_height - 100, max_height)
    new_window.geometry(f"{initial_width}x{initial_height}")

    # Treeview Configuration
    tree = ttk.Treeview(new_window, column=column_names, show='headings')
    max_widths = [max(len(str(row[i])) for row in results) for i in range(len(column_names))]
    min_width = 50
    max_col_width = 200
    for index, value in enumerate(column_names):
        width = max(min_width, min(max_widths[index] * 8, max_col_width))
        tree.column(f"#{index + 1}", anchor=CENTER, width=width)
        tree.heading(f"#{index + 1}", text=f"{value}")

    for row in results:
        tree.insert("", END, values=row)

    # Scrollbar Configuration
    scrollbar = ttk.Scrollbar(new_window, orient=VERTICAL, command=tree.yview)
    scrollbar.place(x=initial_width - 20, y=0, height=initial_height - 100)
    tree.configure(yscrollcommand=scrollbar.set)

    x_scrollbar = ttk.Scrollbar(new_window, orient=HORIZONTAL, command=tree.xview)
    x_scrollbar.place(x=0, y=initial_height - 80, width=initial_width - 20)
    tree.configure(xscrollcommand=x_scrollbar.set)

    # Treeview Placement
    tree.place(x=10, y=10, width=initial_width - 40, height=initial_height - 100)


def display_price_chart(the_prices, suburb, the_names, the_dates):
    fig, ax = plt.subplots(figsize=(5, 2.7))
    ax.scatter(np.arange(len(the_prices)), the_prices, label='Price')
    ax.set_yticklabels([])
    ax.set_title(f"Price Data for {suburb}")
    ax.legend()

    mplcursors.cursor(ax, hover=True).connect('add', lambda sel: on_hover(sel, the_prices, the_names, the_dates))
    plt.show()


def display_keyword_results(results, column_names, keywords):
    # display the results from the chosen keywords the "Search" button
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    new_window = Toplevel(window)
    new_window.title(f"Listings for {keywords}")
    new_window.geometry(f"{screen_width}x{screen_height - 100}")

    tree = ttk.Treeview(new_window, column=column_names, show='headings')
    for index, value in enumerate(column_names):
        tree.column(f"#{index + 1}", anchor=CENTER)
        tree.heading(f"#{index + 1}", text=f"{value}")

    for row in results:
        tree.insert("", END, values=row)

    scrollbar = ttk.Scrollbar(new_window, orient=VERTICAL, command=tree.yview)
    scrollbar.place(x=screen_width - 20, y=0, height=screen_height - 200)

    tree.configure(yscrollcommand=scrollbar.set)

    x_scrollbar = ttk.Scrollbar(new_window, orient=HORIZONTAL, command=tree.xview)
    x_scrollbar.place(x=0, y=screen_height - 180, width=screen_width - 40)

    tree.configure(xscrollcommand=x_scrollbar.set)

    tree.place(x=10, y=10, width=screen_width - 40, height=screen_height - 200)


def display_cleanliness(result_number, suburb, label3):
    # display cleanliness chart from the getCleanlinessData() function "Cleanliness" button
    print("display cleanliness")
    label3.config(text=f"The number of reviews that mention cleanliness in {suburb} is: {result_number}")

# "Display by Ratings" button, "Display List" button
# def displaySuburbRatingsRecords(results, columnNames, suburb):
#     # results, columnNames, suburb = getSuburbRatings(theSuburb, howMuchData, 'Record')
#
#     screen_width = window.winfo_screenwidth()
#     screen_height = window.winfo_screenheight()
#     newWindow = Toplevel(window)
#     newWindow.title(f"Listings for {suburb}")
#     newWindow.geometry(f"{screen_width}x{screen_height - 100}")
#
#     tree = ttk.Treeview(newWindow, column=columnNames, show='headings')
#     for index, value in enumerate(columnNames):
#         tree.column(f"#{index + 1}", anchor=CENTER)
#         tree.heading(f"#{index + 1}", text=f"{value}")
#
#     for row in results:
#         tree.insert("", END, values=row)
#
#     scrollbar = ttk.Scrollbar(newWindow, orient=VERTICAL, command=tree.yview)
#     scrollbar.place(x=screen_width - 20, y=0, height=screen_height - 200)
#
#     tree.configure(yscrollcommand=scrollbar.set)
#
#     x_scrollbar = ttk.Scrollbar(newWindow, orient=HORIZONTAL, command=tree.xview)
#     x_scrollbar.place(x=0, y=screen_height - 180, width=screen_width - 40)
#
#     tree.configure(xscrollcommand=x_scrollbar.set)
#
#     tree.place(x=10, y=10, width=screen_width - 40, height=screen_height - 200)


# "Display by Ratings" button, "Display Chart" button
# def displaySuburbRatingsChart(theScore, suburb, theNames):
#     # theScore, theSuburb, theNames = getSuburbRatings(suburb, howMuchData, 'Chart')
#     fig, ax = plt.subplots(figsize=(5, 2.7))
#     ax.scatter(np.arange(len(theScore)), theScore, label='Rating')
#     ax.set_yticklabels([])
#     ax.set_title(f"Ratings over 75 for {suburb}")
#     ax.legend()
#
#     mplcursors.cursor(ax, hover=True).connect('add', lambda sel: onHoverRatings(sel, theScore, theNames))
#     plt.show()
