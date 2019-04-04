import sqlite3


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
    db_name = "Coffe_shop.db"
    sql = """create table Product
    (ProductID integer,
    Name varchar ,
    Price real,
    primary key(ProductID))"""
    create_table(db_name,sql,"Product")