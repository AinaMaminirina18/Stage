import mysql.connector

connection = mysql.connector.connect(
    user='root',
    password='Asecna2024',
    host='localhost',
    database='login')

mycursor = connection.cursor()

sql_create = "INSERT INTO entry (user , password) VALUES ('Admin', 'Asecna2024')"
sql_delete = "DELETE FROM entry WHERE user='Mamy' and password='Maminirina' IF EXISTS"
sql_update = "UPDATE entry SET user='Admin' WHERE password='Asecna2024'"
sql_create2 = "CREATE TABLE data (id INT PRIMARY KEY , date TIMESTAMP NOT NULL, categorie VARCHAR(50), nom VARCHAR(100), scat VARCHAR(50), hdebut INT NOT NULL , hfin INT NOT NULL)"
mycursor.execute(sql_delete)
connection.commit()