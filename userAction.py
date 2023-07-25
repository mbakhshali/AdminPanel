import sqlite3
import json

cnt = sqlite3.connect('store.db')

def user_login (user, pas):
    global cnt
    sql = ''' SELECT * FROM users WHERE username = ? AND password = ? '''
    result = cnt.execute(sql, (user, pas))
    row = result.fetchone()
    if row:
        return row[0], row[1]
    else:
        return False


def validation(user, pas, addr):
    global cnt
    if user=="" or pas == "" or addr == "":
        return False, "Fill empty fields!"
    if len(pas) > 3:
        return False, "Password length error!"
    
    sql = ''' SELECT * FROM users WHERE username = ? '''
    result = cnt.execute(sql, (user, ))
    row = result.fetchone()
    if row:
        return False, "User already exists!"
    
    return True, ""
    
    

def user_submit(user, pas, address):
    global cnt
    result, errorMSG = validation(user, pas, address)

    if result:
        sql = ''' INSERT INTO users (username, password, address, grade)
VALUES (?, ?, ?, ?)'''
        cnt.execute(sql, (user, pas, address, 5))
        cnt.commit()
        return True, ""
    else:
        return False, errorMSG


def userSetting():
    try:
        with open('setting.json') as file:
            dic = json.load(file)
        return True, dic
    except:
        return False, 'File not found'




def getAllUsers():
    sql = '''
    SELECT * FROM users
    '''
    try:
        result = cnt.execute(sql)
        rows = result.fetchall()
        return True, rows
    except:
        return False, 'Database Error'


def updateUserPermissions(id, grade):
    if not id == "" and not grade == "":
        try:
            id = int(id)
            grade = int(grade)
        except:
            return False, 'Invalid Values. Try Again!'

        sql = '''
        UPDATE users SET grade = ? WHERE id = ?
        '''

        if grade <= 5 and grade >= 1:
            try:
                result = cnt.execute(sql, (grade, id))
                row_cnt = result.rowcount
                if row_cnt == 1:
                    cnt.commit()
                    return True, "User Grade Updated"
                else:
                    return False, "No User Found"

            except:
                return False, 'Database Error'
        else:
            return False, 'Invalid Grade Number'

    else:
        return False, 'Please Fill in All the Fields'
