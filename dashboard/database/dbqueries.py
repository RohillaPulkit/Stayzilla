# get_states = 'SELECT DISTINCT upper(state) AS \"state\" FROM listing;'

get_location_percent = "SELECT round(COUNT(*) * 100/(select count(*) from listing),2) as percent, state" \
                       " FROM (SELECT distinct(listing.id), state FROM LISTING" \
                       " JOIN BOOKING ON booking.listing_id = listing.id " \
                       "where listing.id in(SELECT DISTINCT listing_id from booking) " \
                       "order by listing.id desc) " \
                       "group by state;"

get_chart_data = "select TO_CHAR(TO_DATE(mon, 'MM'), 'Mon') as Mont," \
                 " booking from(select mon, count(booking) as booking from" \
                 "(select extract" \
                 "(MONTH FROM CHECK_IN) as mon, booking.listing_id as booking FROM BOOKING) " \
                 "group by mon order by mon);"

get_single_private_rooms = "SELECT count(*) as singlePrivateRoom from listing " \
                   "where room_type = 'Private room' group by room_type;"

get_entire_apt = "SELECT count(*) as ENTIREROOMS from listing" \
                 " where room_type = 'Entire home/apt' group by room_type;"

get_single_shared_rooms = "SELECT count(*) as SharedRooms from listing " \
                   "where room_type = 'Shared room' group by room_type;"
