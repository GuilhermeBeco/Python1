import sqlite3
def select_data():
    with sqlite3.connect("Coffe_shop.db") as db:
        cursor = db.cursor()
        sql = """Select * from Product"""
        cursor.execute(sql)
        products = cursor.fetchall()
        for prod in products:
         print(prod)

def delete_data():
    with sqlite3.connect("Coffe_shop.db") as db:
        cursor=db.cursor()
        print("From the following, select one to delete: ")
        select_data()
        i=input(": ")
        sql="""Delete from Product where ProductID=?"""
        cursor.execute(sql,i)
        sql = """Select * from Product"""
        cursor.execute(sql)
        products = cursor.fetchall()
        for prod in products:
            print(prod)
        db.commit()
def update_data():
    with sqlite3.connect("Coffe_shop.db") as db:
        cursor=db.cursor()
        print("From the following, select one to edit: ")
        select_data()
        i = input(": ")
        name=input("Wich is the name of the product: ")
        price=input("Wich is the price of the product: ")
        sql="""Update Product set Name=? ,Price=? where ProductID=?"""
        values=[name,price,i]
        cursor.execute(sql,values)
        db.commit()
def insert_data():
    with sqlite3.connect("Coffe_shop.db") as db:
        cursor=db.cursor()
        name = input("Wich is the name of the product: ")
        price = input("Wich is the price of the product: ")
        sql="""insert into Product (Name,Price) values (?,?) """
        values=[name,price]
        cursor.execute(sql,values)
        db.commit()
def create_table(db_name,sql,table_name):
    with sqlite3.connect(db_name) as db:
        cursor=db.cursor()
        cursor.execute("Select name from sqlite_master where name=?",(table_name,))
        result=cursor.fetchall()
        keep_table=True
        if len(result)==1:
            response=int(input("the table {0} already exists, do you wish to recreate it (1/0)".format((table_name))))
            if response==1:
                keep_table=False
                print("The table will be created, all data will be deleted")
                cursor.execute("Drop table if exists {0}".format(table_name))
            else:
                print("The existing table was kept")
        else:
            keep_table=False
        if not keep_table:
            cursor.execute(sql)
            db.commit()
if __name__ == '__main__':
    end=False
    while(not end):
        print("1- (Re)Create DB")
        print("2- Add new prod")
        print("3- Edit prod")
        print("4- Delete prod")
        print("5- Show all prods")
        print("0- Exit")
        opt=int(input("Wich is your option: "))
        if opt==1:
            db_name = "Coffe_shop.db"
            sql = """create table Product
               (ProductID integer,
               Name varchar ,
               Price real,
               primary key(ProductID))"""
            create_table(db_name, sql, "Product")
        elif opt==2:
            insert_data()
        elif opt==3:
            update_data()
        elif opt==4:
            delete_data()
        elif opt==5:
            select_data()
        elif opt==0:
            end=True
        else:
            print("Invalid opt")



