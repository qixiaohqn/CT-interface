import pymysql
#连接MySQL数据库
#输入数据库的IP地址，用户名，密码，端口
db=pymysql.connect(
                   host='10.225.98.209',
                   user='edux_data_w',
                   password='jBpTV2BysiKwakp_pzY9DG3B1X2aNh9j',
                   port=3306,

)
#使用cursor()方法创建一个游标对象
cursor=db.cursor()
#创建一个表
sqll='select * from clues_info where id=567942'

#使用cursor()方法执行sql语句
print(cursor.execute(sqll))
