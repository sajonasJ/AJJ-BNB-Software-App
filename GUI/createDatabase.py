# This file loads the csv files, read and output a database to be read by sqlite3
import time
import sqlite3
import pandas as pd
from utils import *
import os


def run_create_db():
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS reviewsDec(listing_id,id,date,reviewer_id,reviewer_name,comments)")
        cursor.execute("CREATE TABLE IF NOT EXISTS calendarDec(listing_id,date,available,price)")
    show_app(cursor, connection)
    return

def get_the_data(cursor, connection, root, output_text):
    """function to start getting the data using pandas and convert them to sqlite3"""
    count = 0
    try:
        df_listings = pd.read_csv('../bnb_data/listings_dec18.csv', low_memory=False)
        df_reviews = pd.read_csv('../bnb_data/reviews_dec18.csv', low_memory=False)
        df_calendar = pd.read_csv('../bnb_data/calendar_dec18.csv', low_memory=False)
    except FileNotFoundError:
        output_text.insert(tk.END, "File not found: listings_dec18.csv\n")
        output_text.insert(tk.END, "File not found: reviews_dec18.csv\n")
        output_text.insert(tk.END, "File not found: calendar_dec18.csv\n")
        return

    # the total number of records in each dataframe
    num_records_listings = df_listings.shape[0]
    num_records_reviews = df_reviews.shape[0]
    num_records_calendar = df_calendar.shape[0]

    print(num_records_calendar)
    total_records = num_records_listings + num_records_reviews + num_records_calendar

    columns = df_listings.columns.tolist()

    create_table_statement = "CREATE TABLE IF NOT EXISTS listingsDec ({})".format(','.join(columns))
    try:
        cursor.execute(create_table_statement)
    except sqlite3.DatabaseError:
        output_text.insert(tk.END, "Database error occurred.\n")
        return
    print(columns)

    for row in df_listings.itertuples():
        values = tuple(getattr(row, col) for col in columns)

        cursor.execute('''INSERT INTO listingsDec ({})VALUES ({})'''.format(','.join(columns), ','
                                                                            .join(['?'] * len(columns))), values)
        count += 1

        if 0.2 * total_records == count:
            print("20% done.\n")
        elif 0.4 * total_records == count:
            print("40% done.\n")
        elif 0.6 * total_records == count:
            print("60% done.\n")
        elif 0.8 * total_records == count:
            print("80% done.\n")
        elif total_records == count:
            print("100% done!\n")
    connection.commit()

    for row in df_reviews.itertuples():
        # Add this line to see the structure of row
        values = (row.listing_id, row.id, row.date, row.reviewer_id, row.reviewer_name, row.comments)
        # print("reviews", values)
        cursor.execute('''INSERT INTO reviewsDec(listing_id,id,date,reviewer_id,reviewer_name,comments)
                    VALUES (?,?,?,?,?,?)''', values)
        count += 1

        if 0.2 * total_records == count:
            print("20% done.\n")
        elif 0.4 * total_records == count:
            print("40% done.\n")
        elif 0.6 * total_records == count:
            print("60% done.\n")
        elif 0.8 * total_records == count:
            print("80% done.\n")
        elif total_records == count:
            print("100% done!\n")
    connection.commit()

    for row in df_calendar.itertuples():
        # Add this line to see the structure of row
        values = (row.listing_id, row.date, row.available, row.price)
        # print("calendar", values)
        cursor.execute('''INSERT INTO calendarDec(listing_id,date,available,price)VALUES (?,?,?,?)''', values)
        count += 1
        if 0.2 * total_records == count:
            output_text.insert(tk.END, "Total Records 20% done.\n")
            root.update_idletasks()  # Refresh the Tkinter window
            print("20% done.\n")
            time.sleep(1)
        elif 0.4 * total_records == count:
            output_text.insert(tk.END, "Total Records 40% done.\n")
            root.update_idletasks()  # Refresh the Tkinter window
            print("40% done.\n")
            time.sleep(1)
        elif 0.6 * total_records == count:
            output_text.insert(tk.END, "Total Records 60% done.\n")
            root.update_idletasks()  # Refresh the Tkinter window
            print("60% done.\n")
            time.sleep(1)
        elif 0.8 * total_records == count:
            output_text.insert(tk.END, "Total Records 80% done.\n")
            root.update_idletasks()  # Refresh the Tkinter window
            print("80% done.\n")
            time.sleep(1)
        elif total_records == count:
            output_text.insert(tk.END, "Total Records 100% done.\n")
            root.update_idletasks()  # Refresh the Tkinter window
            print("100% done!\n")
            time.sleep(1)
            output_text.insert(tk.END, "Database Created Successfully!\n")
            output_text.insert(tk.END, "You can now close this window.\n")
    connection.commit()


def get_data(root, cursor, connection):
    """func to get the data"""
    output_text.insert(tk.END, "Creating Database...\n")
    output_text.insert(tk.END, "Please wait...\n")
    root.update_idletasks()  # updating the Text widget immediately Simulating some delay in database creation
    get_the_data(cursor, connection, root, output_text)

def close(root):
    """funct to close the window"""
    root.destroy()


def show_app(cursor, connection):
    # create window
    root = tk.Tk()
    print('created root')
    root.geometry('500x300')
    root.title('AJJ BNB')
    root_height, root_width = 626, 932
    center_screen(root, root_width, root_height)
    # grid config
    root.grid_rowconfigure(0, weight=1, minsize=200)
    root.grid_columnconfigure(0, weight=1, minsize=250)
    root.grid_columnconfigure(1, weight=1, minsize=250)

    # start button
    start_button = ttk.Button(root, text='Get Data', command=lambda: get_data(root, cursor, connection))
    start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)


    # stop button
    stop_button = ttk.Button(root, text='Close', command=lambda: close(root))
    stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)
    global output_text
    output_text = tk.Text(root, height=30, width=90)
    output_text.grid(row=0, column=0, columnspan=3)
    output_text.insert(tk.END, "If data.db exists in the directory please close this window\n")



    root.resizable(False, False)  # does not allow the window to resize
    root.mainloop()
