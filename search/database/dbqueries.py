search_customer_listing = \
" WITH "\
   " DATES AS "\
   "(SELECT "\
   " TO_DATE(%s, 'DD-MM-YY') - 1 + rownum AS VALID_DATE "\
   " FROM all_objects "\
   " WHERE TO_DATE(%s, 'DD-MM-YY') - 1 + rownum <= TO_DATE(%s, 'DD-MM-YY')) "\
" SELECT LTABLE.ID AS LISTING_ID, LTABLE.NAME, SUBSTR(LTABLE.DESCRIPTION,0,60)AS DESCRIPTION, PRI_SCORE.PRICE, PRI_SCORE.SCORE "\
"FROM "\
"(SELECT LISTING.ID, LISTING.NAME, LISTING.DESCRIPTION FROM LISTING WHERE LISTING.CITY = %s AND " \
    "LISTING.ACCOMMODATES >= %s) LTABLE "\
"JOIN "\
"(SELECT "\
   " A.LISTING_ID, "\
   " A.PRICE, "\
   " B.SCORE "\
   " FROM "\
   "(SELECT "\
   "LISTING_ID,  "\
   "round(AVG(PRICE)) AS PRICE "\
   "FROM AVAILABLE, DATES "\
   "WHERE AVAILABLE.AVAILABILITY_DATE = DATES.VALID_DATE "\
   "AND AVAILABLE.IS_AVAILABLE = 1 "\
   "GROUP BY LISTING_ID "\
   "ORDER BY LISTING_ID) A "\
   "JOIN "\
   "(SELECT "\
        "LISTING_ID, "\
        "ROUND(AVG(SCORE)) AS SCORE "\
        "FROM REVIEW "\
        "GROUP BY "\
        "LISTING_ID) B "\
   "ON A.LISTING_ID = B.LISTING_ID "\
   "ORDER BY A.LISTING_ID "\
")PRI_SCORE "\
"ON LTABLE.ID = PRI_SCORE.LISTING_ID"