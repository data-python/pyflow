import sqlite3


conn = sqlite3.connect('test.db')
c = conn.cursor()
print ("数据库打开成功")

c.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
      VALUES ('Paul', 32, 'California', 20000.00 )")

c.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
      VALUES ('Allen', 25, 'Texas', 15000.00 )")

c.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
      VALUES ('Teddy', 23, 'Norway', 20000.00 )")

c.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
      VALUES ('Mark', 25, 'Rich-Mond ', 65000.00 )")

conn.commit()
print ("数据插入成功")
conn.close()