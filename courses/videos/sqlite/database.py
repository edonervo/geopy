import sqlite3

def main():
    # Create a connectiomn
    # conn = sqlite3.connect(':memory:') # NOT PERMANENT
    conn = sqlite3.connect('customer.db')  # PERMANENT 

    # Create a c
    c = conn.cursor() # Single cursor

    many_customers = [
        ('Wes', 'Brown', 'wes@gmail.com'),
        ('Steph', 'Kuwe', 'steph@gmail.com'),
        ('Edo', 'Ner', 'edo@gmail.com')
        ] # data can be inserted with python tuples

    # CREATE a table
    # ------------------------------
    # c.execute("""
    #     CREATE TABLE customers (
    #           first_name text, 
    #           last_name text,
    #           email text
    #     )
    # """)
    # -------------------------------

    # INSERT data in the table
    # -------------------------------
    # c.execute('INSERT INTO customers VALUES ("John", "Elder", "john@gmail.com")')
    # c.execute('INSERT INTO customers VALUES ("Tim", "Smith", "tim@gmail.com")')
    # c.execute('INSERT INTO customers VALUES ("Mary", "Brown", "mary@gmail.com")')
    # -------------------------------

    # -------------------------------
    # c.executemany('INSERT INTO customers VALUES (?, ?, ?)', many_customers)
    # -------------------------------

    # FORMATTIN EXAMPLES
    # ------------------------------- 
    # c.execute('SELECT * FROM customers')
    # print(c.fetchone())
    # print(c.fetchmany(3))
    # print(c.fetchall())
    # items = c.fetchall()

    # print("NAME" + '\t' + 'SURNAME' + '\t' + 'EMAIL')
    # print('----------------------------------')
    # for item in items:
    #     print(item[0] + '\t ' + item[1] + '\t' + item[2])
    # -----------------------------------

    # PRIMAREY KEYS
    # -----------------------------------
    # c.execute('SELECT rowid, * FROM customers')

    # items = c.fetchall()

    # for item in items:
    #     print(item)
    # -----------------------------------

    # WHERE CLAUSE
    # -----------------------------------
    # c.execute('SELECT * FROM customers WHERE last_name LIKE "Br%"')

    # items = c.fetchall()

    # for item in items:
        # item
    # -----------------------------------

    # UPDATE RECORDS - better to use id
    # -----------------------------------
#     c.execute("""
#         UPDATE customers SET first_name = "BoB"
#         WHERE last_name = "Elder"
# """)

#     c.execute('SELECT rowid, * FROM customers')

#     items = c.fetchall()

#     for item in items:
#         print(item)
    # -----------------------------------

    # DELETE records
    # -----------------------------------
#     c.execute("""
#         DELETE from customers WHERE rowid = 6
# """)

#     c.execute('SELECT rowid, * FROM customers')

#     items = c.fetchall()

#     for item in items:
#         print(item)
    # -----------------------------------


    # ORDER results with Order By
    # -----------------------------------

    # c.execute('SELECT rowid, * FROM customers ORDER BY last_name DESC')

    # items = c.fetchall()

    # for item in items:
    #     print(item)
    # -----------------------------------

    # Drop Table
    # -----------------------------------

    # c.execute('DROP TABLE customers')

    # items = c.fetchall()

    # for item in items:
    #     print(item)
    # -----------------------------------

    # APP
    

    # The commit command actually execute the commands
    conn.commit()

    # Close the connection
    conn.close()    


if __name__ == '__main__':
    main()