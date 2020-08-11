import xlrd
#获取行数和列数
#row = sheet1.nrows#统计有多少行
#col = sheet1.ncols#统计有多少列
#print("行:"+str(row)+","+"列:"+str(col))

#获取整行和整列的值
#rowdata = sheet1.row_values(0)#获取第一行数据
#coldata = sheet1.col_values(0)#获取第一列数据
#print("行："+str(rowdata)+","+"列："+str(coldata))

#通过循环读取表格的所有行
#for i in range(sheet1.nrows):
    #print(sheet1.row_values(i))

#获取单元格的值
#print(sheet1.row(0)[0])
class ReadEx():
    def read_excel(self):

        workbook1 = xlrd.open_workbook("../Data/data2.xlsx") #打开工作簿对象
        sheet1 = workbook1.sheet_by_name("Sheet1") #获取一个工作表
        row_num = sheet1.nrows #获取总行数
        col_num = sheet1.ncols #获取总列数

        s =[]
        key = sheet1.row_values(0)

        if row_num <= 1:
            print("没有数据可读取！")
        else:
            j = 1
            for i in range(row_num-1):
                d ={}
                values = sheet1.row_values(j)
                for x in range(col_num):
                    d[key[x]] = values[x]
                j+=1
                s.append(d)
            return s



if __name__=='__main__':
    r = ReadEx()
    data1 = r.read_excel()
    print(data1)
