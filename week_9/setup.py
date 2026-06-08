import mysql.connector
import time
time.sleep(2)
conn=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="secret",
    database="soldiers_db"
)

cursor=conn.cursor()
create_tabel_sql="""
CREATE TABLE IF NOT EXISTS soldiers (
id INT PRIMARY KEY AUTO_INCREMENT,
name   VARCHAR(100) NOT NULL,
soldier_rank VARCHAR(50),
unit VARCHAR(100),
active BOOLEAN DEFAULT TRUE
)
"""
cursor.execute(create_tabel_sql)
conn.commit()
print("Tabel created successfully")
cursor.close()
conn.close()