import sqlite3
import pandas as pd
import sys
import tkinter as tk
from tkinter import ttk
import math

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

cursor.execute(
    "CREATE TABLE listingsDec(id,name,description,transit,picture_url,host_id,host_url,street,neighbourhood,city,"
    "state,zipcode,market,smart_location,property_type,room_type,accommodates,bathrooms,bedrooms,beds,price,"
    "weekly_price,monthly_price,security_deposit,cleaning_fee,guests_included,extra_people,review_scores_rating,"
    "review_scores_accuracy,review_scores_cleanliness,review_scores_checkin,review_scores_communication,"
    "review_scores_location,review_scores_value,number_of_reviews)")
cursor.execute("CREATE TABLE reviewsDec(listing_id,id,date,reviewer_id,reviewer_name,comments)")
cursor.execute("CREATE TABLE calendarDec(listing_id,date,available,price)")


def get_the_data():
    count = 0

    df_listings = pd.read_csv('../bnb_data/listings_dec18.csv', low_memory=False)
    df_reviews = pd.read_csv('../bnb_data/reviews_dec18.csv', low_memory=False)
    df_calendar = pd.read_csv('../bnb_data/calendar_dec18.csv', low_memory=False)

    # the total number of records in each dataframe
    num_records_listings = df_listings.shape[0]
    num_records_reviews = df_reviews.shape[0]
    num_records_calendar = df_calendar.shape[0]

    print(num_records_calendar)
    total_records = num_records_listings + num_records_reviews + num_records_calendar

    for row in df_listings.itertuples():
        values = (
            row.id, row.name, row.description, row.transit, row.picture_url, row.host_id, row.host_url, row.street,
            row.neighbourhood, row.city, row.state, row.zipcode, row.market, row.smart_location, row.property_type,
            row.room_type, row.accommodates, row.bathrooms, row.bedrooms, row.beds, row.price, row.weekly_price,
            row.monthly_price, row.security_deposit, row.cleaning_fee, row.guests_included, row.extra_people,
            row.review_scores_rating, row.review_scores_accuracy, row.review_scores_cleanliness,
            row.review_scores_checkin,
            row.review_scores_communication, row.review_scores_location, row.review_scores_value, row.number_of_reviews)
        # print(row)
        cursor.execute('''
                    INSERT INTO listingsDec (id,name,description,transit,picture_url,host_id,host_url,street,\
                    neighbourhood,city,state,zipcode,market,smart_location,property_type,room_type,accommodates,\
                    bathrooms,bedrooms,beds,price,weekly_price,monthly_price,security_deposit,cleaning_fee,\
                    guests_included,extra_people,review_scores_rating,review_scores_accuracy,review_scores_cleanliness,\
                    review_scores_checkin,review_scores_communication,review_scores_location,review_scores_value,\
                    number_of_reviews)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    ''',
                       values
                       )
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
        values = (row.listing_id, row.id, row.date, row.reviewer_id, row.reviewer_name, row.comments)
        # print(row)
        cursor.execute('''INSERT INTO reviewsDec(listing_id,id,date,reviewer_id,reviewer_name,comments)VALUES
        (?,?,?,?,?,?)''',values)
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
        values = (row.listing_id, row.date, row.available, row.price)
        # print(row)
        cursor.execute('''INSERT INTO calendarDec(listing_id,date,available,price)VALUES (?,?,?,?)''',values)
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


root = tk.Tk()
root.geometry('300x120')
root.title('Progressbar Demo')

root.grid()

# start button
start_button = ttk.Button(
    root,
    text='Get Data',
    command=lambda: get_data()
)
start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)

# stop button
stop_button = ttk.Button(root,text='Cancel',command=lambda: cancel())
stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)


def get_data():
    get_the_data()


def cancel():
    root.quit()


root.mainloop()


