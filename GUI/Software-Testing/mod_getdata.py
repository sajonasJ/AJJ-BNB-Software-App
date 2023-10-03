# This file is for retrieving data from the database using queries
from sqlite3 import connect
import sqlite3
from mod_displays import *
from mod_utils import *
from mod_constants import *


def get_suburb_listings( start_date, end_date, suburb, how_much_data):
    """retrieves the suburb listings using date and queries"""
    print('get suburb listings')
    dates = select_date(start_date, end_date)
    print('start Date=', dates[0], 'end Date=', dates[1], 'suburb=', suburb)
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()

        if how_much_data == 'Short':
            # preselected columns
            cursor.execute(SUBURB_LISTING_SHORTQUERY, (dates[0], dates[1], suburb))
            results = cursor.fetchall()
            print("Column names:", COLUMN_NAMES_SHORT)
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


def get_keyword_results(start_date, end_date, key_words, how_much_data, connection=None, display_func=None):
    cleaned_words = clean_user_input(key_words)
    dates = select_date(start_date, end_date)
    print('startDate=', dates[0], 'endDate=', dates[1])

    if connection is None:
        connection = connect('data.db')

    cursor = connection.cursor()

    if how_much_data == 'Short':
        like_conditions = " OR ".join([f"l.amenities LIKE ?" for _ in cleaned_words])
        query = BASE_KEYWORD_QUERY.format(like_conditions)
        params = (dates[0], dates[1]) + tuple(f"%{word}%" for word in cleaned_words)

        cursor.execute(query, params)
        results = cursor.fetchall()
        print("Column names:", COLUMN_NAMES_SHORT)
        if display_func:
            display_func(results, COLUMN_NAMES_SHORT, key_words)

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
        if display_func:
            display_func(results, column_names, key_words)

def get_cleanliness_data(keywords, suburb, label3, connection=None):
    """ get the cleanliness data for the displayCleanliness() """
    print('get cleanliness')

    # Use the provided connection or create a new one
    if connection is None:
        connection = connect('data.db')

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


def get_suburb_ratings(suburb, how_much_data, data_type, connection=None, display_records_func=None,
                       display_chart_func=None):

    if connection is None:
        connection = connect('data.db')
    cursor = connection.cursor()

    if how_much_data == 'All':
        select_columns = '*'
    else:
        select_columns = ', '.join(COLUMN_NAMES_SHORT)
    if data_type == 'Record':
        cursor.execute(QUERY_RECORD.format(columns=select_columns), (suburb,))
        results = cursor.fetchall()
        if how_much_data == 'Short':
            column_names = COLUMN_NAMES_SHORT
            if display_records_func:
                display_records_func(results, column_names, suburb)
        else:
            columns_info = cursor.execute("PRAGMA table_info(listingsDec)").fetchall()
            column_names = [col[1] for col in columns_info]
            print("Column names:", column_names)
            if display_records_func:
                display_records_func(results, column_names, suburb)

    elif data_type == 'Chart':
        cursor.execute(QUERY_CHART, (suburb,))
        results = cursor.fetchall()
        the_score = [row[1] for row in results]
        the_names = [row[0] for row in results]
        if display_chart_func:
            display_chart_func(the_score, suburb, the_names)