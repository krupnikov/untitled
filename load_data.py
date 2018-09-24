import os
import _sqlite3
import time

# Функиця для генерация файла данных для загрузки в БД
def gen_data():
    file = open('data.txt', 'w')
    for i in range(1, 100000):
        d = str(i) + '\n'
        file.write(d)
    file.close()

# Создание таблицы в БД для заполнения
def create_db():
    query("""CREATE TABLE PRODUCTS
                        (id text)
                    """)

# Функция для подключения к БД и выполнения запроса
def query(sql):
    try:
        conn = _sqlite3.connect("mydata.db")
    except _sqlite3.Error as err:
        print("Error: ", err)

    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


def main():

    # Проверка доступности файла с данными
    if os.path.exists('data.txt') == False:
        gen_data()
    try:
        query("SELECT COUNT(*) FROM PRODUCTS")
    except:
        create_db()

    # Записть данных в БД
    start_time = time.clock()
    infile = open('data.txt', 'r')
    rows = infile.readlines()
    for data in rows:
        query("INSERT INTO PRODUCTS VALUES ('{0}')".format(str(data)))

    return print("Данные из файла data.txt внесены в mydata.db. Время выполнения: {0}".format(time.clock() - start_time ) + "\t" + "sek" )

if __name__ == '__main__':
    main()

