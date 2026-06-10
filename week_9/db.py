import mysql.connector
from setup import cursor
import uvicorn

def get_connection():
    """
    connecting to mysql localhost
    :return: the specific tabel in DATABASE
    """
    return mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="secret",
    database="soldiers_db"
    )

def get_schema():
    """
    get the soldier tabel and return his structure
    :return: the structure of soldier table
    """
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("DESCRIBE soldiers")
    rows=cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            "field_name":row[0],
            "type":row[1],
            "allow_null":row[2],
            "key_type":row[3]
         }
        for row in rows
    ]

def get_all():
    """"
    return all the soldiers exists in the tabel
    """
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM soldiers")
    rows=cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_by_id(soldier_id):
    """"
    return soldier by his id
    """
    conn=get_connection()
    cursor.conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM soldiers where id=%s",(soldier_id,))
    row = cursor.fetchall()
    cursor.close()
    conn.close()
    return row

def create(name,soldier_rank,unit,active=True):
    """"
    create a row in sql tabel
    """
    conn=get_connection()
    cursor=conn.cursor()
    sql="INSERT INTO soldiers (name,soldier_rank,unit,active) VALUES (%s,%s,%s,%s)"
    values=(name,soldier_rank,unit,active)
    cursor.execute(sql,values)
    conn.commit()
    new_id=cursor.lastrowid
    cursor.close()
    conn.close()

def update(soldier_id:int,data:dict):
    """
    update data of specific soldier
    :param soldier_id: soldier to update values
    :param data: new data to update
    :return: false if there is no update, else true
    """
    conn=get_connection()
    cursor=conn.cursor()
    set_parts=[f"{key}=%s" for key in data.keys()]
    set_clause=",".join(set_parts)
    sql=f"UPDATE soldiers SET {set_clause} WHERE id = %s"
    values=list(data.values())+[soldier_id]
    cursor.execute(sql,values)
    conn.commit()
    changed=cursor.rowcount>0
    cursor.close()
    conn.close()
    return changed

def delete(soldier_id):
    """"
    delete a specific soldier from soldiers data base
    :return: true if delete success,else false
    """
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM soldiers WHERE id = %s",(soldier_id,))
    conn.commit()
    deleted=cursor.rowcount>0
    cursor.close()
    conn.close()
    return deleted

def get_names_and_ranks():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT name,soldier_rank FROM soldiers")
    rows=cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_by_rank(rank:str):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM soldiers WHERE soldier_rank=%s",(rank,))
    rows=cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def search_by_name(soldier_name:str):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM soldiers WHERE name LIKE %s",(f"%{soldier_name}%",))
    rows=cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_active_sorted(order:str="asc"):
    if order.lower()not in ("asc","desc"):
        order="asc"
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM soldiers WHERE active=TRUE ORDER BY name {order.upper()}")
    rows=cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
def get_distinct_units():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT DISTINCT unit FROM soldiers")
    rows=cursor.fetchall()
    if not rows:
        raise("Error the DataBase soldiers is empty")
    cursor.close()
    conn.close()
    return [row[0] for row in rows]

def get_with_missing_rank():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM soldiers WHERE soldier_rank is NULL")
    row=cursor.fetchall()
    cursor.close()
    conn.close()
    return row

if __name__=="__main__":
    pass