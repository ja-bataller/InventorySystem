import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="admin"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE TUP-C UITC INVENTORY SYSTEM [DATABASE]")