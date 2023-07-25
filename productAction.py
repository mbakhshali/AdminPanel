import sqlite3
cnt = sqlite3.connect('store.db')

def getAllProducts ():
    sql = '''
SELECT * FROM products
'''
    result = cnt.execute(sql)
    rows = result.fetchall()
    return rows


def getUserCart(session):
    sql = '''
    SELECT cart.qnt, products.pname, products.price
    FROM cart INNER JOIN products ON cart.pid = products.id
    WHERE cart.uid = ?
    '''
    result = cnt.execute(sql, (session,))
    rows = result.fetchall()
    return rows
    


def shopValidate (pid, qnt):
    if pid == "" or qnt == "":
        return False, 'Please fill in all the fields!'
    
    sql = '''
        SELECT * FROM products WHERE id = ?
        '''
    result = cnt.execute(sql, (pid,))
    row = result.fetchone()

    if not row:
        return False, 'Product not found! Wong ID.'

    sql = ''' SELECT * FROM products WHERE id = ? AND qnt>= ? '''
    result = cnt.execute(sql, (pid, qnt))
    row = result.fetchone()
    if not row:
        return False, "Not enough quantity!"


    return True, ""




def savetocart(session, pid, qnt):
    sql = ''' INSERT INTO cart (uid, pid, qnt) VALUES (?, ?, ?) '''
    cnt.execute(sql, (session, pid, qnt))
    cnt.commit()


def updateqnt(pid, qnt):
    sql = ''' UPDATE products SET qnt = qnt - ? WHERE id = ?'''
    cnt.execute(sql, (qnt, pid))
    cnt.commit()




def addProduct(pname, price, qnt):
    sql = '''
    INSERT INTO products (pname, price, qnt)
    VALUES
    (?, ?, ?)
    '''
    try:
        if not pname == "" and not price == "" and not qnt == "":
            try:
                price = int(price)
                qnt = int(qnt)
            except:
                return False, "Please pay attention to type of the required values"

            if qnt <= 0 :
                return False, "Quantity must be greater than 0!"

            cnt.execute(sql, (pname, price, qnt))
            cnt.commit()
            return True, ""
        else:
            return False, "Fill in all the fields"
    except:
        return False, "Database Error!"


        
def updateQNT(id, qnt):
    sql = '''
    UPDATE products SET qnt = ? WHERE id = ?
    '''
    if not id == "" and not qnt == "":

        try:
            try:
                qnt = int(qnt)
                id = int(id)
            except:
                return False, 'Wrong Values', 'red'

            if qnt < 0:
                return False, "Invalid Numbers.", 'red'

            result = cnt.execute(sql, (qnt, id))
            counter = result.rowcount
            if counter == 1:
                cnt.commit()
                return True, 'Quantity Successfully Updated', 'green'
            else:
                return False, 'No Product Found. Check the ID.', 'red'

        except:
            return False, "Database Error", 'red'
    else:
        return False, "All the fields are required", 'red'