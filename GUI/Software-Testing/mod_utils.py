# This file is for helper functions for the app
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Label, StringVar, Toplevel, CENTER, VERTICAL, \
    HORIZONTAL, BOTH, END, TOP
from mod_constants import *
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# This file loads the csv files, read and output a database to be read by sqlite3
import time
import sqlite3
import pandas as pd

def select_date(start_date, end_date):
    return start_date.get_date(), end_date.get_date()


def clean_user_input(input):
    if not isinstance(input, str):
        raise ValueError("Input must be a string")
    split_input = [item.strip() for item in input.split(',')]
    return split_input



def make_window(center_screen):
    """Initial tkinter window"""
    window = Tk()
    window.title("AJJ BNB")
    window.configure(bg="#E8E8E8")
    window_height, window_width = 626, 932
    center_screen(window, window_width, window_height)  # make sure window is centre
    return window


def run_create_db():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS reviewsDec(listing_id,id,date,reviewer_id,reviewer_name,comments)")
    cursor.execute("CREATE TABLE IF NOT EXISTS calendarDec(listing_id,date,available,price)")
    connection.close()
    return

def close(root):
    """funct to close the window"""
    root.destroy()




def load_images(PhotoImage, relative_to_assets):
    img = {
        "welcome_image": PhotoImage(relative_to_assets("welcome_img.png")),
        "home_image": PhotoImage(relative_to_assets("home.png")),
        "display_price_dist": PhotoImage(relative_to_assets("display_price_distribution.png")),
        "display_image": PhotoImage(relative_to_assets("display.png")),
        "display_chart": PhotoImage(relative_to_assets("display_chart.png")),
        "display_list_image": PhotoImage(relative_to_assets("display_list.png")),
        "cleanliness_image": PhotoImage(relative_to_assets("cleanliness.png")),
        "display_ratings_image": PhotoImage(relative_to_assets("display_by_ratings.png")),
        "search_image": PhotoImage(relative_to_assets("search.png")),
        "suburb_listing_image": PhotoImage(relative_to_assets("suburb_listing.png")),
        "price_chart_image": PhotoImage(relative_to_assets("price_chart.png")),
        "display_list_img": PhotoImage(relative_to_assets("display_listings_for_suburb_img.png")),
        "display_cleanliness": PhotoImage(relative_to_assets("display_chart_by_cleanliness.png")),
        "display_listings_ratings": PhotoImage(relative_to_assets("display_listings_by_ratings.png")),
        "display_records": PhotoImage(relative_to_assets("Display_Search_Records.png")),
        "entry_image_1": PhotoImage(relative_to_assets("entry_4.png"))
    }
    return img

def get_price_chart_data(start_date, end_date, suburb, select_date_func=None, connection=None, execute_query=None,
                         display_func=None):

    if select_date_func:
        dates = select_date_func(start_date, end_date)
    else:
        dates = (start_date, end_date)


    if connection is None:
        connection = sqlite3.connect('data.db')

    cursor = connection.cursor()

    if execute_query:
        results = execute_query(cursor, PRICE_CHART_QUERY, (dates[0], dates[1], suburb))
    else:
        cursor.execute(PRICE_CHART_QUERY, (dates[0], dates[1], suburb))
        results = cursor.fetchall()

    the_names = [row[0] for row in results]
    the_prices = [row[1] for row in results]
    the_dates = [row[2] for row in results]

    if display_func:
        display_func(the_prices, suburb, the_names, the_dates)



