import MySQLdb

db =MySQLdb.connect('localhost','root','','Medgulf')

def insert(tablename,*columns):
    x =[]
    for item in columns:
        x.append(item)
    x_string =','.join(x)
    trial = "INSERT INTO %s (%s)"%(tablename,x_string)
    return trial

def select(arg,tablename, *coloums):
    y=[]
    for item in coloums:
        y.append(item)
    y_string = ','.join(y)
    print y_string
    trilas = "SELECT %s From %s Where %s ="%(arg,tablename,y_string)
    print trilas
    return y_string

select('*','ptname','Full_name')

def add_pt_database(name,age,app_number):
    cursor = db.cursor()
    #function that calls insert function
    sql = insert('ptname','Full_name','age','APPNUMBER')+""" VALUES ('%s','%d','%s')"""%(name,age,app_number)
    cursor.execute(sql)
    db.commit()

def add_diagnosis_database(diagnosis, icd = ""):
    cursor = db.cursor()
    #function that calls another function
    sql = insert('DIAGNOSIS','ICDCODE','DIAGNOSIS') +"""VALUES ('%s','%s')"""%(icd,diagnosis)
    cursor.execute(sql)
    db.commit()

def add_hospital_database(name):
    cursor = db.cursor()

    sql = insert('HOSPITALNAME','NAME') +"""VALUES ('%s')"""%(name)
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
        #print number
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
        #print number
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

    sql = insert('PTNAME_DIAGNOSIS_HOSPITALNAME','PTNAME_id','DIAGNOSIS_id','HOSPITALNAME_id')+"VALUES ('%d','%d','%d')"%(ptname_id,diagnosis_id, hospital_id)
    cursor.execute(sql)
    db.commit()


def print_screen():
        print("1- Enter 1 to enter pt name")
        print("5- Enter 2 to print Pt information")
        print("8- Enter 3 for exit")

        try:
            x= raw_input("Please enter Your Choice: ")
            x=int(x)
        except:
            ValueError
        return x

while True:
    choice= print_screen()

    if choice == 1:
        pt_name = str(raw_input("Please enter Pt name:"))
        pt_age = int(raw_input("Please enter pt age: "))
        diagnosis= str(raw_input("Please enter diagnosis:"))
        app_number = str(raw_input("Please enter approval number : "))
        hospital_number = int(raw_input(" Enter number for hospital : \n 1- AGH KHOBAR \n 2- Dossary \n 3- Fakhry \n 4- Al Salama  \n 5 - Al Yousef \n  6 - Astoon\n "))
        add_diagnosis_database(diagnosis)
        add_pt_database(pt_name,pt_age,app_number)
        pt_number = retriev_id_ptname(pt_name)
        diagnosis_number = retrive_id_diagnosis(diagnosis)
        linking_tables(pt_number,diagnosis_number,hospital_number)
        hospital_name = str(raw_input("Please enter hospital name :"))
        add_hospital_database(hospital_name)





    if choice == 2:
        cursor=db.cursor()
        sql = "SELECT Full_name FROM PTNAME"
        cursor.execute(sql)
        results_print = cursor.fetchall()
        x = 0
        for row in results_print:
            x +=1
            print  '',x,'-',row[0]

        print "Please enter A to search by name"
        print "Please enter B to search by Approval number"
        print "Please enter C to search by diagnosis"
        user_choice = str(raw_input("Please enter your choice A or B or C:"))
        user_choice = user_choice.lower()

        if user_choice == 'a':
            user_choice_name = str(raw_input("Please enter patient name : "))
            cursor=db.cursor()
            sql = "SELECT *FROM PTNAME WHERE FULL_NAME ='%s'"%user_choice_name
            cursor.execute(sql)
            resutls_usr = cursor.fetchall()
            how_many = len(resutls_usr)
            print 'Data base has %d patient with this name'%how_many
            for row in resutls_usr:
                print 'Patient name is ',row[1] , 'patient Age is ',row[2], 'patient approval number is',row[3], 'visit date is ',row[4]
                cursor=db.cursor()
                sql = "SELECT *FROM PTNAME_DIAGNOSIS_HOSPITALNAME  WHERE PTNAME_ID ='%d'"%row[0]
                try:
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    for row in results:
                        pt_id = row[0]
                        dg_id = row[1]
                        hp_id = row[2]
                    #print pt_id,dg_id,hp_id
                except:
                    print "Error: unable to fecth data"
                sql = "SELECT *FROM DIAGNOSIS WHERE ID ='%d'"%dg_id
                cursor.execute(sql)
                results_dg = cursor.fetchall()

                for row_dg in results_dg:
                    row_dg_new = row_dg[2]
                    print 'Diagnosis is %s'%row_dg_new

                sql = "SELECT * FROM HOSPITALNAME WHERE ID ='%d'"%hp_id
                cursor.execute(sql)
                results_hp = cursor.fetchall()
                for row in results_hp:
                    row_hp_new = row[1]
                    print 'In %s Hospital'%row_hp_new

        if user_choice == 'b':
            user_choice_name = str(raw_input("Please enter patient approval number : "))
            cursor=db.cursor()
            sql = "SELECT *FROM PTNAME WHERE APPNUMBER ='%s'"%user_choice_name
            cursor.execute(sql)
            resutls_usr = cursor.fetchall()
            how_many = len(resutls_usr)
            print 'Data base has %d patient with this Approval number'%how_many
            for row in resutls_usr:
                print 'Patient name is ',row[1] , 'patient Age is ',row[2], 'patient approval number is',row[3], 'visit date is ',row[4]
                cursor=db.cursor()
                sql = "SELECT *FROM PTNAME_DIAGNOSIS_HOSPITALNAME  WHERE PTNAME_ID ='%d'"%row[0]
                try:
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    for row in results:
                        pt_id = row[0]
                        dg_id = row[1]
                        hp_id = row[2]
                    #print pt_id,dg_id,hp_id
                except:
                    print "Error: unable to fecth data"
                sql = "SELECT *FROM DIAGNOSIS WHERE ID ='%d'"%dg_id
                cursor.execute(sql)
                results_dg = cursor.fetchall()

                for row_dg in results_dg:
                    row_dg_new = row_dg[2]
                    print 'Diagnosis is %s'%row_dg_new

                sql = "SELECT * FROM HOSPITALNAME WHERE ID ='%d'"%hp_id
                cursor.execute(sql)
                results_hp = cursor.fetchall()
                for row in results_hp:
                    row_hp_new = row[1]
                    print 'In %s Hospital'%row_hp_new




        """usr_select = int(raw_input("Please enter Pt number  from 1 to %s to get his/her data \n"%x))
        cursor=db.cursor()
        sql = "SELECT *FROM PTNAME_DIAGNOSIS_HOSPITALNAME  WHERE PTNAME_ID ='%d'"%usr_select
        try:
             cursor.execute(sql)
             results = cursor.fetchall()
             for row in results:
                 pt_id = row[0]
                 dg_id = row[1]
                 hp_id = row[2]
             #print pt_id,dg_id,hp_id
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

        print 'Pt name is : ', row_new
        print 'Diagnosis is :', row_dg_new
        print 'Hospital is :', row_hp_new
        print '\n\n'"""





    if choice == 3:
        db.close()
        exit()




