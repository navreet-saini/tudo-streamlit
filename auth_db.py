import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    port=3306,
    username="root",
    password="123456",
    database="internship"

)
csr=conn.cursor()