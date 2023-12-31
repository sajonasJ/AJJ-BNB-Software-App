from getData import get_suburb_ratings,get_cleanliness_data,get_price_chart_data,get_keyword_results,get_suburb_listings
from widgets import load_images, create_button, create_canvas
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Label, StringVar, Toplevel, CENTER, VERTICAL, \
    HORIZONTAL, BOTH, END, TOP
from tkinter import ttk
import sqlite3
from tkcalendar import Calendar
from createDatabase import run_create_db
from displays import initial_window
from constants import *
import time
from utils import throttle_click


def main():
    global current_canvas
    current_canvas = None
    window = initial_window()
    print('main Created')
    img = load_images()


    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(CITY_QUERY)
        results = cursor.fetchall()
        city_array = []
        for row in results:
            city_array.append(row[0])

    def show_suburb():
        """Show Display listings for suburb interface"""
        if not throttle_click():
            return  # Ignore this click if throttle_click returns False


        main_canvas.pack_forget()
        global current_canvas
        print('show_suburb')

        if current_canvas:
            current_canvas.pack_forget()

        canvas_list_suburb = create_canvas(window, show_suburb, show_cleanliness, show_price, show_search, show_listings)
        canvas_list_suburb.update()

        canvas_list_suburb.create_image(564.0, 70.0, image=img['display_list_img'])
        label55 = Label(window, text="How Many Columns?", bg="white")
        label55.place(x=250, y=350)

        n = StringVar()
        data_select = ttk.Combobox(window, width=22, height=13, textvariable=n,state='readonly')
        data_select['values'] = ['Short', 'All']
        data_select.set('Short')

        data_select.place(x=250, y=378)
        label2 = Label(window, text="Pick A Suburb", bg="white")
        label2.place(x=532, y=350)
        n = StringVar()
        city_select = ttk.Combobox(window, width=27, height=13, textvariable=n,state='readonly')
        city_select['values'] = city_array
        city_select.place(x=472, y=378)

        label = Label(window, text="Start date", bg="white")
        label.place(x=250, y=130)
        cal = Calendar(window, selectmode='day', year=2019, month=1, day=1, date_pattern='y-mm-dd')
        cal.place(x=250, y=150)
        end_label = Label(window, text="End date", bg="white")
        end_label.place(x=630, y=130)
        calendar_end = Calendar(window, selectmode='day', year=2019, month=1, day=1, date_pattern='y-mm-dd')
        calendar_end.place(x=630, y=150)

        create_button(
            img['display_image'],
            lambda:  get_suburb_listings(cal, calendar_end, city_select.get(), data_select.get()),
            x=454.0, y=536.0, w=218.0, h=39.0)

        canvas_list_suburb.pack()
        current_canvas = canvas_list_suburb
        return current_canvas

    def show_price():
        """PriceChart"""

        if not throttle_click():
            return  # Ignore this click if throttle_click returns False

        main_canvas.pack_forget()
        global current_canvas
        print('show_price')

        if current_canvas:
            current_canvas.pack_forget()

        canvas_price_listings = create_canvas(window, show_suburb, show_cleanliness, show_price, show_search, show_listings)
        canvas_price_listings.update()  # Update the canvas before getting dimensions
        canvas_price_listings.create_image(564.0, 70.0, image=img['display_price_dist'])

        label2 = Label(window, text="Pick A Suburb", bg="white")
        label2.place(x=532, y=350)

        n = StringVar()
        city_select = ttk.Combobox(window, width=27, height=13, textvariable=n, state='readonly')
        city_select['values'] = city_array
        city_select.place(x=472, y=378)
        label = Label(window, text="Start date", bg="white")
        label.place(x=250, y=130)
        cal = Calendar(window, selectmode='day', year=2019, month=1, day=1, date_pattern='y-mm-dd')
        cal.place(x=250, y=150)
        end_label = Label(window, text="End date", bg="white")
        end_label.place(x=630, y=130)
        calendar_end = Calendar(window, selectmode='day', year=2019, month=1, day=1, date_pattern='y-mm-dd')
        calendar_end.place(x=630, y=150)

        create_button(
            img['display_image'],
            lambda:  get_price_chart_data(cal, calendar_end, city_select.get()),
            x=454.0, y=536.0, w=218.0, h=39.0)

        canvas_price_listings.pack()
        current_canvas = canvas_price_listings
        return current_canvas

    def show_search():
        """Display Search Interface """

        if not throttle_click():
            return  # Ignore this click if throttle_click returns False

        main_canvas.pack_forget()
        global current_canvas
        print('show_search')

        if current_canvas:
            current_canvas.pack_forget()

        canvas_search = create_canvas(window, show_suburb, show_cleanliness, show_price, show_search, show_listings)
        canvas_search.update()  # Update the canvas before getting dimensions
        canvas_search.create_image(564.0, 70.0, image=img['display_records'])

        labelf = Label(window, text="Enter Keywords separated by comma", bg="white")
        labelf.place(x=462, y=425)

        entry_1 = Entry(bd=1, bg="white", fg="#000716", highlightthickness=0)
        entry_1.place(x=446.0, y=455.0, width=235.0, height=37.0)

        label55 = Label(window, text="How Many Columns?", bg="white")
        label55.place(x=250, y=350)

        n = StringVar()
        data_select = ttk.Combobox(window, width=22, height=13, textvariable=n, state='readonly')
        data_select['values'] = ['Short', 'All']
        data_select.set('Short')

        data_select.place(x=250, y=378)
        label = Label(window, text="Start date", bg="white")
        label.place(x=250, y=130)
        cal = Calendar(window, selectmode='day', year=2019, month=1, day=1, date_pattern='y-mm-dd')
        cal.place(x=250, y=150)
        end_label = Label(window, text="End date", bg="white")
        end_label.place(x=630, y=130)
        calendar_end = Calendar(window, selectmode='day', year=2019, month=1, day=1, date_pattern='y-mm-dd')
        calendar_end.place(x=630, y=150)

        create_button(
            img['display_image'],
            lambda: get_keyword_results(cal, calendar_end, entry_1.get(), data_select.get()),
            x=454.0, y=536.0, w=218.0, h=39.0)

        canvas_search.pack()
        current_canvas = canvas_search
        return current_canvas

    def show_cleanliness():
        """Display Price Chart"""

        if not throttle_click():
            return  # Ignore this click if throttle_click returns False

        main_canvas.pack_forget()
        global current_canvas
        print('show_cleanliness')

        if current_canvas:
            current_canvas.pack_forget()

        canvas_cleanliness = create_canvas(window, show_suburb, show_cleanliness, show_price, show_search, show_listings)
        canvas_cleanliness.update()
        canvas_cleanliness.create_image(564.0, 70.0, image=img['display_cleanliness'])

        label3 = Label(window, text="", bg="#FFFFFF")
        label3.place(x=232, y=150)
        label2 = Label(window, text="Pick A Suburb", bg="white")
        label2.place(x=532, y=350)

        n = StringVar()
        city_select = ttk.Combobox(window, width=27, height=13, textvariable=n, state='readonly')
        city_select['values'] = city_array
        city_select.place(x=472, y=378)

        create_button(
            img['display_list_image'],
            lambda: get_cleanliness_data(CLEANLINESS_KEYWORDS, city_select.get(), label3),
            x = 454.0, y = 536.0, w = 218.0, h = 39.0)

        canvas_cleanliness.pack()
        current_canvas = canvas_cleanliness
        return  current_canvas


    def show_listings():
        """Display Listings by Ratings Interface"""

        if not throttle_click():
            return  # Ignore this click if throttle_click returns False

        main_canvas.pack_forget()

        print('show_listings')
        global current_canvas

        if current_canvas:
            current_canvas.pack_forget()

        canvas_listings_by_ratings = create_canvas(window, show_suburb, show_cleanliness, show_price, show_search, show_listings)
        canvas_listings_by_ratings.create_image(564.0, 70.0, image=img['display_listings_ratings'])
        label55 = Label(window, text="How Many Columns?", bg="white")
        label55.place(x=250, y=150)

        n = StringVar()
        data_select = ttk.Combobox(window, width=22, height=13, textvariable=n, state='readonly')
        data_select['values'] = ['Short', 'All']
        data_select.set('Short')
        data_select.place(x=250, y=178)
        label2 = Label(window, text="Pick A Suburb", bg="white")
        label2.place(x=532, y=150)

        n = StringVar()
        city_select = ttk.Combobox(window, width=27, height=13, textvariable=n, state='readonly')
        city_select['values'] = city_array
        city_select.place(x=472, y=178)

        create_button(
            img['display_list_image'],
            lambda: get_suburb_ratings(city_select.get(), data_select.get(), 'Record'),
            x=284.0, y=536.0, w=218.0, h=39.0)
        create_button(
            img['display_chart'],
            lambda: get_suburb_ratings(city_select.get(), data_select.get(), 'Chart'),
            x=626.0, y=536.0, w=218.0, h=39.0)

        canvas_listings_by_ratings.pack()
        current_canvas = canvas_listings_by_ratings
        return current_canvas


    # Landing Canvas
    main_canvas = create_canvas(window, show_suburb, show_cleanliness, show_price, show_search, show_listings)
    main_canvas.create_image(563.0,312.0,image=img['welcome_image'])
    main_canvas.pack()
    window.resizable(False, False)
    window.mainloop()


if __name__ == "__main__":
    run_create_db()
    main()


