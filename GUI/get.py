import sqlite3
from displays import *
from utils import *

def getSuburbListings(startDate, endDate, suburb, howMuchData):
    dates = selectDate(startDate, endDate)
    print('startDate=', dates[0], 'endDate=', dates[1], 'suburb=', suburb)
    # print(fromDate, to, property, dataframe)

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    if howMuchData == 'Short':

        columnNames = ['id', 'listing_url', 'name', 'description', 'transit', 'street', 'neighbourhood', 'city',
                       'state', 'zipcode', 'accommodates', 'bathrooms', 'bedrooms', 'amenities', 'price',
                       'review_scores_rating', 'cancellation_policy']

        query = "SELECT DISTINCT l.id,l.listing_url,l.name,l.description,l.transit,l.street,l.neighbourhood,l.city,l.state,l.zipcode,l.accommodates,l.bathrooms,l.bedrooms,l.amenities,l.price,l.review_scores_rating,l.cancellation_policy FROM listingsDec l INNER JOIN calendarDec c ON c.listing_id = l.id WHERE c.date BETWEEN ? AND ? AND l.city = ? ORDER BY l.id"

        cursor.execute(query, (dates[0], dates[1], suburb))
        results = cursor.fetchall()

        # Print the column names
        print("Column names:", columnNames)

        displaysuburblistings(results, columnNames, suburb)

    elif howMuchData == 'All':
        query = "SELECT DISTINCT l.* FROM listingsDec l INNER JOIN calendarDec c ON c.listing_id = l.id WHERE c.date BETWEEN ? AND ? AND l.city = ? ORDER BY l.id"

        cursor.execute(query, (dates[0], dates[1], suburb))
        results = cursor.fetchall()

        cursor.execute(f"PRAGMA table_info(listingsDec)")
        columns_info = cursor.fetchall()
        # Fetch the results

        columnNames = [col[1] for col in columns_info]

        # Print the column names
        print("Column names:", columnNames)
        connection.close()
        displaysuburblistings(results, columnNames, suburb)


# For a user-selected period, produce a chart to show the distribution of prices of properties
# get property prices data for a chart "Price Chart" button
def get_price_chart_data(startDate, endDate, suburb):
    dates = selectDate(startDate, endDate)

    print('startDate=', dates[0], 'endDate=', dates[1])
    # print(fromDate, to, property, dataframe)

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    # query = "SELECT l.name, c.* FROM calendarDec c INNER JOIN listingsDec l ON c.listing_id = l.id WHERE c.date BETWEEN ? AND ? AND c.price NOT NULL"
    query = "SELECT l.name, c.price, c.date FROM calendarDec c INNER JOIN listingsDec l ON c.listing_id = l.id WHERE c.date BETWEEN ? AND ? AND c.price NOT NULL AND l.city = ?"

    cursor.execute(query, (dates[0], dates[1], suburb))

    results = cursor.fetchall()
    # print("the total cleanliness results=",len(results))
    thePrices = []
    theNames = []
    theDates = []

    for row in results:
        # print(row[0])
        theNames.append(row[0])
        thePrices.append(row[1])
        theDates.append(row[2])

    print(len(thePrices))
    connection.close()
    displaypricechart(thePrices, suburb, theNames, theDates)


def getKeywordResults(startDate, endDate, keyWords, howMuchData):
    # get keyword results from the user
    cleanedWords = cleanUserInput(keyWords)
    dates = selectDate(startDate, endDate)
    print('startDate=', dates[0], 'endDate=', dates[1])

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    if howMuchData == 'Short':
        columnNames = ['id', 'listing_url', 'name', 'description', 'transit', 'street', 'neighbourhood', 'city',
                       'state', 'zipcode', 'accommodates', 'bathrooms', 'bedrooms', 'amenities', 'price',
                       'review_scores_rating', 'cancellation_policy']

        query = "SELECT DISTINCT l.id,l.listing_url,l.name,l.description,l.transit,l.street,l.neighbourhood,l.city,l.state,l.zipcode,l.accommodates,l.bathrooms,l.bedrooms,l.amenities,l.price,l.review_scores_rating,l.cancellation_policy FROM listingsDec l INNER JOIN calendarDec c ON c.listing_id = l.id WHERE c.date BETWEEN ? AND ? AND ("
        query += " OR ".join(["l.amenities LIKE ?" for _ in cleanedWords])
        query += ") ORDER BY l.id"
        params = (dates[0], dates[1]) + tuple(f"%{word}%" for word in cleanedWords)
        cursor.execute(query, params)

        results = cursor.fetchall()

        # Print the column names
        print("Column names:", columnNames)

        displayKeywordResults(results, columnNames, keyWords)

    elif howMuchData == 'All':
        query = "SELECT DISTINCT l.* FROM listingsDec l INNER JOIN calendarDec c ON c.listing_id = l.id WHERE c.date BETWEEN ? AND ? AND ("
        query += " OR ".join(["l.amenities LIKE ?" for _ in cleanedWords])
        query += ") ORDER BY l.id"
        params = (dates[0], dates[1]) + tuple(f"%{word}%" for word in cleanedWords)
        cursor.execute(query, params)

        results = cursor.fetchall()

        cursor.execute(f"PRAGMA table_info(listingsDec)")
        columns_info = cursor.fetchall()

        columnNames = [col[1] for col in columns_info]

        print("Column names:", columnNames)

    connection.close()

    displayKeywordResults(results, columnNames, keyWords)


# get the cleanliness data for the displayCleanliness()
def getCleanlinessData(keywords, suburb, label3):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    query = "SELECT r.* FROM reviewsDec r INNER JOIN listingsDec l ON r.listing_id = l.id WHERE l.city = ? AND (" + " OR ".join(
        ["comments LIKE ?"] * len(keywords)) + ")"

    # Modify each keyword to include wildcards for partial matching
    modified_keywords = ['%{}%'.format(keyword) for keyword in keywords]

    # Combine suburb and modified keywords into a single tuple
    params = (suburb,) + tuple(modified_keywords)

    # Execute the query with the parameters
    cursor.execute(query, params)

    # Fetch the results
    results = cursor.fetchall()

    print("the total cleanliness results=", len(results))

    connection.close()

    displayCleanliness(len(results), suburb, label3)


#get suburb ratings data
# def getSuburbRatings(suburb, howMuchData, dataType):
#     print(howMuchData)
#     print("get suburb ratings" + suburb)
#     connection = sqlite3.connect('data.db')
#     cursor = connection.cursor()
#
#     if dataType == 'Record':
#         if howMuchData == 'Short':
#             columnNames = ['id', 'listing_url', 'name', 'description', 'transit', 'street', 'neighbourhood', 'city',
#                            'state', 'zipcode', 'accommodates', 'bathrooms', 'bedrooms', 'amenities', 'price',
#                            'review_scores_rating', 'cancellation_policy']
#
#             query = "SELECT l.id,l.listing_url,l.name,l.description,l.transit,l.street,l.neighbourhood,l.city,l.state,l.zipcode,l.accommodates,l.bathrooms,l.bedrooms,l.amenities,l.price,l.review_scores_rating,l.cancellation_policy FROM listingsDec l WHERE l.city = '" + suburb + "' AND l.review_scores_rating > 75 ORDER BY review_scores_rating DESC"
#
#             cursor.execute(query)
#
#             results = cursor.fetchall()
#
#             # Print the column names
#             print("Column names:", columnNames)
#
#             return (results, columnNames, suburb)
#
#         elif howMuchData == 'All':
#             query = "SELECT * FROM listingsDec l WHERE l.city = '" + suburb + "' AND l.review_scores_rating > 75 ORDER BY review_scores_rating DESC"
#
#             cursor.execute(query)
#
#             results = cursor.fetchall()
#
#             cursor.execute(f"PRAGMA table_info(listingsDec)")
#             columns_info = cursor.fetchall()
#
#             columnNames = [col[1] for col in columns_info]
#
#             print("Column names:", columnNames)
#
#             return (results, columnNames, suburb)
#     elif dataType == 'Chart':
#         query = "SELECT l.name, l.review_scores_rating FROM listingsDec l WHERE l.city = '" + suburb + "' AND l.review_scores_rating > 75 ORDER BY review_scores_rating ASC"
#         cursor.execute(query)
#         results = cursor.fetchall()
#
#         theScore = []
#         theNames = []
#
#         for row in results:
#             # print(row[0])
#             theNames.append(row[0])
#             theScore.append(row[1])
#             cursor.execute(query)
#
#         return theScore, suburb, theNames
#
#     connection.close()