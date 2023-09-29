import sqlite3
from displays import *
from utils import *
from clean import *


def get_suburb_listings(start_date, end_date, suburb, how_much_data):
    """retrieves the suburb listings using date and queries"""
    dates = select_date(start_date, end_date)
    print('start Date=', dates[0], 'end Date=', dates[1], 'suburb=', suburb)
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()

        if how_much_data == 'Short':
            cursor.execute(suburb_listing_shortquery, (dates[0], dates[1], suburb))
            results = cursor.fetchall()

            print("Column names:", COLUMN_NAMES)
            display_suburb_listings(results, COLUMN_NAMES, suburb)

        elif how_much_data == 'All':
            cursor.execute(suburb_listing_longquery, (dates[0], dates[1], suburb))
            results = cursor.fetchall()
            cursor.execute(f"PRAGMA table_info(listingsDec)")
            columns_info = cursor.fetchall()
            column_names = [col[1] for col in columns_info]
            print("Column names:", column_names)
            display_suburb_listings(results, column_names, suburb)


def get_price_chart_data(start_date, end_date, suburb):
    dates = select_date(start_date, end_date)
    print('startDate=', dates[0], 'endDate=', dates[1])
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(price_chart_query, (dates[0], dates[1], suburb))
        results = cursor.fetchall()
        the_names = [row[0] for row in results]
        the_prices = [row[1] for row in results]
        the_dates = [row[2] for row in results]

        print(len(the_prices))
        display_price_chart(the_prices, suburb, the_names, the_dates)


def get_keyword_results(start_date, end_date, key_words, how_much_data):
    cleaned_words = clean_user_input(key_words)
    dates = select_date(start_date, end_date)
    print('startDate=', dates[0], 'endDate=', dates[1])

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    if how_much_data == 'Short':
        column_names = ['id', 'listing_url', 'name', 'description', 'transit', 'street', 'neighbourhood', 'city',
                        'state', 'zipcode', 'accommodates', 'bathrooms', 'bedrooms', 'amenities', 'price',
                        'review_scores_rating', 'cancellation_policy']

        query = "SELECT DISTINCT l.id,l.listing_url,l.name,l.description,l.transit,l.street,l.neighbourhood,l.city," \
                "l.state,l.zipcode,l.accommodates,l.bathrooms,l.bedrooms,l.amenities,l.price,l.review_scores_rating," \
                "l.cancellation_policy FROM listingsDec l INNER JOIN calendarDec c ON c.listing_id = l.id WHERE " \
                "c.date BETWEEN ? AND ? AND ("
        query += " OR ".join(["l.amenities LIKE ?" for _ in cleaned_words])
        query += ") ORDER BY l.id"
        params = (dates[0], dates[1]) + tuple(f"%{word}%" for word in cleaned_words)
        cursor.execute(query, params)

        results = cursor.fetchall()

        # Print the column names
        print("Column names:", column_names)

        display_keyword_results(results, column_names, key_words)

    elif how_much_data == 'All':
        query = "SELECT DISTINCT l.* FROM listingsDec l INNER JOIN calendarDec c ON c.listing_id = l.id WHERE c.date " \
                "BETWEEN ? AND ? AND ("
        query += " OR ".join(["l.amenities LIKE ?" for _ in cleaned_words])
        query += ") ORDER BY l.id"
        params = (dates[0], dates[1]) + tuple(f"%{word}%" for word in cleaned_words)
        cursor.execute(query, params)

        results = cursor.fetchall()

        cursor.execute(f"PRAGMA table_info(listingsDec)")
        columns_info = cursor.fetchall()

        column_names = [col[1] for col in columns_info]
        display_keyword_results(results, column_names, key_words)
        print("Column names:", column_names)

    connection.close()


# get the cleanliness data for the displayCleanliness()
def get_cleanliness_data(keywords, suburb, label3):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    query = "SELECT r.* FROM reviewsDec r INNER JOIN listingsDec l ON r.listing_id = l.id WHERE l.city = ? \
    AND (" + "OR ".join(["comments LIKE ?"] * len(keywords)) + ")"

    modified_keywords = ['%{}%'.format(keyword) for keyword in keywords]
    params = (suburb,) + tuple(modified_keywords)
    cursor.execute(query, params)
    results = cursor.fetchall()

    print("the total cleanliness results=", len(results))

    connection.close()

    display_cleanliness(len(results), suburb, label3)

# get suburb ratings data
def get_suburb_ratings(suburb, how_much_data, data_type):
    print(how_much_data)
    print("get suburb ratings" + suburb)
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    limit = 'LIMIT 100' if how_much_data == 'Short' else ''
    select_columns = '*' if how_much_data == 'All' else 'l.id, l.listing_url, l.name, l.description, l.transit, l.street, l.neighbourhood, l.city, l.state, l.zipcode, l.accommodates, l.bathrooms, l.bedrooms, l.amenities, l.price, l.review_scores_rating, l.cancellation_policy'

    if data_type == 'Record':
        query = f"""
            SELECT {select_columns} FROM listingsDec l
            WHERE l.city = ? AND l.review_scores_rating > 75
            ORDER BY l.review_scores_rating ASC
            {limit}
            """
        cursor.execute(query, (suburb,))
        results = cursor.fetchall()

        if how_much_data == 'Short':
            column_names = ['id', 'listing_url', 'name', 'description', 'transit', 'street', 'neighbourhood', 'city',
                            'state', 'zipcode', 'accommodates', 'bathrooms', 'bedrooms', 'amenities', 'price',
                            'review_scores_rating', 'cancellation_policy']
        else:
            cursor.execute("PRAGMA table_info(listingsDec)")
            columns_info = cursor.fetchall()
            column_names = [col[1] for col in columns_info]

        print("Column names:", column_names)
        return results, column_names, suburb

    elif data_type == 'Chart':
        query = f"""
            SELECT l.name, l.review_scores_rating 
            FROM listingsDec l
            WHERE l.city = ? AND l.review_scores_rating > 75
            ORDER BY l.review_scores_rating ASC
            {limit}
            """
        cursor.execute(query, (suburb,))
        results = cursor.fetchall()
        the_score = [row[1] for row in results]
        the_names = [row[0] for row in results]
        return the_score, suburb, the_names

    connection.close()
