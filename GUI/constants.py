# This file is used for constant's storage

MAX_WIDTH = 1200
MAX_HEIGHT = 800
MIN_WIDTH = 50
MAX_COL_WIDTH = 200



# List of keywords for cleanliness
CLEANLINESS_KEYWORDS = ['dirty', 'clean', 'cleanliness', 'disgusting', 'disgust', 'mold', 'neat', 'filthy',
                        'fresh', 'spotless', 'dust', 'germ', 'immaculate', 'tidy', 'hygiene', 'hygenic',
                        'gleaming''unsoiled', 'sanitary', 'contaminated''mop', 'vacuum''decontaminate', 'orderly',
                        'rinse', 'cob', 'cobwebs', 'rodents', 'rodent', 'vermin', 'mice', 'mouse']

# column_names
COLUMN_NAMES_SHORT = ['id', 'listing_url', 'name', 'description', 'transit', 'street', 'neighbourhood', 'city',
                      'state', 'zipcode', 'accommodates', 'bathrooms', 'bedrooms', 'amenities', 'price',
                      'review_scores_rating', 'cancellation_policy']

# Queries
# query for get_suburb_ratings
QUERY_CHART = """
    SELECT l.name, l.review_scores_rating 
    FROM listingsDec l
    WHERE l.city = ? AND l.review_scores_rating > 75
    ORDER BY l.review_scores_rating ASC"""


# query for get_suburb_ratings
QUERY_RECORD = """
    SELECT {columns} FROM listingsDec l
    WHERE l.city = ? AND l.review_scores_rating > 75
    ORDER BY l.review_scores_rating ASC"""


# query for get_suburb_listings
SUBURB_LISTING_SHORTQUERY = """
    SELECT DISTINCT
        l.id,
        l.listing_url,
        l.name,
        l.description,
        l.transit,
        l.street,
        l.neighbourhood,
        l.city,
        l.state,
        l.zipcode,
        l.accommodates,
        l.bathrooms,
        l.bedrooms,
        l.amenities,
        l.price,
        l.review_scores_rating,
        l.cancellation_policy
    FROM listingsDec l
    INNER JOIN calendarDec c ON c.listing_id = l.id
    WHERE c.date BETWEEN ? AND ? AND l.city = ?
    ORDER BY l.id """


# query for get_suburb_listings
SUBURB_LISTING_LONG_QUERY = """
    SELECT DISTINCT l.* 
    FROM listingsDec l 
    INNER JOIN calendarDec c ON c.listing_id = l.id 
    WHERE c.date BETWEEN ? AND ? AND l.city = ? 
    ORDER BY l.id;"""


# query for get_price_chart_data
PRICE_CHART_QUERY = """
    SELECT l.name, c.price, c.date 
    FROM calendarDec c 
    INNER JOIN listingsDec l ON c.listing_id = l.id 
    WHERE c.date BETWEEN ? AND ? AND c.price NOT NULL AND l.city = ? """


# query for get_keyword_results
BASE_KEYWORD_QUERY = """
    SELECT DISTINCT 
        l.id, l.listing_url, l.name, l.description, 
        l.transit, l.street, l.neighbourhood, l.city, 
        l.state, l.zipcode, l.accommodates, l.bathrooms, 
        l.bedrooms, l.amenities, l.price, l.review_scores_rating, 
        l.cancellation_policy 
    FROM listingsDec l 
    INNER JOIN calendarDec c ON c.listing_id = l.id 
    WHERE c.date BETWEEN ? AND ? AND ({})
    ORDER BY l.id """


# query for get_keyword_results
LONG_KEYWORD_QUERY = """
    SELECT DISTINCT l.*
    FROM listingsDec l 
    INNER JOIN calendarDec c ON c.listing_id = l.id 
    WHERE c.date BETWEEN ? AND ? AND ({})
    ORDER BY l.id """


# query for city_query
CITY_QUERY = "SELECT DISTINCT city FROM listingsDec"


# query for get_cleanliness_data
CLEANLINESS_QUERY = """
            SELECT rev.date, rev.reviewer_name, rev.comments
            FROM reviewsDec rev
            INNER JOIN listingsDec l ON rev.listing_id = l.id
            WHERE l.city = ? AND ({like_clauses})"""
