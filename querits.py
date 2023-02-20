import sqlite3


def list_querys():
    print('''
    1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    2. Знайти студента із найвищим середнім балом з певного предмета.
    3. Знайти середній бал у групах з певного предмета.
    4. Знайти середній бал на потоці (по всій таблиці оцінок).
    5. Знайти які курси читає певний викладач.
    6. Знайти список студентів у певній групі.
    7. Знайти оцінки студентів у окремій групі з певного предмета.
    8. Знайти середній бал, який ставить певний викладач зі своїх предметів.
    9. Знайти список курсів, які відвідує студент.
    10. Список курсів, які певному студенту читає певний викладач.
    11. Середній бал, який певний викладач ставить певному студентові.
    12. Оцінки студентів у певній групі з певного предмета на останньому занятті.
''')


querys = {
    '1': 'query_1.sql',
    '2': 'query_2.sql',
    '3': 'query_3.sql',
    '4': 'query_4.sql',
    '5': 'query_5.sql',
    '6': 'query_6.sql',
    '7': 'query_7.sql',
    '8': 'query_8.sql',
    '9': 'query_9.sql',
    '10': 'query_10.sql',
    '11': 'query_11.sql',
    '12': 'query_12.sql',
}


def execute_query(sql_file: str) -> list:
    sql = ''
    with open(sql_file, 'r') as q:
        sql = q.read()
    with sqlite3.connect('SQlite_db.sqlite') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


def main():
    while True:
        command = input('enter query number or one of commands: '
                        'list querys, exit\n --->  ')
        if command in querys or 'exit' or 'list querys':
            if command == 'exit':
                exit()
            if command == 'list querys':
                list_querys()
                continue
            print(*execute_query(querys[command]))


if __name__ == '__main__':
    main()


