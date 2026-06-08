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
    """
    get the schema of the tabel
    :return: the schema
    """
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
    """
    get all the messages
    :return: return all the messages in the repository
    """
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
    """
    add new message to our sql tabel
    :param data: new data to insert
    :return: the new id of the data
    """
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
    """
    get a specific message
    :param id:the id of message to get
    :return: the specific message
    """
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    sql="SELECT * FROM messages WHERE id=%s"
    cursor.execute(sql,(id,))
    row=cursor.fetchall()
    cursor.close()
    conn.close()
    return row
def update_specific_message(id:int,data:dict):
    """
    update specific message data
    :param id: message to update
    :param data: new data to update
    :return: the number of messages changed
    """
    conn=get_connection()
    cursor=conn.cursor()
    # cursor.execute("DESCRIBE messages")
    set_part=[f"{key}=%s" for key in data.keys()]
    set_clause=",".join(set_part)
    sql=f"UPDATE messages SET {set_clause} WHERE id= %s"
    values=list(data.values())+[id]
    cursor.execute(sql,values)
    conn.commit()
    changed=cursor.rowcount>0
    cursor.close()
    conn.close()
    return changed

def delete_specific_message(id:int):
    """
    delete a specific message from database
    :param id: message id to remove
    :return: update database without the message id
    """
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM messages WHERE id=%s",(id,))
    conn.commit()
    deleted=cursor.rowcount>0
    cursor.close()
    conn.close()
    return True if deleted else False
def return_messages_unit(unit_name):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * from messages where unit=%s",(unit_name,))
    all_unit=cursor.fetchall()
    cursor.close()
    conn.close()
    return all_unit