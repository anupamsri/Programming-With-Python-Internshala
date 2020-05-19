import sqlite3
book=sqlite3.connect("bookstore.db")
curbook=book.cursor()
#curbook.execute('''create table books (book_id integer  primary key autoincrement , book_name text(20), author text(20), price integer);''')

while True:
    x=input("want to enter data yes/no: ")
    if x=='yes':
        book_id=int(input("Enter book id: "))
        book_name=input("Enter book name: ")
        author=input("Enter author name: ")
        price=input("Enter price of book: ")
        curbook.execute("insert into books (book_id,book_name,author, price) values(?,?,?,?);",(book_id,book_name,author, price))
        book.commit()
        print("data add successfully")

    else:
        break
    




#book.close()
