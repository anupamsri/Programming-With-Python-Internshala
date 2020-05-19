import sqlite3
book=sqlite3.connect("bookstore.db")
curbook=book.cursor()
total_price=0
while True:
    bt=input("Book Title:  ")
    sql="select *from books where book_name='"+bt+"';"
    curbook.execute(sql)
    record=curbook.fetchone()
    print(record)
    n=int(input("No. of copies: "))
    total_price=total_price+record[3]*n
    add_book=input("Add more books? Y/N ")
    if add_book=='N':
        break
print("Total Cost {}".format(total_price))
n=input("enter to exit")
book.close()
