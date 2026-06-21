import mysql.connector
def get_connection():
    return mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="secret",
    database="soldiers_db"
    )
def get_summary():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM soldiers")
    total=cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) AS active FROM soldiers WHERE active=TRUE")
    count_active=cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return {"total":total,"active":count_active,"inactive":total-count_active}

def count_by_units():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    sql="SELECT unit,COUNT(*) AS total FROM soldiers GROUP BY unit ORDER BY total DESC"
    cursor.execute(sql)
    rows=cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_mising_data():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    sql = "SELECT * FROM soldiers WHERE soldier_rank IS NULL"
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_units_with_multiple_soldiers():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    sql = "SELECT unit,COUNT(*) AS total FROM soldiers GROUP BY unit HAVING total>1"
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [row["unit"] for row in rows]