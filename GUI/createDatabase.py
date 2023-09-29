import sqlite3
import pandas as pd
import sys
import tkinter as tk
from tkinter import ttk
import math


connection = sqlite3.connect("data.db")
cursor = connection.cursor()

#cursor.execute("CREATE TABLE listingsDec(id,name,description,transit,picture_url,host_id,host_url,street,neighbourhood,city,state,zipcode,market,smart_location,property_type,room_type,accommodates,bathrooms,bedrooms,beds,price,weekly_price,monthly_price,security_deposit,cleaning_fee,guests_included,extra_people,review_scores_rating,review_scores_accuracy,review_scores_cleanliness,review_scores_checkin,review_scores_communication,review_scores_location,review_scores_value,number_of_reviews)")
cursor.execute("CREATE TABLE IF NOT EXISTS reviewsDec(listing_id,id,date,reviewer_id,reviewer_name,comments)")
cursor.execute("CREATE TABLE IF NOT EXISTS calendarDec(listing_id,date,available,price)")


root = tk.Tk()
root.geometry('500x300')
root.title('AJJ BNB')
root_height = 626
root_width = 932

global screen_height, screen_width, x_cordinate, y_cordinate
def center_screen():
    """ gets the coordinates of the center of the screen """

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # Coordinates of the upper left corner of the window to make the window appear in the center
    x_cordinate = int((screen_width / 2) - (root_width / 2))
    y_cordinate = int((screen_height / 2) - (root_height / 2))
    root.geometry("{}x{}+{}+{}".format(root_width, root_height, x_cordinate, y_cordinate))


center_screen()

root.grid_rowconfigure(0, weight=1, minsize=200)
root.grid_columnconfigure(0, weight=1, minsize=250)
root.grid_columnconfigure(1, weight=1, minsize=250)

# start button
start_button = ttk.Button(root, text='Get Data', command= lambda: getData())
start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)

# stop button
stop_button = ttk.Button(root, text='Close', command= lambda: close())
stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)


output_text = tk.Text(root, height=30, width=90)
output_text.grid(row=0, column=0, columnspan=3)
output_text.insert(tk.END, "If data.db exists in the directory please close this window\n")


def getTheData():
    count = 0

    output_text.insert(tk.END, "Creating Database...\n")
    output_text.insert(tk.END, "Please wait...\n")
    root.update_idletasks()  # updating the Text widget immediately
    # Simulating some delay in database creation

    dfListings = pd.read_csv('../bnb_data/listings_dec18.csv', low_memory=False)
    dfReviews = pd.read_csv('../bnb_data/reviews_dec18.csv', low_memory=False)
    dfCalendar = pd.read_csv('../bnb_data/calendar_dec18.csv', low_memory=False)

    # the total number of records in each dataframe
    num_records_listings = dfListings.shape[0]
    num_records_reviews = dfReviews.shape[0]
    num_records_calendar = dfCalendar.shape[0]

    print(num_records_calendar)
    totalRecords = num_records_listings + num_records_reviews + num_records_calendar

    # id listing_url	scrape_id	last_scraped	name	summary	space
    # description	experiences_offered	neighborhood_overview	notes	transit	access
    # interaction	house_rules	thumbnail_url	medium_url	picture_url	xl_picture_url	host_id	host_url
    # host_name	host_since	host_location	host_about	host_response_time	host_response_rate	host_acceptance_rate
    # host_is_superhost	host_thumbnail_url	host_picture_url	host_neighbourhood	host_listings_count
    # host_total_listings_count	host_verifications	host_has_profile_pic	host_identity_verified	street
    # neighbourhood	neighbourhood_cleansed	neighbourhood_group_cleansed	city	state	zipcode	market
    # smart_location	country_code	country	latitude	longitude	is_location_exact	property_type
    # room_type	accommodates	bathrooms	bedrooms	beds	bed_type	amenities	square_feet	price
    # weekly_price	monthly_price	security_deposit	cleaning_fee	guests_included	extra_people
    # minimum_nights	maximum_nights	calendar_updated	has_availability
    # availability_30	availability_60	availability_90	availability_365	calendar_last_scraped	number_of_reviews
    # first_review	last_review	review_scores_rating	review_scores_accuracy	review_scores_cleanliness
    # review_scores_checkin	review_scores_communication	review_scores_location	review_scores_value	requires_license
    # license	jurisdiction_names	instant_bookable	is_business_travel_ready	cancellation_policy
    # require_guest_profile_picture	require_guest_phone_verification	calculated_host_listings_count
    # reviews_per_month
    columns = dfListings.columns.tolist()
    cursor = connection.cursor()

    create_table_statement = "CREATE TABLE IF NOT EXISTS listingsDec ("
    create_table_statement += ','.join(columns)
    create_table_statement += ")"

    cursor.execute(create_table_statement)
    print(columns)

    for row in dfListings.itertuples():
        values = tuple(getattr(row, col) for col in columns)
        #values = (row.id,row.name,row.description,row.transit,row.picture_url,row.host_id,row.host_url,row.street,row.neighbourhood,row.city,row.state,row.zipcode,row.market,row.smart_location,row.property_type,row.room_type,row.accommodates,row.bathrooms,row.bedrooms,row.beds,row.price,row.weekly_price,row.monthly_price,row.security_deposit,row.cleaning_fee,row.guests_included,row.extra_people,row.review_scores_rating,row.review_scores_accuracy,row.review_scores_cleanliness,row.review_scores_checkin,row.review_scores_communication,row.review_scores_location,row.review_scores_value,row.number_of_reviews)
        #print(row)
        cursor.execute('''
                    INSERT INTO listingsDec ({})
                VALUES ({})
                '''.format(','.join(columns), ','.join(['?'] * len(columns))),
                values)
        count+= 1

        if(0.2 * totalRecords == count):
            print("20% done.\n")
        elif(0.4 * totalRecords == count):
            print("40% done.\n")
        elif(0.6 * totalRecords == count):
            print("60% done.\n")
        elif(0.8 * totalRecords == count):
            print("80% done.\n")
        elif(totalRecords == count):
            print("100% done!\n")
    connection.commit()


    for row in dfReviews.itertuples():
        values = (row.listing_id,row.id,row.date,row.reviewer_id,row.reviewer_name,row.comments)
        #print(row)
        cursor.execute('''INSERT INTO reviewsDec(listing_id,id,date,reviewer_id,reviewer_name,comments)
                    VALUES (?,?,?,?,?,?)
                    ''',
                    values
                    )
        count+= 1

        if(0.2 * totalRecords == count):
            print("20% done.\n")
        elif(0.4 * totalRecords == count):
            print("40% done.\n")
        elif(0.6 * totalRecords == count):
            print("60% done.\n")
        elif(0.8 * totalRecords == count):
            print("80% done.\n")
        elif(totalRecords == count):
            print("100% done!\n")
    connection.commit()

    for row in dfCalendar.itertuples():
        values = (row.listing_id,row.date,row.available,row.price)
        #print(row)
        cursor.execute('''INSERT INTO calendarDec(listing_id,date,available,price)
                    VALUES (?,?,?,?)
                    ''',
                    values
                    )
        count+= 1
        if(0.2 * totalRecords == count):
            output_text.insert(tk.END, "Total Records 20% done.\n")
            root.update_idletasks()  # Refresh the Tkinter window
            print("20% done.\n")
        elif(0.4 * totalRecords == count):
            output_text.insert(tk.END, "Total Records 40% done.\n")
            root.update_idletasks()  # Refresh the Tkinter window
            print("40% done.\n")
        elif(0.6 * totalRecords == count):
            output_text.insert(tk.END, "Total Records 60% done.\n")
            root.update_idletasks()  # Refresh the Tkinter window
            print("60% done.\n")
        elif(0.8 * totalRecords == count):
            output_text.insert(tk.END, "Total Records 80% done.\n")
            root.update_idletasks()  # Refresh the Tkinter window
            print("80% done.\n")
        elif(totalRecords == count):
            output_text.insert(tk.END, "Total Records 100% done.\n")
            root.update_idletasks()  # Refresh the Tkinter window
            print("100% done!\n")
            root.after(6000)  # waits for 2000 milliseconds
            output_text.insert(tk.END, "Database Created Successfully!\n")
            output_text.insert(tk.END, "You can now close this window.\n")
    connection.commit()





def getData():
    getTheData()


def close():
    #quit the script
    root.destroy()


root.mainloop()


