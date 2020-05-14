# Alex Bello
# April 30, 2020
# Database test using SQLite Database

# SQLite is a simple SQL database that does not require
# a database server.

import sqlite3
from sqlite3 import Error
from datetime import datetime


# Method to create the connection to the database.
# The cool part is you do not need to modify this method,
# it will create a connection to a database that you specify
# in the parameter.  If it does not exist, it will create it.
# If it does exist, it will open it for use.
def create_connection(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return conn


# Create the connection object to the database, "database filename" is the parameter
print("Connect to SQLite database:")
connection = create_connection("assignment13.db")


# Execute predefined write queries
# Send the query as a parameter
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


# Execute predefined read queries
# Send the query as a parameter
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


# String holds the query to create a table
create_customer_table = """
CREATE TABLE IF NOT EXISTS customer (
  cust_id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  street_address TEXT NOT NULL,
  city TEXT NOT NULL,
  state TEXT NOT NULL,
  zip_code INTEGER NOT NULL,
  
);
"""

create_book_table = """
CREATE TABLE IF NOT EXISTS book (
 book_id INTEGER PRIMARY KEY AUTOINCREMENT,
 title TEXT NOT NULL,
 author TEXT NOT NULL,
 isbn INTEGER NOT NULL,
 edition INTEGER NOT NULL,
 price INTEGER NOT NULL,
 publisher TEXT NOT NULL,
 
 );
 """

order_table = """
CREATE TABLE IF NOT EXISTS
  ordering (
  order_number INTEGER PRIMARY KEY AUTOINCREMENT,
  order_date   TEXT,
  order_total  TEXT,
  customer_id  INTEGER,
  CONSTRAINT order_fk_customer
  FOREIGN KEY (customer_id)
  REFERENCES customer (customer_id)
);
"""


order_line_item = """
CREATE TABLE IF NOT EXISTS
  order_line_item (
  order_number INTEGER,
  book_id      INTEGER,
  quantity     INTEGER,
  PRIMARY KEY (order_number, book_id),
  CONSTRAINT oli_fk_order
  FOREIGN KEY (order_number)
  REFERENCES ordering (order_number),
  CONSTRAINT oli_fk_book
  FOREIGN KEY (book_id)
  REFERENCES book (book_id)
);  
"""


# String holds the query to add data to the table
create_customer = """
INSERT INTO
  customer (cust_id, first_name, last_name, street_address, city, state, zip_code)
VALUES
  (1, 'James', 'Smith', '25 Mappleton Dr', 'Utica', 'NY', 13502),
  (2, 'Leila', 'Jones', '32 Stone Rd', Yorkville', 'NY', 13502),
  (3, 'Brigitte', 'Griffing', '35 Stone Rd', 'NY', 13502),
  (4, 'Mike', 'Colameco', '40 Teal St', 'NY', 1378),
  (5, 'Elizabeth', 'McGovern', '21 Funk Rd', 'NY', 13824);
"""

create_book = """
INSERT INTO 
 book (book_id, title, author, isbn, edition, price, publisher)
VALUES
  (1, 'Gundam', 'Tony', '15', '2', '5.99', 'Withers'),
  (2, 'Sight's of a Dryer', 'Davis', '46', '3', '10.25', 'Everette'),
  (3, 'Fitness', 'Kim', '120', '1', '12.50', 'Naples');
"""


# Execute the four queries to create the tables of the database
print("\nRun the query to create the customer table:")
execute_query(connection, create_customer_table)
print("\nRun the query to add customers to the customer table:")
execute_query(connection, create_customer)
print("\nRun the query to create the book table:")
execute_query(connection, create_book_table)
print("\nRun the query to add books to the book table:")
execute_query(connection, create_book)
print("\nRun the query to create the order table:")
execute_query(connection, create_order_table)
print("\nRun the query to add orders to the order table:")
execute_query(connection, create_order)
print("\nRun the query to create the order line table:")
execute_query(connection, create_order_line_table)
print("\nRun the query to add to the order line table:")
execute_query(connection, create_order_line)
#--------------------------------------------------#

menu = 0
menu2 = 0
menu3 = 0
menu4 = 0
menu5 = 0

while menu != 6:
    print("Choose which table you would like to work with.")
    print("1. Customers.")
    print("2. Books.")
    print("3. Orders")
    print("4. Order Lines")
    print("5. Exit menu.")
    menu = int(input(">"))

    if menu == 1:
        while menu2 != 5:
            print("This is the menu for the customers table, what would you like to do?")
            print("1. Add a new customer.")
            print("2. Modify a customer.")
            print("3. print a list of customers.")
            print("4. Delete all customers.")
            print("5. Return to the main menu.")
            menu2 = int(input(">"))

            if menu2 == 1:
                add_customer = """
                INSERT INTO
                customer (cust_id, first_name, last_name, street_address, city, state, zip)
                VALUES
                ('input', 'input', 'input', 'input', 'input', 'input', 'input');
                """

            if menu2 == 2:
                print("\nLet's change Elizabeth McGovern's last name to Smith and print all Smith's")
                update_customer_name = """
                UPDATE
                customer
                SET
                last_name = 'Smith'
                WHERE
                last_name = 'McGovern'
                """

            if menu2 == 3:
                select_customer = "SELECT * from customer"
                customer = execute_read_query(connection, select_customer)

                for customer in customer:
                    print(customer)

            if menu2 == 4:
                "DELETE FROM customer"

    if menu == 2:
        while menu3 != 5:
            print("This is the menu for the books table, what would you like to do?")
            print("1. Add a new book.")
            print("2. Modify a book")
            print("3. Print a list of books")
            print("4. Delete a book.")
            print("5. Return to the main menu")
            menu3 = int(input(">"))

            if menu3 == 1:
                add_book = """"
                INSERT INTO
                book (book_id, title, author, isbn, edition, price, publisher)
                VALUES
                ('input', 'input', 'input', 'input', 'input', 'input', 'input');
                """

            if menu3 == 2:
                print("\nLet's change Gundam's title to something less weird")
                update_book_name = """
                UPDATE
                book
                SET
                title = 'History of Mecha'
                WHERE
                title = 'gundam'
                """

            if menu3 == 3:
                select_book = "SELECT * from book"
                book = execute_read_query(connection, select_book)

                for book in book:
                    print(book)

            if menu3 == 4:
                "DELETE FROM book"

    if menu == 3:
        while menu4 != 5:
            print("This is the menu for the books table, what would you like to do?")
            print("1. Add a new order.")
            print("2. Modify an order")
            print("3. Print a list of orders")
            print("4. Delete an order.")
            print("5. Return to the main menu")
            menu3 = int(input(">"))

            if menu4 == 1:
                add_order = """"
                INSERT INTO
                order (order_number, order_date, order_total, customer_id)
                VALUES
                ('input', 'input', 'input', 'input');
                """

            if menu4 == 2:
                print("\nThis will let you change the number on an order.")
                update_order_name = """
                UPDATE
                order
                SET
                order_number = ''
                WHERE
                order_number = ''
                """

            if menu4 == 3:
                select_order = "SELECT * from order"
                order = execute_read_query(connection, select_order)

                for order in order:
                    print(order)

            if menu4 == 4:
                "DELETE FROM order"

    if menu == 4:
        while menu5 != 5:
            print("This is the menu for the books table, what would you like to do?")
            print("1. Add a new order line.")
            print("2. Modify an order line")
            print("3. Print a list of order lines")
            print("4. Delete an order line.")
            print("5. Return to the main menu")
            menu3 = int(input(">"))
