insert_user = "INSERT INTO USERS(User_ID, Password, Email_Address, First_Name, Last_Name) VALUES(%s, %s, %s, %s, %s)"

get_user_id = "SELECT Max(User_ID)+1 AS \"User_ID\" FROM USERS"
get_user = "SELECT * FROM USERS WHERE User_ID = %s"
get_customer_id = "SELECT CUSTOMERID FROM CUSTOMER"

authenticate_user = "SELECT * FROM USERS WHERE Email_Address = %s AND Password = %s"


