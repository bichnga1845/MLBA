from CONNECTMYSQLBENCH.connectdatabase import conn

cursor = conn.cursor()

sql="insert into student (code,name,age) values (%s,%s,%s)"

val=("sv05","Trần Duy Thanh",45)

cursor.execute(sql,val)

conn.commit()

print(cursor.rowcount," record inserted")

cursor.close()