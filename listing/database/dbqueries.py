insert_booking = "INSERT INTO BOOKING(LISTING_ID, CUSTOMER_ID, CHECK_IN, CHECK_OUT, PRICE, NUMBER_OF_GUESTS)" \
                 " VALUES(%s, %s, TO_DATE(%s,'DD-MM-YY'), TO_DATE(%s,'DD-MM-YY'), %s, %s);"

get_listing_ids = "SELECT ID FROM LISTING;"
get_listing_for_id = "SELECT LISTING.*, (USERS.FIRST_NAME ||' '|| USERS.LAST_NAME) AS HOST_NAME, " \
                     "USERS.EMAIL_ADDRESS AS HOST_CONTACT, SCORE " \
                     "FROM LISTING, USERS, (SELECT ROUND(AVG(SCORE)/2) " \
                     "AS SCORE FROM REVIEW WHERE LISTING_ID = %s)" \
                     " WHERE ID = %s  AND USERS.USER_ID = LISTING.HOST_ID"

get_listing_reviews = "SELECT REVIEW.*, USERS.FIRST_NAME AS REVIEWER_NAME FROM REVIEW, USERS " \
                      "WHERE USERS.USER_ID = REVIEWER_ID AND Listing_id = %s ORDER BY REVIEW_DATE DESC;"

get_popularity_trend = "SELECT ROUND(AVG(BOOKINGS)) AS \"BOOKINGS\", " \
                       "TO_CHAR(TO_DATE(\"MON\", 'MM'), 'Mon') AS \"MONTH\"" \
                       "FROM (SELECT COUNT(*) AS BOOKINGS, " \
                       "EXTRACT(MONTH FROM CHECK_IN) AS \"MON\", " \
                       "EXTRACT(YEAR FROM CHECK_IN) AS \"YEAR\" " \
                       "FROM BOOKING WHERE LISTING_ID = %s " \
                       "GROUP BY  EXTRACT(MONTH FROM CHECK_IN), " \
                       "EXTRACT(YEAR FROM CHECK_IN)) " \
                       "GROUP BY \"MON\" " \
                       "ORDER BY \"MON\";"

get_monthly_price_trend = "SELECT TO_CHAR(TO_DATE(MON, 'MM'), 'Month') AS MONTH, " \
                          "ROUND(TOTAL_PRICE/TOTAL_DAYS, 2) AS PRICE " \
                          "FROM (SELECT MON, SUM(PRICE) AS TOTAL_PRICE," \
                          " SUM(NUMBER_OF_DAYS) AS TOTAL_DAYS " \
                          "FROM (SELECT EXTRACT(MONTH FROM CHECK_IN) AS MON, " \
                          "PRICE, (CHECK_OUT-CHECK_IN) AS " \
                          "NUMBER_OF_DAYS " \
                          "FROM BOOKING " \
                          "WHERE LISTING_ID = %s) " \
                          "GROUP BY MON) " \
                          "ORDER BY MON;"

get_available_dates_with_price = "SELECT TO_CHAR(AVAILABILITY_DATE, 'DD-MM-YY') AS AVAILABILITY_DATE, PRICE" \
                                " FROM AVAILABLE WHERE LISTING_ID = %s AND IS_AVAILABLE = 1;"

get_best_time_to_visit = " SELECT TO_CHAR(TO_DATE(MON, 'MM'), 'Month') AS \"MONTH\" FROM"\
                         "("\
                         "    SELECT MON, MIN(AVG_PRICE) AS PRICE, SUM(TOTAL_DAYS) AS TOTAL_DAYS FROM"\
                         "    ("\
                         "        SELECT MON, YR, ROUND(TOTAL_PRICE/TOTAL_DAYS) AS AVG_PRICE, TOTAL_DAYS  FROM"\
                         "        ("\
                         "            SELECT MON, YR, SUM(PRICE) AS TOTAL_PRICE, SUM(NUMBER_OF_DAYS) AS TOTAL_DAYS FROM"\
                         "            ("\
                         "                SELECT EXTRACT(MONTH FROM CHECK_IN) AS MON, "\
                         "                EXTRACT(YEAR FROM CHECK_IN) AS YR,"\
                         "                PRICE, (CHECK_OUT-CHECK_IN) AS NUMBER_OF_DAYS"\
                         "                FROM BOOKING WHERE LISTING_ID = %s"\
                         "            )"\
                         "            GROUP BY MON, YR"\
                         "        )"\
                         "    )"\
                         "    GROUP BY MON"\
                         "    ORDER BY TOTAL_DAYS DESC, PRICE ASC FETCH FIRST 1 ROW ONLY"\
                         ")"

get_past_weekly_price_trend = "WITH "\
    "DATES AS (SELECT UPPER_BOUND.CURRENT_DATE - ROWNUM AS VALID_DATE "\
    "FROM ALL_OBJECTS, (SELECT TO_DATE(%s, 'DD-MM-YY') AS \"CURRENT_DATE\" FROM DUAL) UPPER_BOUND WHERE  ROWNUM <= 5), "\
    "DATA_TABLE AS (SELECT ID, CHECK_IN, CHECK_OUT, (PRICE/(CHECK_OUT-CHECK_IN)) AS PRICE, "\
    "                           VALID_DATE FROM BOOKING, "\
    "                            DATES WHERE LISTING_ID =%s AND to_number(to_char(DATES.VALID_DATE, 'DDD')) "\
    "                            BETWEEN to_number(to_char(CHECK_IN, 'DDD'))"\
    "                            AND "\
    "                            to_number(to_char(CHECK_OUT, 'DDD')))"\
    "SELECT NVL(ROUND(AVG(PRICE), 2), 0) AS PRICE,"\
    "TO_CHAR(DATES.VALID_DATE, 'DD Month') AS \"DATE\" FROM "\
    "                            DATA_TABLE"\
    "                            RIGHT JOIN DATES ON DATES.VALID_DATE = DATA_TABLE.VALID_DATE"\
    "                            GROUP BY DATES.VALID_DATE"\
    "                            ORDER BY DATES.VALID_DATE;"


get_future_weekly_price_trend = "WITH "\
    "DATES AS (SELECT UPPER_BOUND.CURRENT_DATE + ROWNUM AS VALID_DATE "\
    "FROM ALL_OBJECTS, (SELECT TO_DATE(%s, 'DD-MM-YY') AS \"CURRENT_DATE\" FROM DUAL) UPPER_BOUND WHERE  ROWNUM <= 5), "\
    "DATA_TABLE AS (SELECT ID, CHECK_IN, CHECK_OUT, (PRICE/(CHECK_OUT-CHECK_IN)) AS PRICE, "\
    "                           VALID_DATE FROM BOOKING, "\
    "                            DATES WHERE LISTING_ID =%s AND to_number(to_char(DATES.VALID_DATE, 'DDD')) "\
    "                            BETWEEN to_number(to_char(CHECK_IN, 'DDD'))"\
    "                            AND "\
    "                            to_number(to_char(CHECK_OUT, 'DDD')))"\
    "SELECT NVL(ROUND(AVG(PRICE), 2), 0) AS PRICE,"\
    "TO_CHAR(DATES.VALID_DATE, 'DD Month') AS \"DATE\" FROM "\
    "                            DATA_TABLE"\
    "                            RIGHT JOIN DATES ON DATES.VALID_DATE = DATA_TABLE.VALID_DATE"\
    "                            GROUP BY DATES.VALID_DATE"\
    "                            ORDER BY DATES.VALID_DATE;"
