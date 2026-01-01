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
