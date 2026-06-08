from fastapi import FastAPI
import mysql.connector
# from coding_ex.setup_messages import cursor
def get_connection():
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
    cursor.execute("DESCRIBE messages")
    rows=cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            "field_name": row[0],
            "data_type": row[1],
            "allow_null": row[2],
            "key_type": row[3]
        }
        for row in rows
    ]
def get_all_messages():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT id, unit, classification, content, source, created_at FROM messages")
    rows=cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            "id": row[0],
            "unit": row[1],
            "classification": row[2],
            "content": row[3],
            "source": row[4],
            "created_at": str(row[5])
        }
        for row in rows
    ]

def add_massage(data:dict):
    conn=get_connection()
    cursor=conn.cursor()
    sql="INSERT INTO messages (unit,classification,content,source) VALUES (%s,%s,%s,%s)"
    values=(data["unit"],data["classification"],data["content"],data["source"])
    cursor.execute(sql,values)
    conn.commit()
    new_id=cursor.lastrowid
    cursor.close()
    conn.close()
    return new_id
def get_specific_message(id:int):
    pass
def update_specific_message(id:int):
    pass
def delete_specific_massage(id:int):
    pass