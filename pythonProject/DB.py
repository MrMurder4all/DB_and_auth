import cx_Oracle
import csv
from datetime import datetime

# Параметры подключения
dsn = cx_Oracle.makedsn("localhost", 1521, sid="XE")
user = "C##PROG"
password = "password"

# Имя файла
current_date = datetime.now().strftime("%d.%m.%Y")
file_name = f"report_{current_date}.csv"

# Подключение к базе данных и выполнение запроса
connection = cx_Oracle.connect(user=user, password=password, dsn=dsn)
cursor = connection.cursor()

# SQL-запрос для получения необходимых данных
query = """
SELECT 
    c.First_Name || ' ' || c.Last_Name AS Full_Name,
    cr.Credit_Number
FROM 
    CLIENT c
JOIN 
    RELATION r ON c.id = r.Client
JOIN 
    CREDIT cr ON r.Credit = cr.id
WHERE 
    cr.Balance > 1000
"""

cursor.execute(query)

# Открываем CSV файл для записи
with open(file_name, mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)

    # Запись заголовков столбцов
    writer.writerow(["Full_Name", "Credit_Number"])

    # Запись данных из запроса
    for row in cursor:
        writer.writerow(row)

# Закрываем соединение с базой данных
cursor.close()
connection.close()

print(f"Выгрузка завершена. Данные сохранены в файл {file_name}")
