import logging

import mysql.connector
from logging import Logger

class IntelMessagesDAL:
    VALID_CLASSIFICATIONS=('unclassified','confidential','secret','top_secret')

    def __init__(self, host: str, port: int, user: str, password: str, database: str,logger: Logger):
        self._host=host
        self._port=port
        self._user=user
        self._password=password
        self._database=database
        self._logger=logger

    def get_conn(self):
        self._logger.info("enter to get_conn function in DAL")
        conn=mysql.connector.connect(
            host=self._host,
            port=self._port,
            user=self._user,
            password=self._password,
            database=self._database
        )
        return conn

    def setup(self):
        self._logger.info("enter to setup function in DAL")
        conn=self.get_conn()
        cursor=conn.cursor()
        sql="""CREATE TABLE IF NOT EXISTS messages(
                id INT PRIMARY KEY AUTO_INCREMENT,
                unit VARCHAR(100) NOT NULL,
                classification  ENUM('unclassified','confidential','secret','top_secret'),
                content TEXT NOT NULL,
                source VARCHAR(100),
                created_at DATETIME DEFAULT NOW()
            )"""
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    def get_schema(self):
        self._logger.info("enter to get_schema function in DAL")
        conn=self.get_conn()
        cursor=conn.cursor()
        cursor.execute(f"DESCRIBE messages")
        rows=cursor.fetchall()
        cursor.close()
        conn.close()
        return [
            {
                "field_name": row[0],
                "type": row[1],
                "allow_null": row[2],
                "key_type": row[3]
            }
            for row in rows
        ]
    def get_all(self):
        self._logger.info("enter to get_all function in DAL")
        conn=self.get_conn()
        cursor=conn.cursor(dictionary=True)
        sql="SELECT * FROM messages"
        cursor.execute(sql)
        # self._logger.info("enter to get_all function in DAL")
        rows=cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    def get_by_id(self,message_id:int):
        self._logger.info("enter to get_by_id function in DAL")
        conn=self.get_conn()
        cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM messages where id=%s",(message_id,))
        row=cursor.fetchall()
        cursor.close()
        conn.close()
        return row

    def create(self, unit: str, classification: str, content: str, source: str| None):
        self._logger.info("enter to create function in DAL")
        conn=self.get_conn()
        cursor=conn.cursor()
        sql="INSERT INTO messages (unit,classification,content,source) VALUES (%s,%s,%s,%s)"
        values=(unit,classification,content,source)
        cursor.execute(sql,values)
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return new_id

    def update(self, message_id: int, data:dict):
        self._logger.info("enter to update function in DAL")
        conn=self.get_conn()
        cursor=conn.cursor()
        set_parts = [f"{key}=%s" for key in data.keys()]
        set_clause = ",".join(set_parts)
        sql = f"UPDATE soldiers SET {set_clause} WHERE id = %s"
        values = list(data.values()) + [message_id]
        cursor.execute(sql, values)
        conn.commit()
        changed = cursor.rowcount > 0
        cursor.close()
        conn.close()
        return changed

    def delete(self,message_id):
        self._logger.info("enter to delete function in DAL")
        conn=self.get_conn()
        cursor=conn.cursor()
        cursor.execute("DELETE FROM messages WHERE id=%s",(message_id,))
        conn.commit()
        deleted=cursor.rowcount>0
        if deleted:
            self._logger.info(f" Message with ID {message_id} was deleted")
        else:
            self._logger.warning(f"Message with ID {message_id} was not found")
        cursor.close()
        conn.close()
        return deleted

    def get_by_unit(self,unit:str):
        conn=self.get_conn()
        cursor=conn.cursor(dictionary=True)
        sql="SELECT * FROM messages WHERE unit=%s"
        cursor.execute(sql,(unit,))
        row=cursor.fetchall()
        cursor.close()
        conn.close()
        return row

    def get_by_classification(self, classification: str):
        if classification not in self.VALID_CLASSIFICATIONS:
            return None
        conn = self.get_conn()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM messages WHERE classification=%s"
        cursor.execute(sql, (classification,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    def get_by_unit_and_classification(self, unit: str, classification: str):
        conn = self.get_conn()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM messages WHERE classification=%s AND unit=%s"
        cursor.execute(sql, (classification,unit))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    def get_distinct_units(self):
        conn = self.get_conn()
        cursor = conn.cursor()
        sql = "SELECT DISTINCT unit FROM messages"
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [row[0] for row in rows]

    def search_content(self, term: str):
        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM messages WHERE content LIKE %s",(f"%{term}%",))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    def get_missing_source(self):
        conn = self.get_conn()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM messages WHERE source IS NULL")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

