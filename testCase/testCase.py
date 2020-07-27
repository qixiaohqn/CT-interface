'''
功能描述：获取测试数据，完成接口测试的请求，断言结果

解析：
1、调用readExcel模块，获取测试数据
2、跟进接口测试数据，进行请求
    2-1、-get请求，使用get方法
    2-2、-post请求，使用post方法
3、断言每个接口返回的数据
    3-1、成功
    3-2、失败
4、写入Excel


'''

from common import readExcel
import request,unittest
#python 编写的测试用例必须
class testCase(unittest.TestCase):

    def setUp(self) -> None:
        pass
# 1、调用readExcel模块，获取测试数据
    re=readExcel()
    test_data=re.read()
#2、跟进接口测试数据，进行请求
    def testRun(self):
        for i in
        id,url,name,method,param,expect=test_data[0]
        #接口地址，接口方法，接口参数，预期结果

        #2-1、-get请求，使用get方法
        if method=='get':
            pass

        # 2-2、-post请求，使用post方法
        elif method=='post':
            pass


#3、断言每个接口返回的数据
        assert (expect,real):
    #3-1、成功
    #3-2、失败
#4、写入Excel

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    tc=testCase()
    print(tc.test_data)
