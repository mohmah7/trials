import xlrd

import MySQLdb

workbook = xlrd.open_workbook("/Users/mohamedmahmoud/Desktop/Medgulf/excel.xlsx")
worksheet = workbook.sheet_by_name('Sheet2')
num_rows = worksheet.nrows - 1
num_cells = worksheet.ncols - 1
curr_row = -1
while curr_row < num_rows:
	curr_row += 1
	row = worksheet.row(curr_row)
	print 'Row:', curr_row
	curr_cell = -1
	while curr_cell < num_cells:
		curr_cell += 1
		# Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
		cell_type = worksheet.cell_type(curr_row, curr_cell)
		cell_value = worksheet.cell_value(curr_row, curr_cell)
		print '	', cell_type, ':', cell_value, curr_cell


        if curr_cell == 3:
            print 'hi 3'
            db= MySQLdb.connect('localhost','root','','Medgulf')
            cursor=db.cursor()
            sql = """INSERT INTO PTNAME (FULL_NAME) VALUES ('%s')"""%(cell_value)
            cursor.execute(sql)
            db.commit()
            db.close()
        if curr_cell ==curr_cell:
            print 'hi'