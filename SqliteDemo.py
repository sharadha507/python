import sqlite3
con=sqlite3.connect("mydatabase.db")
cur=con.cursor()
#cur.execute("create table if not exists students(name varchar(50),email varchar(50),password varchar(50))")
#cur.execute('insert into students values("sharadha","101","A")')
#cur.execute('insert into students values("supriya","ID512","B")')
#cur.execute('insert into students values("sathya","ID513","C")')
#cur.execute('delete from students where name="sathya" ')
cur.execute('update students set name="sharadha" where email="ID514" ')
X=cur.execute('select *from students')
print(X.fetchall())
#x=cur.execute("show tables")
con.commit()
print(X)
