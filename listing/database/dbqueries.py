insert_booking = "INSERT INTO BOOKING(ID, LISTING_ID, CUSTOMER_ID, CHECK_IN, CHECK_OUT, PRICE, NUMBER_OF_GUESTS)" \
                 " VALUES(:1, :2, :3, :4, :5, :6, :7);"

get_listing_ids = "SELECT ID FROM LISTING;"
get_listing_for_id = "SELECT LISTING.*, (USERS.FIRST_NAME ||' '|| USERS.LAST_NAME) AS HOST_NAME, SCORE " \
                     "FROM LISTING, USERS, (SELECT ROUND(AVG(SCORE)/2) " \
                     "AS SCORE FROM REVIEW WHERE LISTING_ID = %s)" \
                     " WHERE ID = %s  AND USERS.USER_ID = LISTING.HOST_ID"

get_listing_reviews = "SELECT REVIEW.*, USERS.FIRST_NAME AS REVIEWER_NAME FROM REVIEW, USERS " \
                      "WHERE USERS.USER_ID = REVIEWER_ID AND Listing_id = %s ORDER BY REVIEW_DATE DESC;"

get_popularity_trend = "SELECT ROUND(AVG(BOOKINGS)) AS \"BOOKINGS\", TO_CHAR(TO_DATE(\"MON\", 'MM'), 'Mon') AS \"MONTH\"" \
                       "FROM (SELECT COUNT(*) AS BOOKINGS, " \
                       "EXTRACT(MONTH FROM CHECK_IN) AS \"MON\", " \
                       "EXTRACT(YEAR FROM CHECK_IN) AS \"YEAR\" " \
                       "FROM BOOKING WHERE LISTING_ID = %s " \
                       "GROUP BY  EXTRACT(MONTH FROM CHECK_IN), " \
                       "EXTRACT(YEAR FROM CHECK_IN)) " \
                       "GROUP BY \"MON\" " \
                       "ORDER BY \"MON\";"
