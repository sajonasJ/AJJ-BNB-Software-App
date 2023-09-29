import createDatabase
import os
from clean import *
from pathlib import Path
from displays import *
from get import *

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Label, StringVar, Toplevel, CENTER, VERTICAL, \
    HORIZONTAL, BOTH, END, TOP
from tkinter import ttk
import pandas as pd
import matplotlib as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import sqlite3
from tkcalendar import Calendar
import numpy as np
import mplcursors

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


photo_images = {}
current_canvas = None

with sqlite3.connect('data.db') as connection:
    cursor = connection.cursor()
    cursor.execute(CITY_QUERY)
    results = cursor.fetchall()
    cityArray = []
    for row in results:
        cityArray.append(row[0])


def show_canvas2():
    print('canvas 2')
    canvas.pack_forget()
    global current_canvas

    if current_canvas:
        current_canvas.pack_forget()

    canvas_list_suburb = Canvas(window, bg="#E8E8E8", height=626, width=932, bd=0, highlightthickness=0, relief="ridge")
    canvas_list_suburb.place(x=0, y=0)
    canvas_list_suburb.update()
    canvas_list_suburb.create_rectangle(228.0, 122.0, 899.0, 517.0, fill="#FFFFFF", outline="")
    canvas_list_suburb.create_rectangle(0.0, 0.0, 195.0, 626.0, fill="#32213A", outline="")
    canvas_list_suburb.create_text(56.0, 36.0, anchor="nw", text="AJJ", fill="#FFFFFF", font=("Inter Bold", 40 * -1))
    image_image_6 = PhotoImage(file=relative_to_assets("home.png"))
    window.one = image_image_6
    # Create and place the image on canvas_list_suburb
    image_6 = canvas_list_suburb.create_image(96.0, 145.0, image=image_image_6)
    button_image_1 = PhotoImage(file=relative_to_assets("display.png"))
    window.negative = button_image_1
    button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0,
                      command=lambda: get_suburb_listings(cal, calendar_end, city_select.get(), data_select.get()),
                      relief="flat")
    button_1.place(x=454.0, y=536.0, width=218.0, height=39.0)
    image_image_7 = PhotoImage(file=relative_to_assets("display_listings_for_suburb_img.png"))
    window.two = image_image_7
    image_7 = canvas_list_suburb.create_image(564.0, 70.0, image=image_image_7)
    label55 = Label(window, text="How Many Columns?")
    window.aaaaaeeeeeeea = label55
    label55.place(x=250, y=350)

    n = StringVar()
    data_select = ttk.Combobox(window, width=22, height=13, textvariable=n)
    data_select['values'] = ['Short', 'All']
    data_select.set('Short')
    window.niineeeeee = data_select
    data_select.place(x=250, y=378)
    label2 = Label(window, text="Pick A Suburb")
    window.aaaaaa = label2
    label2.place(x=532, y=350)

    n = StringVar()
    city_select = ttk.Combobox(window, width=27, height=13, textvariable=n)
    city_select['values'] = cityArray
    window.niine = city_select
    city_select.place(x=472, y=378)
    button_image_1 = PhotoImage(file=relative_to_assets("display_by_ratings.png"))
    window.six = button_image_1
    button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas6(), relief="flat")
    button_1.place(x=33.0, y=539.0, width=126.0, height=56.0)
    button_image_2 = PhotoImage(file=relative_to_assets("price_chart.png"))
    window.seven = button_image_2
    button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas4(), relief="flat")
    button_2.place(x=33.0, y=302.0, width=126.0, height=56.0)
    button_image_3 = PhotoImage(file=relative_to_assets("cleanliness.png"))
    window.eight = button_image_3
    button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas3(), relief="flat")
    button_3.place(x=33.0, y=460.0, width=126.0, height=56.0)
    button_image_4 = PhotoImage(file=relative_to_assets("search.png"))
    window.nine = button_image_4
    button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas5(), relief="flat")
    button_4.place(x=33.0, y=381.0, width=126.0, height=56.0)
    button_image_5 = PhotoImage(file=relative_to_assets("suburb_listing.png"))
    window.ten = button_image_5
    button_5 = Button(image=button_image_5, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas2(), relief="flat")
    button_5.place(x=33.0, y=223.0, width=126.0, height=56.0)
    canvas_list_suburb.create_text(56.0, 36.0, anchor="nw", text="AJJ", fill="#FFFFFF", font=("Inter Bold", 40 * -1))
    label = Label(window, text="Start date")
    window.sixty = label
    label.place(x=250, y=130)
    cal = Calendar(window, selectmode='day', year=2019, month=1, day=1, date_pattern='y-mm-dd')
    window.fifty = cal
    cal.place(x=250, y=150)
    end_label = Label(window, text="End date")
    window.sixtytwo = end_label
    end_label.place(x=630, y=130)
    calendar_end = Calendar(window, selectmode='day', year=2019, month=1, day=1, date_pattern='y-mm-dd')
    window.fiftytwo = calendar_end
    calendar_end.place(x=630, y=150)
    canvas_list_suburb.pack()

    current_canvas = canvas_list_suburb


def show_canvas4():
    print("canvas4")
    canvas.pack_forget()
    global current_canvas

    if current_canvas:
        current_canvas.pack_forget()

    canvas_price_listings = Canvas(window, bg="#E8E8E8", height=626, width=932, bd=0, highlightthickness=0,
                                   relief="ridge")
    canvas_price_listings.place(x=0, y=0)
    canvas_price_listings.update()  # Update the canvas before getting dimensions
    canvas_price_listings.create_rectangle(228.0, 122.0, 899.0, 517.0, fill="#FFFFFF", outline="")
    canvas_price_listings.create_rectangle(0.0, 0.0, 195.0, 626.0, fill="#32213A", outline="")
    canvas_price_listings.create_text(56.0, 36.0, anchor="nw", text="AJJ", fill="#FFFFFF", font=("Inter Bold", 40 * -1))
    image_image_6 = PhotoImage(file=relative_to_assets("home.png"))
    window.one = image_image_6
    # Create and place the image on canvasPriceListings
    image_6 = canvas_price_listings.create_image(96.0, 145.0, image=image_image_6)
    button_image_1 = PhotoImage(file=relative_to_assets("display.png"))
    window.negative = button_image_1
    button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0,
                      command=lambda: get_price_chart_data(cal, calendar_end, city_select.get()), relief="flat")
    button_1.place(x=454.0, y=536.0, width=218.0, height=39.0)
    image_image_7 = PhotoImage(file=relative_to_assets("display_listings_for_suburb_img.png"))
    window.two = image_image_7
    image_7 = canvas_price_listings.create_image(564.0, 70.0, image=image_image_7)

    image_image_1 = PhotoImage(file=relative_to_assets("display_price_distribution.png"))
    window.two = image_image_1
    image_1 = canvas_price_listings.create_image(564.0, 70.0, image=image_image_1)

    button_image_1 = PhotoImage(file=relative_to_assets("display_by_ratings.png"))
    window.six = button_image_1
    button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas6(), relief="flat")
    button_1.place(x=33.0, y=539.0, width=126.0, height=56.0)

    button_image_2 = PhotoImage(file=relative_to_assets("price_chart.png"))
    window.seven = button_image_2
    button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas4(), relief="flat")
    button_2.place(x=33.0, y=302.0, width=126.0, height=56.0)

    button_image_3 = PhotoImage(file=relative_to_assets("cleanliness.png"))
    window.eight = button_image_3
    button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas3(), relief="flat")
    button_3.place(x=33.0, y=460.0, width=126.0, height=56.0)

    button_image_4 = PhotoImage(file=relative_to_assets("search.png"))
    window.nine = button_image_4
    button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas5(), relief="flat")
    button_4.place(x=33.0, y=381.0, width=126.0, height=56.0)

    button_image_5 = PhotoImage(file=relative_to_assets("suburb_listing.png"))
    window.ten = button_image_5
    button_5 = Button(image=button_image_5, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas2(), relief="flat")
    button_5.place(x=33.0, y=223.0, width=126.0, height=56.0)
    canvas_price_listings.create_text(56.0, 36.0, anchor="nw", text="AJJ", fill="#FFFFFF", font=("Inter Bold", 40 * -1))
    label2 = Label(window, text="Pick A Suburb")
    window.aaaaaa = label2
    label2.place(x=532, y=350)

    n = StringVar()
    city_select = ttk.Combobox(window, width=27, height=13, textvariable=n)
    city_select['values'] = cityArray
    window.niine = city_select
    city_select.place(x=472, y=378)
    label = Label(window, text="Start date")
    window.sixty = label
    label.place(x=250, y=130)
    cal = Calendar(window, selectmode='day', year=2019, month=1, day=1, date_pattern='y-mm-dd')
    window.fifty = cal
    cal.place(x=250, y=150)
    end_label = Label(window, text="End date")
    window.sixtytwo = end_label
    end_label.place(x=630, y=130)
    calendar_end = Calendar(window, selectmode='day', year=2019, month=1, day=1, date_pattern='y-mm-dd')
    window.fiftytwo = calendar_end
    calendar_end.place(x=630, y=150)
    canvas_price_listings.pack()
    current_canvas = canvas_price_listings


# Display search records function (Search button)
def show_canvas5():
    print("canvas5")
    canvas.pack_forget()
    global current_canvas

    if current_canvas:
        current_canvas.pack_forget()

    canvas_search = Canvas(window, bg="#E8E8E8", height=626, width=932, bd=0, highlightthickness=0, relief="ridge")
    canvas_search.place(x=0, y=0)
    canvas_search.update()  # Update the canvas before getting dimensions
    canvas_search.create_rectangle(228.0, 122.0, 899.0, 517.0, fill="#FFFFFF", outline="")
    canvas_search.create_rectangle(0.0, 0.0, 195.0, 626.0, fill="#32213A", outline="")
    canvas_search.create_text(56.0, 36.0, anchor="nw", text="AJJ", fill="#FFFFFF", font=("Inter Bold", 40 * -1))
    image_image_6 = PhotoImage(file=relative_to_assets("home.png"))
    window.one = image_image_6

    image_6 = canvas_search.create_image(96.0, 145.0, image=image_image_6)
    button_image_1 = PhotoImage(file=relative_to_assets("display.png"))
    window.negative = button_image_1
    button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0,
                      command=lambda: get_keyword_results(cal, calendar_end, entry_1.get(), data_select.get()),
                      relief="flat")
    button_1.place(x=454.0, y=536.0, width=218.0, height=39.0)
    image_image_1 = PhotoImage(file=relative_to_assets("Display_Search_Records.png"))
    window.two = image_image_1
    image_1 = canvas_search.create_image(564.0, 70.0, image=image_image_1)
    labelf = Label(window, text="Enter Keywords separated by comma")
    window.sixtyt = labelf
    labelf.place(x=462, y=425)
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_4.png"))
    window.three = entry_image_1
    entry_bg_1 = canvas_search.create_image(563.5, 474.5, image=entry_image_1)
    entry_1 = Entry(bd=0, bg="#E8E8E8", fg="#000716", highlightthickness=0)
    entry_1.place(x=446.0, y=455.0, width=235.0, height=37.0)
    label55 = Label(window, text="How Many Columns?")
    window.aaaaaeeeeeeea = label55
    label55.place(x=250, y=350)

    n = StringVar()
    data_select = ttk.Combobox(window, width=22, height=13, textvariable=n)
    data_select['values'] = ['Short', 'All']
    data_select.set('Short')
    window.niineeeeee = data_select
    data_select.place(x=250, y=378)
    label = Label(window, text="Start date")
    window.sixty = label
    label.place(x=250, y=130)
    cal = Calendar(window, selectmode='day', year=2019, month=1, day=1, date_pattern='y-mm-dd')
    window.fifty = cal
    cal.place(x=250, y=150)
    end_label = Label(window, text="End date")
    window.sixtytwo = end_label
    end_label.place(x=630, y=130)
    calendar_end = Calendar(window, selectmode='day', year=2019, month=1, day=1, date_pattern='y-mm-dd')
    window.fiftytwo = calendar_end
    calendar_end.place(x=630, y=150)
    button_image_1 = PhotoImage(file=relative_to_assets("display_by_ratings.png"))
    window.six = button_image_1
    button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas6(), relief="flat")
    button_1.place(x=33.0, y=539.0, width=126.0, height=56.0)
    button_image_2 = PhotoImage(file=relative_to_assets("price_chart.png"))
    window.seven = button_image_2
    button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas4(), relief="flat")
    button_2.place(x=33.0, y=302.0, width=126.0, height=56.0)

    button_image_3 = PhotoImage(file=relative_to_assets("cleanliness.png"))
    window.eight = button_image_3
    button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas3(), relief="flat")
    button_3.place(x=33.0, y=460.0, width=126.0, height=56.0)

    button_image_4 = PhotoImage(file=relative_to_assets("search.png"))
    window.nine = button_image_4
    button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0, command=lambda: show_canvas5(),
                      relief="flat")
    button_4.place(x=33.0, y=381.0, width=126.0, height=56.0)

    button_image_5 = PhotoImage(file=relative_to_assets("suburb_listing.png"))
    window.ten = button_image_5
    button_5 = Button(image=button_image_5, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas2(), relief="flat")
    button_5.place(x=33.0, y=223.0, width=126.0, height=56.0)
    canvas_search.create_text(56.0, 36.0, anchor="nw", text="AJJ", fill="#FFFFFF", font=("Inter Bold", 40 * -1))
    canvas_search.pack()
    current_canvas = canvas_search


def show_canvas3():
    print('canvas 3')
    canvas.pack_forget()
    global current_canvas
    if current_canvas:
        current_canvas.pack_forget()
    canvas_cleanliness = Canvas(window, bg="#E8E8E8", height=626, width=932, bd=0, highlightthickness=0, relief="ridge")
    canvas_cleanliness.place(x=0, y=0)
    canvas_cleanliness.update()
    canvas_cleanliness.create_rectangle(228.0, 122.0, 899.0, 517.0, fill="#FFFFFF", outline="")
    canvas_cleanliness.create_rectangle(0.0, 0.0, 195.0, 626.0, fill="#32213A", outline="")
    label3 = Label(window, text="", bg="#FFFFFF")
    window.aaaaaa = label3
    label3.place(x=232, y=150)
    label2 = Label(window, text="Pick A Suburb")
    window.aaaaaa = label2
    label2.place(x=532, y=350)

    n = StringVar()
    city_select = ttk.Combobox(window, width=27, height=13, textvariable=n)
    city_select['values'] = cityArray
    window.niine = city_select
    city_select.place(x=472, y=378)
    image_image_1 = PhotoImage(
        file=relative_to_assets("display_chart_by_cleanliness.png"))
    window.twelve = image_image_1
    image_1 = canvas_cleanliness.create_image(564.0, 70.0, image=image_image_1)
    button_image_1 = PhotoImage(file=relative_to_assets("display_by_ratings.png"))
    window.three = button_image_1
    button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas6(), relief="flat")
    button_1.place(x=33.0, y=539.0, width=126.0, height=56.0)
    image_image_2 = PhotoImage(file=relative_to_assets("home.png"))
    window.thirteen = image_image_2
    image_2 = canvas_cleanliness.create_image(96.0, 145.0, image=image_image_2)
    button_image_1 = PhotoImage(file=relative_to_assets("display_by_ratings.png"))
    window.fourteen = button_image_1
    button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas6(), relief="flat")
    button_1.place(x=33.0, y=539.0, width=126.0, height=56.0)
    button_image_2 = PhotoImage(file=relative_to_assets("price_chart.png"))
    window.fifteen = button_image_2
    button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas4(), relief="flat")
    button_2.place(x=33.0, y=302.0, width=126.0, height=56.0)
    button_image_3 = PhotoImage(file=relative_to_assets("cleanliness.png"))
    window.sixteen = button_image_3
    button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0,
                      command=lambda: print("button_3 clicked"), relief="flat")
    button_3.place(x=33.0, y=460.0, width=126.0, height=56.0)

    button_image_4 = PhotoImage(file=relative_to_assets("search.png"))
    window.seventeen = button_image_4
    button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas5(), relief="flat")
    button_4.place(x=33.0, y=381.0, width=126.0, height=56.0)
    button_image_5 = PhotoImage(file=relative_to_assets("suburb_listing.png"))
    window.eighteen = button_image_5
    button_5 = Button(image=button_image_5, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas2(), relief="flat")
    button_5.place(x=33.0, y=223.0, width=126.0, height=56.0)
    canvas_cleanliness.create_text(56.0, 36.0, anchor="nw", text="AJJ", fill="#FFFFFF", font=("Inter Bold", 40 * -1))
    button_image_5 = PhotoImage(file=relative_to_assets("display.png"))
    window.nineteen = button_image_5
    button_5 = Button(image=button_image_5, borderwidth=0, highlightthickness=0,
                      command=lambda: get_cleanliness_data(CLEANLINESS_KEYWORDS, city_select.get(), label3),
                      relief="flat")
    button_5.place(x=454.0, y=536.0, width=218.0, height=39.0)
    canvas_cleanliness.pack()
    current_canvas = canvas_cleanliness


def display_suburb_ratings_records(the_suburb, how_much_data):
    results, column_names, suburb = get_suburb_ratings(the_suburb, how_much_data, 'Record')
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    new_window = Toplevel(window)
    new_window.title(f"Listings for {suburb}")
    new_window.geometry(f"{screen_width}x{screen_height - 100}")
    tree = ttk.Treeview(new_window, columns=column_names, show='headings')
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


def display_suburb_ratings_chart(suburb, how_much_data):
    the_score, the_suburb, the_names = get_suburb_ratings(suburb, how_much_data, 'Chart')
    fig, ax = plt.subplots(figsize=(5, 2.7))
    ax.scatter(np.arange(len(the_score)), the_score, label='Rating')
    ax.set_yticklabels([])
    ax.set_title(f"Ratings over 75 for {the_suburb}")
    ax.legend()
    mplcursors.cursor(ax, hover=True).connect('add', lambda sel: on_hover_ratings(sel, the_score, the_names))
    plt.show()


def show_canvas6():
    print("canvas 6")
    canvas.pack_forget()
    global current_canvas

    if current_canvas:
        current_canvas.pack_forget()
    canvas_listings_by_ratings = Canvas(window, bg="#E8E8E8", height=626, width=932, bd=0, highlightthickness=0,
                                        relief="ridge")
    canvas_listings_by_ratings.place(x=0, y=0)
    canvas_listings_by_ratings.update()  # Update the canvas before getting dimensions
    canvas_listings_by_ratings.create_rectangle(228.0, 122.0, 899.0, 517.0, fill="#FFFFFF", outline="")
    canvas_listings_by_ratings.create_rectangle(0.0, 0.0, 195.0, 626.0, fill="#32213A", outline="")
    image_image_6 = PhotoImage(file=relative_to_assets("home.png"))
    window.one = image_image_6
    # Create and place the image on canvas_listings_by_ratings
    image_6 = canvas_listings_by_ratings.create_image(96.0, 145.0, image=image_image_6)
    button_image_1 = PhotoImage(file=relative_to_assets("display_list.png"))
    window.negativenegative = button_image_1
    button_111 = Button(image=button_image_1, borderwidth=0, highlightthickness=0,
                        command=lambda: display_suburb_ratings_records(city_select.get(), data_select.get()),
                        relief="flat")
    button_111.place(x=284.0, y=536.0, width=218.0, height=39.0)
    button_image_2 = PhotoImage(file=relative_to_assets("display_chart.png"))
    window.negativenegativenegative = button_image_2
    button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0,
                      command=lambda: display_suburb_ratings_chart(city_select.get(), data_select.get()), relief="flat")
    button_2.place(x=626.0, y=536.0, width=218.0, height=39.0)
    image_image_1 = PhotoImage(file=relative_to_assets("display_listings_by_ratings.png"))
    window.two = image_image_1
    image_1 = canvas_listings_by_ratings.create_image(564.0, 70.0, image=image_image_1)
    canvas_listings_by_ratings.create_text(56.0, 36.0, anchor="nw", text="AJJ", fill="#FFFFFF",
                                           font=("Inter Bold", 40 * -1))
    label55 = Label(window, text="How Many Columns?")
    window.aaaaaeeeeeeea = label55
    label55.place(x=250, y=150)

    n = StringVar()
    data_select = ttk.Combobox(window, width=22, height=13, textvariable=n)
    data_select['values'] = ['Short', 'All']
    data_select.set('Short')
    window.niineeeeee = data_select
    data_select.place(x=250, y=178)
    label2 = Label(window, text="Pick A Suburb")
    window.aaaaaa = label2
    label2.place(x=532, y=150)

    n = StringVar()
    city_select = ttk.Combobox(window, width=27, height=13, textvariable=n)
    city_select['values'] = cityArray
    window.niine = city_select
    city_select.place(x=472, y=178)
    button_image_1 = PhotoImage(file=relative_to_assets("display_by_ratings.png"))
    window.six = button_image_1
    button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas6(), relief="flat")
    button_1.place(x=33.0, y=539.0, width=126.0, height=56.0)
    button_image_2 = PhotoImage(file=relative_to_assets("price_chart.png"))
    window.seven = button_image_2
    button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas4(), relief="flat")
    button_2.place(x=33.0, y=302.0, width=126.0, height=56.0)
    button_image_3 = PhotoImage(file=relative_to_assets("cleanliness.png"))
    window.eight = button_image_3
    button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas3(), relief="flat")
    button_3.place(x=33.0, y=460.0, width=126.0, height=56.0)
    button_image_4 = PhotoImage(file=relative_to_assets("search.png"))
    window.nine = button_image_4
    button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas5(), relief="flat")
    button_4.place(x=33.0, y=381.0, width=126.0, height=56.0)
    button_image_5 = PhotoImage(file=relative_to_assets("suburb_listing.png"))
    window.ten = button_image_5
    button_5 = Button(image=button_image_5, borderwidth=0, highlightthickness=0,
                      command=lambda: show_canvas2(), relief="flat")
    button_5.place(x=33.0, y=223.0, width=126.0, height=56.0)
    canvas_listings_by_ratings.create_text(56.0, 36.0, anchor="nw", text="AJJ", fill="#FFFFFF",
                                           font=("Inter Bold", 40 * -1))
    canvas_listings_by_ratings.pack()
    current_canvas = canvas_listings_by_ratings


canvas = Canvas(window, bg="#E8E8E8", height=626, width=932, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("welcome_img.png"))
image_1 = canvas.create_image(563.0, 312.0, image=image_image_1)
canvas.create_rectangle(0.0, 0.0, 195.0, 626.0, fill="#32213A", outline="")
button_image_1 = PhotoImage(file=relative_to_assets("display_by_ratings.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0,
                  command=lambda: show_canvas6(), relief="flat")
button_1.place(x=33.0, y=539.0, width=126.0, height=56.0)
button_image_2 = PhotoImage(file=relative_to_assets("price_chart.png"))
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0,
                  command=lambda: show_canvas4(), relief="flat")
button_2.place(x=33.0, y=302.0, width=126.0, height=56.0)
button_image_3 = PhotoImage(file=relative_to_assets("cleanliness.png"))
button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0,
                  command=lambda: show_canvas3(), relief="flat")
button_3.place(x=33.0, y=460.0, width=126.0, height=56.0)
button_image_4 = PhotoImage(file=relative_to_assets("search.png"))
button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0,
                  command=lambda: show_canvas5(), relief="flat")
button_4.place(x=33.0, y=381.0, width=126.0, height=56.0)
button_image_5 = PhotoImage(file=relative_to_assets("suburb_listing.png"))
button_5 = Button(image=button_image_5, borderwidth=0, highlightthickness=0,
                  command=lambda: show_canvas2(), relief="flat")
button_5.place(x=33.0, y=223.0, width=126.0, height=56.0)
canvas.create_text(56.0, 36.0, anchor="nw", text="AJJ", fill="#FFFFFF", font=("Inter Bold", 40 * -1))
image_image_2 = PhotoImage(file=relative_to_assets("home.png"))
image_2 = canvas.create_image(96.0, 145.0, image=image_image_2)

canvas.pack()
window.resizable(False, False)
window.mainloop()
