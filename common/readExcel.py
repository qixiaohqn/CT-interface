import  xlrd
import os
#当前路径
current_dir=os.path.abspath(__file__)
base_dir=os.path.dirname(os.path.dirname(current_dir))
excel_dir=base_dir+'//'+'testData'

class readExcel(object):
    #定义属性
    def __init__(self):
        self.readbook=xlrd.open_workbook(excel_dir+'//'+'data.xlsx')
        self.data_list=[]

    #定义方法
    def read(self):
        #定位sheet页
        sheet=self.readbook.sheet_by_index(0)
        #读取数据
        rownum=sheet.nrows
        for i in range(1,rownum):
            rowdata=sheet.row_values(i)
            self.data_list.append(rowdata)
        return self.data_list
if __name__ == '__main__':
    re=readExcel()
    print(re.read())


