# This file is for retrieving data from the database using queries

import sqlite3
from displays import *
from utils import *
from constants import *

def get_suburb_listings( start_date, end_date, suburb, how_much_data):
    """retrieves the suburb listings using date and queries"""
    print('get suburb listings')
    dates = select_date(start_date, end_date)
    print('start Date=', dates[0], 'end Date=', dates[1], 'suburb=', suburb)
    with sqlite3.connect('data.db') as connection:
        #print('cursor',connection.cursor)
        cursor = connection.cursor()

        if how_much_data == 'Short':
            # preselected columns
            cursor.execute(SUBURB_LISTING_SHORTQUERY, (dates[0], dates[1], suburb))
            results = cursor.fetchall()
            print("Column names:", COLUMN_NAMES_SHORT)
            print(results)
            display_suburb_listings( results, COLUMN_NAMES_SHORT, suburb)

        elif how_much_data == 'All':
            # all columns
            cursor.execute(SUBURB_LISTING_LONG_QUERY, (dates[0], dates[1], suburb))
            results = cursor.fetchall()
            cursor.execute(f"PRAGMA table_info(listingsDec)")
            columns_info = cursor.fetchall()
            column_names = [col[1] for col in columns_info]
            print("Column names:", column_names)
            display_suburb_listings( results, column_names, suburb)


def get_price_chart_data(start_date, end_date, suburb):
    """get price data and display chart"""
    print('get price chart data')

    dates = select_date(start_date, end_date)
    print('startDate=', dates[0], 'endDate=', dates[1])
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(PRICE_CHART_QUERY, (dates[0], dates[1], suburb))
        results = cursor.fetchall()
        the_names = [row[0] for row in results]
        the_prices = [row[1] for row in results]
        the_dates = [row[2] for row in results]

        print(len(the_prices))
        display_price_chart(the_prices, suburb, the_names, the_dates)


def get_keyword_results(start_date, end_date, key_words, how_much_data):
    """Display the results of Search Bar"""
    print('get keyword results')

    cleaned_words = clean_user_input(key_words)
    dates = select_date(start_date, end_date)
    print('startDate=', dates[0], 'endDate=', dates[1])
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()

        if how_much_data == 'Short':
            # Preselected Columns
            like_conditions = " OR ".join([f"l.amenities LIKE ?" for _ in cleaned_words])
            query = BASE_KEYWORD_QUERY.format(like_conditions)
            params = (dates[0], dates[1]) + tuple(f"%{word}%" for word in cleaned_words)

            cursor.execute(query, params)
            results = cursor.fetchall()
            print("Column names:", COLUMN_NAMES_SHORT)
            display_keyword_results(results, COLUMN_NAMES_SHORT, key_words)

        elif how_much_data == 'All':
            # All columns
            like_conditions = " OR ".join([f"l.amenities LIKE ?" for _ in cleaned_words])
            query = LONG_KEYWORD_QUERY.format(like_conditions)
            params = (dates[0], dates[1]) + tuple(f"%{word}%" for word in cleaned_words)

            cursor.execute(query, params)
            results = cursor.fetchall()

            cursor.execute(f"PRAGMA table_info(listingsDec)")
            columns_info = cursor.fetchall()
            column_names = [col[1] for col in columns_info]

            print("Column names:", column_names)
            display_keyword_results(results, column_names, key_words)


def get_cleanliness_data(keywords, suburb, label3):
    """ get the cleanliness data for the displayCleanliness() """
    print('get cleanliness')

    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()

        # reconstruct the search query depending on the keywords
        modified_keywords = ['%{}%'.format(keyword) for keyword in keywords]
        like_clauses = ' OR '.join(f'comments LIKE ?' for keyword in modified_keywords)

        query = CLEANLINESS_QUERY.format(like_clauses=like_clauses)
        params = (suburb,) + tuple(modified_keywords)
        cursor.execute(query, params)
        results = cursor.fetchall()

        print("the total cleanliness results=", len(results))
        display_cleanliness(len(results), suburb, label3)


def get_suburb_ratings(suburb, how_much_data, data_type):
    """ get suburb ratings data"""
    print('get suburb ratings')

    print(how_much_data)
    print("get suburb ratings" + suburb)
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()

        if how_much_data == 'All':
            select_columns = '*'
        else:
            # Preselected Columns"
            select_columns = ', '.join(COLUMN_NAMES_SHORT)

        if data_type == 'Record':
            # display the data in a table
            cursor.execute(QUERY_RECORD.format(columns=select_columns), (suburb,))
            results = cursor.fetchall()

            if how_much_data == 'Short':
                column_names = COLUMN_NAMES_SHORT
                display_suburb_ratings_records(results, column_names, suburb)
            else:
                columns_info = cursor.execute("PRAGMA table_info(listingsDec)").fetchall()
                column_names = [col[1] for col in columns_info]
                print("Column names:", column_names)
                display_suburb_ratings_records(results, column_names, suburb)

        elif data_type == 'Chart':
            # display the data in a chart
            cursor.execute(QUERY_CHART, (suburb,))
            results = cursor.fetchall()
            the_score = [row[1] for row in results]
            the_names = [row[0] for row in results]
            display_suburb_ratings_chart(the_score, suburb, the_names)
