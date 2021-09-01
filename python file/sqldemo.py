import sqlite3

if __name__ == '__main__':
    connection = sqlite3.connect('bookstore.db')
    cursor = connection.cursor()
    #cursor.execute("CREATE TABLE demo (id nvarchar(10) PRIMARY KEY,price REAL)")
    #cursor.execute( "CREATE TABLE bookstore (id varchar(255) PRIMARY KEY,Book_Name nvarchar(225), pages int,PRICE int ,AUTHOR_NAME varchar(25))")
    #cursor.execute("DELETE FROM bookstore")
    x = 'A'
    num = '978-1-47113-687-0'
    #num ='111111'
    #cursor.execute("INSERT INTO demo (id,price) VALUES (\""+x+"\",\""+num+"\")")
    #cursor.execute("INSERT INTO bookstore VALUES (\""+num+"\",\"The 7 Habits of Highly Effective Teenagers\",266,99,\"Sean Covey\")")

    #cursor.execute("DELETE FROM bookstore WHERE id =\'" + num + "\'")
    #cursor.execute("INSERT INTO bookstore VALUES (\""+num+"\",\"1\",266,99,\"J.K. Rowling\")")
    connection.commit()
    #cursor.execute("DELETE FROM bookstore")
    print(cursor.execute("SELECT * FROM bookstore WHERE id = '978-1-47113-687-0' ").fetchone())
    print(cursor.execute("SELECT COUNT (id) FROM bookstore WHERE id ='"+num+"'").fetchone())

    row =(cursor.execute("SELECT COUNT (id) FROM bookstore WHERE id = '978-1-47113-687-0'").fetchone())[0]
    print(int(row))
