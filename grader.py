import sqlite3
import json

cnt = sqlite3.connect('store.db')


def check_grade(username):
    sql = '''
    SELECT * FROM users WHERE username = ?
    '''
    result = cnt.execute(sql, (username,))
    row = result.fetchone()
    grade = str(row[4])


    with open('setting.json') as file:
        dic = json.load(file)

    return dic[grade]