import xlrd

x = xlrd.open_workbook("/Users/mohamedmahmoud/Desktop/Medgulf/excel.xlsx")

worksheet = x.sheet_by_name('Sheet2')

num_rows = worksheet.nrows - 1

curr_row = -1

while curr_row < num_rows:
    curr_row += 1
    row = worksheet.row(curr_row)
    print row