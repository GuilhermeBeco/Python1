import sqlite3
def delete_data(values):
    with sqlite3.connect("Coffe_shop.db") as db:
        cursor=db.cursor()
        sql="""Delete from Product where ProductID=?"""
        cursor.execute(sql,values)
        db.commit()
if __name__ == '__main__':
    product=("2")
    delete_data(product)
