import mysql.connector
from setup import cursor

def get_connection():
    """

    :return:
    """
    return mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="secret",
    database="soldiers_db"
    )

def get_schema():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("DESCRIBE soldiers")
    rows=cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"column":row[0],"type":row[1]} for row in rows]
def get_all():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM soldiers")
    rows=cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
def get_by_id(soldier_id):
    conn=get_connection()
    cursor.conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM soldiers where id=%s",(soldier_id,))
    row = cursor.fetchall()
    cursor.close()
    conn.close()
    return row

def create(name,soldier_rank,unit,active=True):
    """"

    """
    conn=get_connection()
    cursor=conn.cursor()
    sql="INSERT INTO soldiers (name,soldier_rank,unit,active) VALUES (%s,%s,%s)"
    values=(name,soldier_rank,unit,active)
    cursor.execute(sql,values)
    conn.commit()
    new_id=cursor.lastrowid
    cursor.close()
    conn.close()
