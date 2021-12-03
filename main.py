import sqlite3
from sqlite3 import Error

# константа, (если переменная начинается с большой буквы ее лучше не менять)
PATH = 'testdb.db'
table = input('введите название таблицы которую хотите удалить: ')
def create_connection():
    connection = None
    try:
        connection = sqlite3.connect(PATH)
        print('пробую подключиться к базе данных')
    except Error as e:
        print('не удалось подключиться к базу данных', e)
    else:
        print('подключение прошло успешно')
    return connection

conn = create_connection()

def del_table(connection):
    cursor = connection.cursor()
    quary_del_table = f'DROP TABLE {table}'
    cursor.execute(quary_del_table)
    print(f'таблица {inp} была удалена успешно')


inp = input(f'удалить таблицу {table}? (да/нет): ')
if inp == 'да':
    dt = del_table(conn)
else:
    print('отмена')