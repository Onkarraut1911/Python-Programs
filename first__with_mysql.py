import mysql.connector as connector


class dbhelper:
    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306', user='root',
                                     password='onkarraut1911@mysqlserver', database='first__with_mysql')
        query = 'create table if not exists user(usrid int primary key,username varchar(200),phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("created")

    # insert
    def insert_user(self, usrid, username, phone):
        query = "insert into user(usrid,username,phone)values({},'{}','{}')".format(
            usrid, username, phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")

    # fech all
    def fetch_all(self):
        query = "select*from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("user id : ", row[0])
            print("user name : ", row[1])
            print("user phone : ", row[2])
            print()
            print()


# main coding
helper = dbhelper()
# helper.insert_user(1, "priya", "123")
helper.fetch_all()
