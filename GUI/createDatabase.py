import sqlite3
import pandas as pd
import sys
import tkinter as tk
from tkinter import ttk
import math

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

#cursor.execute("CREATE TABLE listingsDec(id,name,description,transit,picture_url,host_id,host_url,street,neighbourhood,city,state,zipcode,market,smart_location,property_type,room_type,accommodates,bathrooms,bedrooms,beds,price,weekly_price,monthly_price,security_deposit,cleaning_fee,guests_included,extra_people,review_scores_rating,review_scores_accuracy,review_scores_cleanliness,review_scores_checkin,review_scores_communication,review_scores_location,review_scores_value,number_of_reviews)")
cursor.execute("CREATE TABLE reviewsDec(listing_id,id,date,reviewer_id,reviewer_name,comments)")
cursor.execute("CREATE TABLE calendarDec(listing_id,date,available,price)")

def getTheData():
    count = 0
    
    dfListings = pd.read_csv('../bnb_data/listings_dec18.csv', low_memory=False)
    dfReviews = pd.read_csv('../bnb_data/reviews_dec18.csv', low_memory=False)
    dfCalendar = pd.read_csv('../bnb_data/calendar_dec18.csv', low_memory=False)

    #the total number of records in each dataframe
    num_records_listings = dfListings.shape[0]
    num_records_reviews = dfReviews.shape[0]
    num_records_calendar = dfCalendar.shape[0]

    print(num_records_calendar)
    totalRecords = num_records_listings + num_records_reviews + num_records_calendar
    
    #id	listing_url	scrape_id	last_scraped	name	summary	space	description	experiences_offered	neighborhood_overview	notes	transit	access	interaction	house_rules	thumbnail_url	medium_url	picture_url	xl_picture_url	host_id	host_url	host_name	host_since	host_location	host_about	host_response_time	host_response_rate	host_acceptance_rate	host_is_superhost	host_thumbnail_url	host_picture_url	host_neighbourhood	host_listings_count	host_total_listings_count	host_verifications	host_has_profile_pic	host_identity_verified	street	neighbourhood	neighbourhood_cleansed	neighbourhood_group_cleansed	city	state	zipcode	market	smart_location	country_code	country	latitude	longitude	is_location_exact	property_type	room_type	accommodates	bathrooms	bedrooms	beds	bed_type	amenities	square_feet	price	weekly_price	monthly_price	security_deposit	cleaning_fee	guests_included	extra_people	minimum_nights	maximum_nights	calendar_updated	has_availability	availability_30	availability_60	availability_90	availability_365	calendar_last_scraped	number_of_reviews	first_review	last_review	review_scores_rating	review_scores_accuracy	review_scores_cleanliness	review_scores_checkin	review_scores_communication	review_scores_location	review_scores_value	requires_license	license	jurisdiction_names	instant_bookable	is_business_travel_ready	cancellation_policy	require_guest_profile_picture	require_guest_phone_verification	calculated_host_listings_count	reviews_per_month
    columns = dfListings.columns.tolist()
    cursor = connection.cursor()

    create_table_statement = "CREATE TABLE listingsDec ("
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


root = tk.Tk()
root.geometry('300x120')
root.title('Progressbar Demo')

root.grid()

# start button
start_button = ttk.Button(
    root,
    text='Get Data',
    command= lambda: getData()
)
start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)

# stop button
stop_button = ttk.Button(
    root,
    text='Cancel',
    command= lambda: cancel()
)
stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)


def getData():
    getTheData()
    

def cancel():
    #quit the script
    root.quit()
    
root.mainloop()

#sys.exit()
