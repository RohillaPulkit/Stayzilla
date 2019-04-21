insert_booking = "INSERT INTO BOOKING(ID, LISTING_ID, CUSTOMER_ID, CHECK_IN, CHECK_OUT, PRICE, NUMBER_OF_GUESTS)" \
                 " VALUES(:1, :2, :3, :4, :5, :6, :7);"

get_listing_id = "SELECT ID FROM LISTING;"

