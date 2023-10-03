# This file is for helper functions for the app
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Label, StringVar, Toplevel, CENTER, VERTICAL, \
    HORIZONTAL, BOTH, END, TOP
from mod_constants import *
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def on_hover(sel, the_prices, the_names, the_dates):
    index = sel.index
    sel.annotation.set_text(f'Price: {the_prices[index]}\nName:{the_names[index]}\nDate: {the_dates[index]}')


def select_date(start_date, end_date):
    """grab and store the start and end date for a user selected period from 2 calendars"""
    # date.config(text = "Selected Date is: " + cal.get_date())
    #print(start_date.get_date(), end_date.get_date())
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


def center_screen(window, window_width, window_height, screen_width, screen_height):
    """ gets the coordinates of the center of the screen """
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))



def make_window(window, window_title="AJJ BNB", bg_color="#E8E8E8", window_height=626, window_width=932, center_func=None):
    """Initial tkinter window"""
    window.title(window_title)
    window.configure(bg=bg_color)
    if center_func:
        center_func(window, window_width, window_height)  # make sure window is centered
    return window



def calculate_initial_size(window, max_width=MAX_WIDTH, max_height=MAX_HEIGHT):
    """sets the height and width at constant"""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    initial_width = min(screen_width, max_width)
    initial_height = min(screen_height - 100, max_height)
    return initial_width, initial_height


def create_new_window(suburb, width, height, toplevel_constructor=Toplevel, parent_window=None, center_func=center_screen):
    """Creates the new window with defined values"""
    new_window = toplevel_constructor(parent_window)
    new_window.title(f"Listings for {suburb}")
    new_window.geometry(f"{width}x{height}")
    new_window.maxsize(MAX_WIDTH, MAX_HEIGHT)
    center_func(new_window, width, height)  # make sure window is centered
    return new_window





def configure_treeview(window, results, column_names, width, height, treeview_constructor=ttk.Treeview):
    """creates the treeview inside a tkinter window"""

    tree = treeview_constructor(window, columns=column_names, show='headings')
    max_widths = [max(len(str(row[i])) for row in results) for i in range(len(column_names))]

    for index, name in enumerate(column_names):
        col_width = max(MIN_WIDTH, min(max_widths[index] * 8, MAX_COL_WIDTH))
        tree.column(f"#{index + 1}", anchor=CENTER, width=col_width)
        tree.heading(f"#{index + 1}", text=f"{name}")

    for row in results:
        tree.insert("", END, values=row)

    return tree


def add_scrollbars_to_treeview(window, tree, width, height, ttk_module=ttk, vertical_orient=VERTICAL, horizontal_orient=HORIZONTAL):
    v_scrollbar = ttk_module.Scrollbar(window, orient=vertical_orient, command=tree.yview)
    v_scrollbar.place(x=width - 20, y=0, height=height - 100)
    tree.configure(yscrollcommand=v_scrollbar.set)

    h_scrollbar = ttk_module.Scrollbar(window, orient=horizontal_orient, command=tree.xview)
    h_scrollbar.place(x=0, y=height - 80, width=width - 20)
    tree.configure(xscrollcommand=h_scrollbar.set)


def show_chart(fig, title, tk=tk, Frame=Frame, FigureCanvasTkAgg=None, center_screen=None):

    chart = tk.Tk()
    chart.title(title)
    window_width = 932
    window_height = 626
    if center_screen:
        center_screen(chart, window_width, window_height)

    frame = Frame(master=chart)
    frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    if FigureCanvasTkAgg:
        canvas = FigureCanvasTkAgg(fig, master=frame)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    tk.mainloop()


