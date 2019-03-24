get_user_id = "SELECT Max(User_ID)+1 AS \"User_ID\" FROM USERS"
authenticate_user = "SELECT * FROM USERS WHERE Email_Address = %s AND Password = %s"
get_user = "SELECT * FROM USERS WHERE User_ID = %s"
