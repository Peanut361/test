import xlsxwriter
workbook = xlsxwriter.Workbook(r'C:\Users\16209\Desktop\test.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', '订单编号')
worksheet.write('B1', '用户名称')

a = 123456

for i in range(2, 100):
    a = a+1
    worksheet.write('A' + str(i), a)
    worksheet.write('B' + str(i), '一个用户')
workbook.close()



