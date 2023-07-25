import sqlite3
cnt = sqlite3.connect('store.db')



# ---------------------------- Creates products table --------------------------

#sql = ''' CREATE TABLE products (
##id INTEGER PRIMARY KEY,
##pname CHAR(30) NOT NULL,
##price INTEGER NOT NULL,
##qnt INTEGER NOT NULL)
##'''
##cnt.execute(sql)



# ---------------------------- insert new products --------------------------

##sql = '''
##INSERT INTO products (pname, price, qnt)
##VALUES
##('dell laptop', 500, 7 )
##'''
##cnt.execute(sql)
##cnt.commit()


# ----------------------------  Create cart table --------------------------

sql = ''' CREATE TABLE cart (
id INTEGER PRIMARY KEY,
uid INTEGER NOT NULL,
pid INTEGER NOT NULL,
qnt INTEGER NOT NULL)
'''
cnt.execute(sql)




