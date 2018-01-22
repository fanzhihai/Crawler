# coding=utf-8
import csv

my_file = 'C:\Users\jiao.fang.jiaofang\Desktop\\testdata.csv'
dates = csv.reader(file(my_file,'rb'))

for user in dates:
    print user[0]
    print user[1]
    print user[2]
    print user[3]

"""
异常
AssertionError
AttributeError
IOError
ImportError
IndentationError
IndexError
KeyError
NameError
SyntaxError
TypeError
ValueError



"""