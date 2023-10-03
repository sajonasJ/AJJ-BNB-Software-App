# This file sets the variables for the widgets
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Label, StringVar, Toplevel, CENTER, VERTICAL, \
    HORIZONTAL, BOTH, END, TOP
from tkinter import ttk
from pathlib import Path
from mod_utils import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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




def create_button(ButtonClass, image, command, x, y, w, h):
    button = ButtonClass(image=image, borderwidth=0, highlightthickness=0, command=command, relief="flat")
    button.place(x=x, y=y, width=w, height=h)
    return button



def create_canvas(window, canvas_class, create_button, img, show_suburb, show_cleanliness, show_price, show_search, show_listings):
    canvas = canvas_class(window, bg="#E8E8E8", height=626, width=932, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    canvas.create_rectangle(228.0, 122.0, 899.0, 517.0, fill="#FFFFFF", outline="")
    canvas.create_rectangle(0.0, 0.0, 195.0, 626.0, fill="#32213A", outline="")
    canvas.create_text(56.0, 36.0, anchor="nw", text="AJJ", fill="#FFFFFF", font=("Inter Bold", 40 * -1))
    canvas.create_image(96.0, 145.0, image=img['home_image'])

    n = 79
    y_start = 223.0
    x_start = 33.0
    w = 126.0
    h = 56.0

    create_button(img['suburb_listing_image'], show_suburb, x_start, y_start, w, h)
    create_button(img['price_chart_image'], show_price, x_start, (n * 1) + y_start, w, h)
    create_button(img['search_image'], show_search, x_start, (n * 2) + y_start, w, h)
    create_button(img['cleanliness_image'], show_cleanliness, x_start, (n * 3) + y_start, w, h)
    create_button(img['display_ratings_image'], show_listings, x_start, (n * 4) + y_start, w, h)

    return canvas

