#!c:\Python37\python.exe
print('Content-type:text/html\r\n\r\n')
import cgi
import mysql.connector
form=cgi.FieldStorage()
name=form.getvalue('Name')
email=form.getvalue('Email')
message=form.getvalue('message')
if name=="" or email=="" or message=="":
	print("Bad data","some or all required\n Fields are blank")
else:
    db=mysql.connector.connect(host='localhost',database='food order',user='root',password='')
    cur=db.cursor()
    cur.execute("insert into contact(name,email,message) values('%s','%s','%s')"%(name,email,message))
    cur.close()
    db.commit()
    db.close()