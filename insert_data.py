import sqlite3
def insert_data(values):
    with sqlite3.connect("Coffe_shop.db") as db:
        cursor=db.cursor()
        sql="""insert into Product (Name,Price) values (?,?) """
        cursor.execute(sql,values)
        db.commit()
if __name__ == '__main__':
    product=("expresso",1.5)
    insert_data(product)
    product=("latte", 1.35)
    insert_data(product)
    product=("Mocha", 2.4)
    insert_data(product)
    product=("Green Tea",1.20)
    insert_data(product)
    product=("Black Tea",1.00)
    insert_data(product)
    product=("Americano",1.50)
    insert_data(product)