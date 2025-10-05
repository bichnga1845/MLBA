import mysql

from CONNECTMYSQLBENCH.connectdatabase import server, port, database, username, password

conn = mysql.connector.connect(
                host=server,
                port=port,
                database=database,
                user=username,
                password=password)
cursor = conn.cursor()
sql = "DELETE from student where ID=%s"
val = (5,)

cursor.execute(sql, val)

conn.commit()

print(cursor.rowcount," record(s) affected")