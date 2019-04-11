import sqlite3
def delete_data():
    with sqlite3.connect("Coffe_shop.db") as db:
        cursor=db.cursor()
        sql="""Select * from Product"""
        cursor.execute(sql)
        products=cursor.fetchall()
        for prod in products:
            print(prod)
        i=input("Wich prod do you want to delete: ")

        sql="""Delete from Product where ProductID=?"""
        cursor.execute(sql,i)
        sql = """Select * from Product"""
        cursor.execute(sql)
        products = cursor.fetchall()
        for prod in products:
            print(prod)
        db.commit()
if __name__ == '__main__':
    delete_data()
