import mysql.connector

server="localhost"
port=3306
database="studentmanagement"
username="BichNga"
password="@Bichnga184"

conn = mysql.connector.connect(
                host=server,
                port=port,
                database=database,
                user=username,
                password=password)
