import MySQLdb

db=MySQLdb.connect('localhost','root','','Medgulf')
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS PTNAME")
sql= """CREATE TABLE PTNAME (id INT NOT NULL AUTO_INCREMENT, FULL_NAME  CHAR(20) NOT NULL, AGE INT, APPNUMBER CHAR(20),VISITDATE INT,  PRIMARY KEY (id))"""

cursor.execute(sql)

db.close()


db=MySQLdb.connect('localhost','root','','Medgulf')
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS DIAGNOSIS")
sql= """CREATE TABLE DIAGNOSIS (id INT NOT NULL AUTO_INCREMENT, ICDCODE CHAR(10), DIAGNOSIS CHAR (30), PRIMARY KEY (id))"""

cursor.execute(sql)

db.close()


db=MySQLdb.connect('localhost','root','','Medgulf')
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS HOSPITALNAME")
sql= """CREATE TABLE HOSPITALNAME (id INT NOT NULL AUTO_INCREMENT, NAME CHAR(30) NOT NULL, PRIMARY KEY (id))"""
cursor.execute(sql)

db.close()

db=MySQLdb.connect('localhost','root','','Medgulf')
cursor=db.cursor()
cursor.execute("DROP TABLE IF EXISTS PTNAME_DIAGNOSIS_HOSPITALNAME")
sql="""CREATE TABLE PTNAME_DIAGNOSIS_HOSPITALNAME (PTNAME_id INT ,DIAGNOSIS_id INT,HOSPITALNAME_id INT )"""
cursor.execute(sql)
db.close()

#db=MySQLdb.connect('localhost','root','','Medgulf')
#cursor = db.cursor()
#sql= """CREATE TABLE PTNAME_HOSPITALNAME (
#  PTNAME_id int NOT NULL,
# HOSPITALNAME_id tinyint NOT NULL
#)