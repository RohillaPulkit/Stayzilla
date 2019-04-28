# get_states = 'SELECT DISTINCT upper(state) AS \"state\" FROM listing;'

get_location_percent = "SELECT round(COUNT(*) * 100/(select count(*) from listing),2) as percent, state" \
                       " FROM (SELECT distinct(listing.id), state FROM LISTING" \
                       " JOIN BOOKING ON booking.listing_id = listing.id " \
                       "where listing.id in(SELECT DISTINCT listing_id from booking) " \
                       "order by listing.id desc) " \
                       "group by state;"

get_chart_data = " select TO_CHAR(TO_DATE(mon, 'MM'), 'Mon') as Mont,bookingprice as booking, state "\
                 "from (select mon ,round(avg(price)) as bookingprice, state  "\
                 "from (select Round((total_price/(total_guests * no_of_days)),2) as price,mon, state "\
                 "from(select state, Round(SUM(price),2)as total_price, " \
                 "Round(Sum(number_of_guests),2) as total_guests,id,mon," \
                 " sum(number_of_days) as no_of_days "\
                "from(select listing.id, price, state, number_of_guests ," \
                 " extract(MONTH FROM CHECK_IN) as mon,(check_out-check_in) as number_of_days "\
                "  from booking join listing on booking.listing_id = listing.id) "\
                " group by id,mon,state "\
                " ))group by mon, state order by mon ) "\
                " WHERE state = %s;"

get_all_states = "select distinct state as state from listing order by state ASC;"


get_single_private_rooms = " select count(*) as SINGLEPRIVATEROOM from(select room_type from listing " \
                           "where state = %s)where room_type = 'Private room'"

get_entire_apt = " select count(*) as ENTIREROOMS from(select room_type from listing " \
                           "where state = %s)where room_type = 'Entire home/apt'"

get_single_shared_rooms = " select count(*) as SHAREDROOMS from(select room_type from listing " \
                           "where state = %s)where room_type = 'Shared room'"

get_max_state_month = "select state as STATE from(select count(*) as number_of_booking, state, mon " \
                 "from( select extract(MONTH FROM CHECK_IN) as mon,listing_id, state " \
                 "from booking join listing on booking.listing_id = listing.id)" \
                 " group by mon, state) order by number_of_booking desc " \
                 "fetch first 1 row only;"

get_best_home ="select id as ID from(select id, (price/nog) as priceperguest, review from(select listing.id as id," \
               " sum(price)as price, sum(number_of_guests) as nog, sum(score) as review from booking " \
               "join listing on booking.listing_id = listing.id " \
               "join review on review.listing_id = booking.listing_id " \
               "group by listing.id)) order by priceperguest asc, " \
               "review desc fetch first 1 row only"

get_best_host = "select first_name||''||last_name as HOST from users " \
                "where users.user_id in" \
                "(select host from (select sum(price) as max_profit, host.host_id as host" \
                " from listing join host on host.host_id = listing.host_id" \
                " join booking on booking.listing_id = listing.id " \
                "group by host.host_id order by max_profit desc " \
                "fetch first 1 row only))"

get_least_avail = "select first_name||' '||last_name as NAME from users " \
                  "where users.user_id in (select host_id " \
                  "from listing where id in( select id from " \
                  "( select count(availability_date) as available, available.listing_id as id " \
                  "from available join listing on listing.id = available.listing_id " \
                  "where is_available = 1 " \
                  "group by available.listing_id " \
                  "order by available desc " \
                  "fetch first 1 row only)));"

get_info = "SELECT 'Listing' AS NAME, COUNT(*) AS Count FROM LISTING UNION " \
           "SELECT 'Review' AS NAME, COUNT(*) AS Count FROM REVIEW UNION " \
           "SELECT 'Booking' AS NAME, COUNT(*) AS Count FROM BOOKING UNION " \
           "SELECT 'Available' AS NAME, COUNT(*) AS Count FROM AVAILABLE UNION " \
           "SELECT 'Host' AS Name,COUNT(*) AS Count FROM HOST UNION " \
           "SELECT 'Customer' AS Name, COUNT(*) AS Count FROM CUSTOMER UNION " \
           "SELECT 'Users' AS NAME , COUNT(*) AS Count FROM USERS;"

get_profit = ""
# get_profit = "select (sum(price)* 0.1) as profit, yea as yr from
# (select price,extract(YEAR FROM CHECK_IN) as yea
# from booking)
# group by yea;
# "