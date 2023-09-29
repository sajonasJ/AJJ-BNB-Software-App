# List of keywords for cleanliness
cleanliness_keywords = ['dirty', 'clean', 'cleanliness', 'disgusting', 'disgust', 'mold', 'neat', 'filthy',
                        'fresh', 'spotless', 'dust', 'germ', 'immaculate', 'tidy', 'hygiene', 'hygenic',
                        'gleaming''unsoiled', 'sanitary', 'contaminated''mop', 'vacuum''decontaminate', 'orderly',
                        'rinse', 'cob', 'cobwebs', 'rodents', 'rodent', 'vermin', 'mice', 'mouse']

# column_names
COLUMN_NAMES = ['id', 'listing_url', 'name', 'description', 'transit', 'street', 'neighbourhood', 'city',
                'state', 'zipcode', 'accommodates', 'bathrooms', 'bedrooms', 'amenities', 'price',
                'review_scores_rating', 'cancellation_policy']

# Queries

# suburb_rating_query
SUBURB_RATING_QUERY_100 = f"""
    SELECT l.name, l.review_scores_rating 
    FROM listingsDec l
    WHERE l.city = ? AND l.review_scores_rating > 75
    ORDER BY l.review_scores_rating ASC
    LIMIT 100
    """

SUBURB_RATING_QUERY_ALL = """
    SELECT * FROM listingsDec l
    WHERE l.city = ? AND l.review_scores_rating > 75
    ORDER BY l.review_scores_rating ASC;
"""


suburb_listing_shortquery = """
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
    FROM
        listingsDec l
    INNER JOIN
        calendarDec c ON c.listing_id = l.id
    WHERE
        c.date BETWEEN ? AND ?
        AND l.city = ?
    ORDER BY
        l.id;
"""

suburb_listing_longquery = """
    SELECT DISTINCT 
        l.* 
    FROM 
        listingsDec l 
    INNER JOIN 
        calendarDec c ON c.listing_id = l.id 
    WHERE 
        c.date BETWEEN ? AND ? 
        AND l.city = ? 
    ORDER BY 
        l.id;
"""

price_chart_query = """
    SELECT l.name, c.price, c.date 
    FROM calendarDec c 
    INNER JOIN listingsDec l ON c.listing_id = l.id 
    WHERE c.date BETWEEN ? AND ? AND c.price NOT NULL AND l.city = ?
    """