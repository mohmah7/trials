import MySQLdb

db =MySQLdb.connect('localhost','root','','Medgulf')

def add_pt_database(name,age):
    cursor = db.cursor()
    sql = """INSERT INTO PTNAME (FULL_NAME, AGE) VALUES ('%s','%d')"""%(name,age)
    cursor.execute(sql)
    db.commit()

def add_diagnosis_database(diagnosis, icd = ""):
    cursor = db.cursor()
    sql = """INSERT INTO DIAGNOSIS (ICDCODE,DIAGNOSIS) VALUES ('%s','%s')"""%(icd,diagnosis)
    cursor.execute(sql)
    db.commit()

def add_hospital_database(name):
    cursor = db.cursor()
    sql = """INSERT INTO HOSPITALNAME (NAME) VALUES ('%s')"""%(name)
    cursor.execute(sql)
    db.commit()

def retriev_id_ptname(name):
    cursor=db.cursor()
    sql = "SELECT ID FROM PTNAME WHERE FULL_NAME ='%s'"% name
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            number = row[0]
        print number


    except:
        print "Error: unable to fetch data"
    return number


def retrive_id_diagnosis(name):
    cursor=db.cursor()
    sql = "SELECT ID FROM DIAGNOSIS WHERE DIAGNOSIS ='%s'"% name
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            number = row[0]
        print number
    except:
        print "Error: unable to fecth data"
    return number

def retrive_id_ptname(name):
    cursor=db.cursor()
    sql = "SELECT ID FROM PTNAME WHERE FULL_NAME ='%s'"% name
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            number = row[0]
        print number
    except:
        print "Error: unable to fecth data"
    return number

def linking_tables(ptname_id,diagnosis_id, hospital_id):
    cursor=db.cursor()
    sql = "INSERT INTO PTNAME_DIAGNOSIS_HOSPITALNAME (PTNAME_id,DIAGNOSIS_id, HOSPITALNAME_id) VALUES \
        ('%d','%d','%d')"%(ptname_id,diagnosis_id, hospital_id)
    cursor.execute(sql)
    db.commit()


def print_screen():
        print("1- Enter 1 to enter pt name")
        print("2- Enter 2 to enter visiting date")
        print("3- Enter 3 to enter hospital name")
        print("4- Enter 4 to enter diagnosis")
        print("5- Enter 5 to print Pt information")
        print("8- Enter 8 for exit")


        x= raw_input("Please enter Your Choice: ")
        x=int(x)
        return x

while True:
    choice= print_screen()

    if choice == 1:
        pt_name = str(raw_input("Please enter Pt name:"))
        pt_age = int(raw_input("Please enter pt age: "))
        diagnosis= str(raw_input("Please enter diagnosis:"))
        hospital_number = int(raw_input(" Enter number for hospital : \n 1- AGH KHOBAR \n 2- Dossary \n 3- Fakhry \n \
            4- Al Salama  \n 5 - Al Yousef \n  6 - Astoon\n "))
        add_diagnosis_database(diagnosis)
        add_pt_database(pt_name,pt_age)
        pt_number = retriev_id_ptname(pt_name)
        diagnosis_number = retrive_id_diagnosis(diagnosis)
        linking_tables(pt_number,diagnosis_number,hospital_number)

        print(pt_name, pt_age)




    if choice== 2:

        db = MySQLdb.connect("localhost","root","","Medgulf" )

        cursor = db.cursor()
        name='mohamed'

        sql = "SELECT id FROM ptname \
            WHERE full_name = '%s'"%name
        try:
             cursor.execute(sql)
             results = cursor.fetchall()
             for row in results:
                 number = row[0]
             print number


        except:
             print "Error: unable to fecth data"



    if choice == 3:
        hospital_name = str(raw_input("Please enter hospital name :"))
        add_hospital_database(hospital_name)

    if choice == 4:
        diagnosis_usr = str(raw_input("Please enter diagnosis:"))
        add_diagnosis_database(diagnosis=diagnosis_usr)


    if choice == 5:
        cursor=db.cursor()
        sql = "SELECT Full_name FROM PTNAME"
        cursor.execute(sql)
        results_print = cursor.fetchall()
        x = 0
        for row in results_print:
            x +=1
            print  '',x,'-',row[0]
        usr_select = int(raw_input("Please enter Pt number  from 1 to %s to get his/her data \n"%x))
        cursor=db.cursor()
        sql = "SELECT *FROM PTNAME_DIAGNOSIS_HOSPITALNAME  WHERE PTNAME_ID ='%d'"%usr_select
        try:
             cursor.execute(sql)
             results = cursor.fetchall()
             for row in results:
                 pt_id = row[0]
                 dg_id = row[1]
                 hp_id = row[2]
             print pt_id,dg_id,hp_id
        except:
             print "Error: unable to fecth data"

        cursor=db.cursor()
        sql = "SELECT *FROM PTNAME WHERE ID ='%d'"%pt_id
        cursor.execute(sql)
        results_pt= cursor.fetchall()
        for row in results_pt:
            row_new=row[1]

        sql = "SELECT *FROM DIAGNOSIS WHERE ID ='%d'"%dg_id
        cursor.execute(sql)
        results_dg = cursor.fetchall()

        for row_dg in results_dg:
            row_dg_new = row_dg[2]

        sql = "SELECT * FROM HOSPITALNAME WHERE ID ='%d'"%hp_id
        cursor.execute(sql)
        results_hp = cursor.fetchall()
        for row in results_hp:
            row_hp_new = row[1]

        print 'Pt name is : ', row_new, 'Diagnosis is :', row_dg_new, 'Hospital is :', row_hp_new





    if choice == 8:
        db.close()
        exit()




