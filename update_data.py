import sqlite3
def update_data(values):
    with sqlite3.connect("Coffe_shop.db") as db:
        cursor=db.cursor()
        sql="""Update Product set Name=? ,Price=? where ProductID=?"""
        cursor.execute(sql,values)
        db.commit()
if __name__ == '__main__':
    product=("expresso",2,1)
    update_data(product)
    product=("latteee", 1.35,3)
    update_data(product)
    product=("Mochaaa", 2,4)
    update_data(product)
    product=("Green Tea",1.50,5)
    update_data(product)
    product=("Iced Tea",1.00,6)
    update_data(product)
    product=("American",1.50,7)
    update_data(product)