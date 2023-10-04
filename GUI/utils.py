# This file is for helper functions for the app
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Label, StringVar, Toplevel, CENTER, VERTICAL, \
    HORIZONTAL, BOTH, END, TOP
from constants import *
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
    if not input:
        print("Error: empty input")
        return []

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


def make_window():
    """Initial tkinter window"""
    global window
    window = Tk()
    window.title("AJJ BNB")
    window.configure(bg="#E8E8E8")
    window_height, window_width = 626, 932
    center_screen(window, window_width, window_height)  # make sure window is centre
    return window


def calculate_initial_size():
    """sets the height and width at constant"""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    initial_width = min(screen_width, MAX_WIDTH)
    initial_height = min(screen_height - 100, MAX_HEIGHT)
    return initial_width, initial_height


def create_new_window(suburb, width, height):
    """Creates the new window with defined values"""
    new_window = Toplevel(window)
    new_window.title(f"Listings for {suburb}")
    new_window.geometry(f"{width}x{height}")
    new_window.maxsize(MAX_WIDTH, MAX_HEIGHT)
    center_screen(new_window, width, height)  # make sure window is centre
    return new_window


def configure_treeview(window, results, column_names, width, height):
    """creates the treeview inside a tkinter window"""
    tree = ttk.Treeview(window, columns=column_names, show='headings')
    max_widths = [max(len(str(row[i])) for row in results) for i in range(len(column_names))]

    for index, name in enumerate(column_names):
        col_width = max(MIN_WIDTH, min(max_widths[index] * 8, MAX_COL_WIDTH))
        tree.column(f"#{index + 1}", anchor=CENTER, width=col_width)
        tree.heading(f"#{index + 1}", text=f"{name}")

    for row in results:
        tree.insert("", END, values=row)
    return tree


def add_scrollbars_to_treeview(window, tree, width, height):
    """sets the scrollbars for the windows"""
    v_scrollbar = ttk.Scrollbar(window, orient=VERTICAL, command=tree.yview)
    v_scrollbar.place(x=width - 20, y=0, height=height - 100)
    tree.configure(yscrollcommand=v_scrollbar.set)

    h_scrollbar = ttk.Scrollbar(window, orient=HORIZONTAL, command=tree.xview)
    h_scrollbar.place(x=0, y=height - 80, width=width - 20)
    tree.configure(xscrollcommand=h_scrollbar.set)


def show_chart(fig, title):
    """takes the chart or diagram from matplotlib and includes it inside a window"""
    print('This chart is shown by tkinter')
    chart = tk.Tk()
    chart.title(title)
    window_width = 932
    window_height = 626
    center_screen(chart, window_width, window_height)

    frame = Frame(master=chart)
    frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    canvas = FigureCanvasTkAgg(fig, master=frame)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    tk.mainloop()


