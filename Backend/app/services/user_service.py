import pymysql

def register_user(user,db):
    try:
    
        with db.cursor() as cursor:
            cursor.execute("SELECT id from users where email = %s",(user.email,))
            existing_user = cursor.fetchone()
            if existing_user:
                raise LookupError("Email already exists")
            
            cursor.execute("INSERT INTO users (name,email,password) VALUES (%s,%s,%s)",(user.name,user.email,user.password))
            db.commit()
            return {
                "message":"user registered successfully"
            }
        
    except pymysql.MySQLError:
        db.rollback()
        raise RuntimeError("Db failed")

def login_user(user,db):
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT id,name,password from users where email = %s",(user.email,))
            loginuser = cursor.fetchone()
            print("DB ROW:", loginuser)
            if not loginuser:
                raise ValueError("invalid email or password")
            db_password = loginuser["password"]

            if user.password.strip() != db_password :
                raise ValueError("invalid email or password")
            return{
                "message":"login successfull",
                "user_id": loginuser["id"],
                "name":loginuser["name"]
            }
               
    except pymysql.MySQLError:
        raise RuntimeError("Dbfailed")