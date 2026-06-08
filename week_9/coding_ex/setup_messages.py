import mysql.connector

i_m=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="secret",
    database="soldiers_db"
)

intel_m=i_m.cursor()
create_tabel_sql="""
CREATE TABLE IF NOT EXISTS messages (
id INT PRIMARY KEY AUTO_INCREMENT,
unit VARCHAR(100) NOT NULL,
classification  ENUM('unclassified','confidential','secret','top_secret'),
content TEXT NOT NULL,
source VARCHAR(100),
created_at DATETIME DEFAULT NOW()
)
"""
intel_m.execute(create_tabel_sql)
i_m.commit()
# cursor=intel_m.cursor()
intel_m.execute("DESCRIBE messages")
intel_m.fetchall()
print("Tabel created successfully")
intel_m.close()
i_m.close()
if __name__=="__main__":
    # get_masseges()
    pass